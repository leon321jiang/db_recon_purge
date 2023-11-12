import pymysql
import cx_Oracle
import psycopg2
from dynamo_ops import log_unreachable_host_record, delete_dynamodb_record
from reset_password import reset_user_password

def test_db_connection(db_engine, db_host, db_name, db_user, db_password):
    try:
        if db_engine == 'mysql':
            print("mysql")
            conn = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
            conn = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name, connect_timeout=5)
        elif db_engine == 'oracle':
            dsn = cx_Oracle.makedsn(db_host, 1521, service_name=db_name)
            conn = cx_Oracle.connect(user=db_user, password=db_password, dsn=dsn)
        elif db_engine == 'postgres':
            conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
        else:
            print("Unsupported database engine")
            return

        # If the connection is successful, do nothing
        print(f"successful connected to {db_host}")
        conn.close()

    except Exception as e:
        if "not known" in str(e) or "Network is unreachable" in str(e):
            # Host not reachable for MySQL, Oracle, PostgreSQL
            print(f"failed to reach to {db_host}")
            log_unreachable_host_record(db_host, db_name, db_user)
            delete_dynamodb_record(db_name)
        elif isinstance(e, (pymysql.OperationalError, cx_Oracle.DatabaseError, psycopg2.OperationalError)) and 'authentication' in str(e).lower():
            # Failed to authenticate
            print(f"failed to authenticate to {db_host} with user {db_user}")
            reset_user_password(db_host, db_user)
        else:
            print(f"An error occurred: {e}")


