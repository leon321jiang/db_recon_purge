# AWS Lambda Function for db recon and purge

This AWS Lambda function is designed to manage RDS instances by testing connections, 
logging unreachable hosts, iterating over a list of database, and 
resetting passwords if needed.

## Files

- `db_conn.py`: Contains the function to test connections to RDS instances.
- `dynamo_ops.py`: Provides functions to log unreachable hosts to a DynamoDB table and delete records.
- `iterate_list.py`: Iterates over a list of database configurations and uses other functions as needed.
- `reset_password.py`: A dummy function to reset the RDS instance master user password.

## Setup

1. Ensure AWS CLI is configured with the necessary permissions.
2. Install the required Python packages:
```
pip install boto3
```

3. Deploy the Python files to AWS Lambda.

## Deployment

Create a zip file with all the Python scripts and upload it to AWS Lambda as a function package.
Make sure the IAM role associated with the Lambda function has the necessary permissions.


## IAM Permissions

The Lambda function requires the following IAM permissions:
- DynamoDB: PutItem, DeleteItem

## Logging

Logs are automatically managed by AWS Lambda and can be viewed in Amazon CloudWatch.

## Security Note

Do not hardcode sensitive information like database passwords. Use AWS Secrets Manager or environment variables.
