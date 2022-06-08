import psycopg2
from repo.connection import get_connection
from models.user_dto import User

def new_reimbursement_request(login_dto:User,amount,reason):
    connection = get_connection()
    cursor = connection.cursor()
    status = "pending"
    qry = "INSERT INTO reimbursements VALUES (default,%s,%s,%s,%s) RETURNING request_id;"

    try:
        cursor.execute(qry,(login_dto.id,amount,reason,status))
        account_id = cursor.fetchone()[0]
        connection.commit()
        return account_id
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()

def alter_request_status(request_id,status):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "UPDATE reimbursements set status='{status}' where request_id='{request_id}';"

    try:
        cursor.execute(qry)
        account_id = cursor.fetchone()[0]
        connection.commit()
        return account_id
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()

def cancel_request(request_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"DELETE FROM reimbursements WHERE request_id = {request_id};"
    
    try:
        cursor.execute(qry)
        print(qry)
        connection.commit()
        return "Request Deleted"

    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()

def get_request(request_id):
    connection = get_connection()
    cursor = connection.cursor()
    qry = "SELECT * FROM reimbursements WHERE request_id = '{request_id}' RETURNING request_id;"

    try:
        cursor.execute(qry)
        request_id = cursor.fetchone()
        connection.commit()
        return request_id
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()