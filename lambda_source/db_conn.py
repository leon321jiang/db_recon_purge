import pymysql
import oracledb
import psycopg2

def test_db_connection(db_engine, db_host, db_name, db_user, db_password):
    try:
        if db_engine == 'mysql':
            conn = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name, connect_timeout=5)
        elif db_engine == 'oracle':
            # Set the DSN (Data Source Name)
            dsn = oracledb.makedsn(host=db_host, port=1521, service_name=db_name)
            # Connect to the database
            conn = oracledb.connect(user=db_user, password=db_password, dsn=dsn)
        elif db_engine == 'postgres':
            conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
        else:
            print(f"Unsupported database engine {db_engine}")
            return {'statusCode': 591, 'body': f"Unsupported database engine {db_engine}"}
   
        # If the connection is successful, do nothing
        print(f"Successfully connected to {db_host}")
        conn.close()
        return {'statusCode': 200, 'body': f"Successfully connected to {db_host}"}

    except Exception as e:
        print(str(e))
        if "not known" in str(e).lower() or "Network is unreachable" in str(e).lower():
            # Host not reachable for MySQL, Oracle, PostgreSQL
            print(f"failed to reach to {db_host}")
            return {'statusCode': 592, 'body': f"Failed to reach to {db_host}"}

        elif "access denied" in str(e).lower():
            # Failed to authenticate 
            #TODO add authentication failures of postgres and Oracle, currenly it only supports mySQL
            print(f"failed to authenticate to {db_host} with user {db_user}")
            return {'statusCode': 593, 'body': f"Failed to authenticate to {db_host} with user {db_user}"}
        else:
            print(f"An error occurred: {e}")
            return {'statusCode': 599, 'body': f"An error occurred: {e}"}


