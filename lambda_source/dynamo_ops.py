import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
db_list_table_name = 'onboarded_db_list'
deleted_table_name = 'records_deleted'

def log_unreachable_host_record(db_name, db_host, db_user):
    table = dynamodb.Table('records_deleted')
    try:
        table.put_item(
            Item={
                'db_host': db_host,
                'db_name': db_name,
                'db_user': db_user
            }
        )
        print("Logged unreachable host record.")
    except ClientError as e:
        print(f"Error logging unreachable host record: {e}")

def delete_dynamodb_record(db_host):
    table = dynamodb.Table(db_list_table_name)
    try:
        table.delete_item(
            Key={
                'db_host': db_host
            }
        )
        print(f"Deleted record from {db_list_table_name}.")
    except ClientError as e:
        print(f"Error deleting record from {db_list_table_name}: {e}")

#TODO need proper exception handling