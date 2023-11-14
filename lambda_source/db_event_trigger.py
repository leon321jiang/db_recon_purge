import boto3
from dynamo_ops import delete_db_host_record, update_db_writer_arn
from reset_password import reset_user_password

dynamodb = boto3.resource('dynamodb')
onboarded_db_list = 'onboarded_db_list'

def db_recon(event, context):
    '''
    A lambda to monitor various trigger events from db lifecycle changes such as db failover, deletion, restoration from a db snapshot
    '''

    try:
        if event['eventType'] == 'dbDeletion':
            return delete_db_host_record(event['db_host'])
        
        elif event['eventType'] == 'restoreFromSnapshot':
            #TODO add code to compare timesnap
            #If this is a snapshot was taken before the last password rotation, then password needs to be reset
            if event['SnapshotTime'] < 'LAST PASSWORD ROTATION TIME':
                return reset_user_password(event['db_host'], event['db_name'])
            #otherwise, do nothing 

        elif event['eventType'] == 'dbFailover':
            return update_db_writer_arn(event['db_host'], event['db_writer_arn'])
        
        else:
            return {'statusCode': 416, 'body': 'unsupported eventType'}
        
    except Exception as e:
        return {'statusCode': 400, 'body': f'bad reqeust {e}'}