from lambda_source.db_helper import test_db_connection
from lambda_source.dynamo_ops import log_unreachable_host_record, delete_dynamodb_record
from lambda_source.reset_password import reset_user_password
from lambda_source.iterate_list import iterate_list
from create_db_list import create_db_list

# direct connect 
#test_db_connection('mysql', 'mydb-instance.cg034hpkmmjt.us-west-2.rds.amazonaws.com', 'mydbname', 'mydbuser', 'mydbpassword')

# create a list with a mixture of dummy and real db instance info 
#create_db_list('good_password')

# iterate a list from dynamodb table
#iterate_list('dummy_event','dummy_context')

# create a list with a mixture of dummy and real db instance info but bad passord
create_db_list('incorrect_password')

# iterate a list from dynamodb table
iterate_list('dummy_event','dummy_context')