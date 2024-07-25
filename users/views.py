from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer
from .models import User
from luxswipeback.dynamodb import DynamoDB

class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            db = DynamoDB()
            
            data = {
                'username': user.username,
                'SK': 'PROFILE',
                'uid': user.uid,
                'name': user.name,
            }
            
            # only add bio to the data if it's provided
            # if user.bio:
            #     data['bio'] = user.bio
            
            db.add_user(data)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def retrieve_user(self, request):
        uid = request.data.get('uid')
        if not uid:
            return Response({'error': 'UID is required'}, status=status.HTTP_400_BAD_REQUEST)

        db = DynamoDB()
        user_details = db.get_user(uid)
        if user_details:
            return Response(user_details, status=status.HTTP_200_OK)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['post'])
    def check_username(self, request):
        username = request.data.get('username')
        if not username:
            return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        db = DynamoDB()
        user_details = db.check_user(username)
        if user_details:
            return Response({'available': False}, status=status.HTTP_200_OK)
        return Response({'available': True}, status=status.HTTP_200_OK)


    