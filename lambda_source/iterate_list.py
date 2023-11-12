import boto3
from botocore.exceptions import ClientError
from db_conn import test_db_connection

dynamodb = boto3.resource('dynamodb')
onboarded_db_list = 'onboarded_db_list'

def iterate_list(event, context):
    # Read the list of databases from the 'onboarded_db_list' DynamoDB table
    onboarded_db_list_table = dynamodb.Table(onboarded_db_list)
    try:
        onboarded_dbs = onboarded_db_list_table.scan().get('Items', [])
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'statusCode': 500, 'body': e.response['Error']['Message']}

    # Process each onboarded database
    for db_info in onboarded_dbs:
        test_db_connection(db_info['db_engine'], db_info['db_host'], db_info['db_name'], db_info['db_user'], db_info['db_password'])