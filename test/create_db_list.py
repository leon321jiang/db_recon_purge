import boto3
from botocore.exceptions import ClientError

# Initialize a session using Amazon DynamoDB
session = boto3.Session()
dynamodb = session.resource('dynamodb')
db_list_table_name = 'onboarded_db_list'

def create_db_list(option):
    # Define the table
    table = dynamodb.Table('onboarded_db_list')
    temp_mysql_host = 'mydbinstance.cu53kqprya26.us-west-2.rds.amazonaws.com'

    # Define the items to insert
    items_good = [
        {
            'db_host': temp_mysql_host,
            'db_engine': 'mysql',
            'db_name': 'testrdsmysql',
            'db_user': 'db_admin',
            'db_password': 'QASEFduey34!'
        },
        {
            'db_host': 'testrdsoracle-host',
            'db_engine': 'oracle',
            'db_name': 'database2-name',
            'db_user': 'db_admin',
            'db_password': 'QASEFduey34!'
        },
        {
            'db_host': 'testrdspostgres-host',
            'db_engine': 'postgres',
            'db_name': 'database3-name',
            'db_user': 'db_admin',
            'db_password': 'QASEFduey34!'
        },
        {
            'db_host': 'database4',
            'db_engine': 'sqlserver',
            'db_name': 'database4-name',
            'db_user': 'admin4',
            'db_password': 'dkedl38578374d!@'
        }
    ]

    items_incorrect_pass = [
        {
            'db_host': temp_mysql_host,
            'db_engine': 'mysql',
            'db_name': 'testrdsmysql',
            'db_user': 'db_admin',
            'db_password': 'QASEFduey34!ddddd'
        },
        {
            'db_host': 'testrdsoracle-host',
            'db_engine': 'oracle',
            'db_name': 'database2-name',
            'db_user': 'db_admin',
            'db_password': 'QASEFduey34!ddddd'
        },
        {
            'db_host': 'testrdspostgres',
            'db_engine': 'postgres',
            'db_name': 'database3-host',
            'db_user': 'db_admin',
            'db_password': 'QASEFduey34!dddd'
        },
        {
            'db_host': 'database4',
            'db_engine': 'sqlserver',
            'db_name': 'database4-host',
            'db_user': 'admin4',
            'db_password': 'dkedl38578374d!@'
        }
    ]
    if option == 'good_password':
        items = items_good
    else:
        items = items_incorrect_pass

    # Write items to the table
    for item in items:
        try:
            print(f"Adding item: {item['db_host']}")
            response = table.put_item(Item=item)
            print(f"Item added: {item['db_host']}", response)
        except ClientError as e:
            print(f"Error adding item {item['db_host']}: {e.response['Error']['Message']}")

    print("Script completed.")
