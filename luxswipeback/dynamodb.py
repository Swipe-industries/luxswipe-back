import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError


load_dotenv()

class DynamoDB:
    def __init__(self):
        self.dynamodb = boto3.resource(
            "dynamodb",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION_NAME")
        )
        self.table = self.dynamodb.Table("LuxSwipe")

    #define other database operations(CRUD) over here
    def add_user(self, data):
        """
        
        This function adds the items to the database
        
        'username': unique username of the user of LuxSwipe
        'SK': 'PROFILE' used for sorting the data
        'uid': firebase uid to identify the user's username
        'name' : user's name
        'bio': description of the user's profile
        
        """
        try:
            self.table.put_item(Item = data)
            print("User added successfully.")
            
        except ClientError as e:
            print(f"An error occured: {e.response['Error']['Message']}")
            raise
        
        except Exception as e:
            print(f"An unexpected error occured: {e}")
            raise
    
    def get_user(self, uid):
        """
        
        Fetch user details from DynamoDB using uid.
        
        :param uid: The value of the uid to search for
        :return: User details if found, else None
            
        """
        try:
            response = self.table.query(
                IndexName= 'uid-index',  # Replace 'uid-index' with your GSI name
                KeyConditionExpression='uid = :uid AND SK = :sk',
                ExpressionAttributeValues={':uid': uid, ':sk': 'PROFILE'}
            )
            items = response.get('Items', [])
            if items:
                return items[0]  # Assuming uid is unique and returns a single item

        except ClientError as e:
            print(f"An error occurred: {e.response['Error']['Message']}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
        
    def check_user(self, username):
        """
        
        Checks either the username is awailable or not
        
        :param username: the username to check if it's unique or not
        :return: User details if found, else None
        
        """
        
        try:
            response = self.table.get_item(
                Key={
                    'username': username,
                    'SK': 'PROFILE'
                }
            )
            return response.get('Item', None)
        except ClientError as e:
            print(f"An error occurred: {e.response['Error']['Message']}")
            return None #handle the error at frontend if return type is None
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None