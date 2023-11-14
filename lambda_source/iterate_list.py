import boto3
from botocore.exceptions import ClientError
from db_conn import test_db_connection
from dynamo_ops import log_unreachable_host_record, delete_dynamodb_record
from reset_password import reset_user_password


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
        conn = test_db_connection(db_info['db_engine'], db_info['db_host'], db_info['db_name'], db_info['db_user'], db_info['db_password'])
        if conn['statusCode'] == 592: # "failed to connect to" 
            log_unreachable_host_record(db_info['db_host'], db_info['db_name'], db_info['db_user'])
            delete_dynamodb_record(db_info['db_name'])
        elif conn['statusCode'] == 593: #"failed to authenticate"
            reset_user_password(db_info['db_host'], db_info['db_user'])
        elif conn['statusCode'] == 200:  #"successfully connected to"
            print(f"successfuly connected to {db_info['db_host']}")
            return
        else:
            print(f"An error occurred with stau code: {conn['statusCode']}, and error message: {conn['body']}")


