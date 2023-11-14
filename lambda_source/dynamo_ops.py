import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
db_list_table_name = 'onboarded_db_list'
archive_table_name = 'records_deleted'

def delete_db_host_record(db_host):
    table_original = dynamodb.Table(db_list_table_name)
    table_archive = dynamodb.Table(archive_table_name)

    try:
        # read item to be delieted
        item = table_original.get_item(
            Key={
                'db_host': db_host
            }
        )
    except ClientError as e:
        print(f"Error reading record for host {db_host} with error: {e}")
        return {'statusCode': 581, 'body': f"Error reading record for host {db_host} with error: {e}"}
    
    try:
        # archive the item to be deleted 
        table_archive.put_item(
            Item = item
        )
    except ClientError as e:
        print(f"Error archiving record for host {db_host} with error: {e}")
        return {'statusCode': 582, 'body': f"Error archiving record for host {db_host} with error: {e}"}
    
    try:
        #deleting records
        table_original.delete_item(
            Key={
                'db_host': db_host
            }
        )
        print(f"Successfully deleted record {db_host}.")
        return {'statusCode': 200, 'body': f"Successfully deleted record {db_host}."}
    except ClientError as e:
        print(f"Error deleting record from {db_list_table_name}: {e}")
        return {'statusCode': 583, 'body': f"Error deleting record from {db_list_table_name}: {e}"}

#TODO need proper exception handling

def update_db_writer_arn(db_host):
    print(f"updating db writer arn for {db_host}")
    #TODO add real function