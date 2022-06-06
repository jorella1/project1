import psycopg2

def get_connection():
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="revpword",
        host="project0db.c9ikmmxypxlz.us-east-1.rds.amazonaws.com",
        port="5432"
    )
    return connection