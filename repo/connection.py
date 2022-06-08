import psycopg2

def get_connection():
    connection = psycopg2.connect(
        database = "postgres",
        user = "postgres",
        password = "project1pass",
        host = "project1.csqmpqer3gcj.us-east-2.rds.amazonaws.com",
        port = "5432"
    )
    return connection
    