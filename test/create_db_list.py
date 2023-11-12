import boto3
from botocore.exceptions import ClientError

# Initialize a session using Amazon DynamoDB
session = boto3.Session()
dynamodb = session.resource('dynamodb')
db_list_table_name = 'onboarded_db_list'

def create_db_list():
    # Define the table
    table = dynamodb.Table('onboarded_db_list')
    temp_mysql_host = 'mydbinstance.cu53kqprya26.us-west-2.rds.amazonaws.com'

    # Define the items to insert
    items = [
        {
            'db_name': 'testrdsmysql',
            'db_engine': 'mysql',
            'db_host': temp_mysql_host,
            'db_user': 'db_admin',
            'db_password': 'QASEFduey34!'
        },
        {
            'db_name': 'testrdsoracle',
            'db_engine': 'oracle',
            'db_host': 'database2-host',
            'db_user': 'db_admin',
            'db_password': 'QASEFduey34!'
        },
        {
            'db_name': 'testrdspostgres',
            'db_engine': 'postgres',
            'db_host': 'database3-host',
            'db_user': 'db_admin',
            'db_password': 'QASEFduey34!'
        },
        {
            'db_name': 'database4',
            'db_engine': 'sqlserver',
            'db_host': 'database4-host',
            'db_user': 'admin4',
            'db_password': 'dkedl38578374d!@'
        }
    ]

    # Write items to the table
    for item in items:
        try:
            print(f"Adding item: {item['db_name']}")
            response = table.put_item(Item=item)
            print(f"Item added: {item['db_name']}", response)
        except ClientError as e:
            print(f"Error adding item {item['db_name']}: {e.response['Error']['Message']}")

    print("Script completed.")
