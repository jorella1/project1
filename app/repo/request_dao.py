
import psycopg2
from app.models.request_dto import Request
from app.models.user_dto import User

from .connection import get_connection


def new_reimbursement_request(login_dto:User,amount,reason):
    connection = get_connection()
    cursor = connection.cursor()
    status = "pending"
    qry = "INSERT INTO reimbursements VALUES (default,%s,%s,%s,%s,%s) RETURNING request_id;"

    try:
        cursor.execute(qry,(login_dto.id,amount,reason,status,login_dto.username))
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

    qry = f"UPDATE reimbursements SET status='{status}' WHERE request_id={request_id} returning user_id;"

    try:
        cursor.execute(qry)
        account_id = cursor.fetchone()
        connection.commit()
        return account_id
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()

def cancel_user_request(request_id):
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

def get_request(request_id) -> Request:
    connection = get_connection()
    cursor = connection.cursor()
    
    qry = f"SELECT * FROM reimbursements WHERE request_id = {request_id};"

    try:
        cursor.execute(qry)
        record = cursor.fetchone()
        if record is not None:
            request = Request(record[0],record[1],record[2],record[3],record[4],record[5])
            connection.commit()
            return request
        return None
        
       
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()


def get_request_table():
    connection = get_connection()
    cursor = connection.cursor()
    qry = "SELECT * FROM reimbursements;"
    requests = []
    try:
        cursor.execute(qry)
        records = cursor.fetchall()
        if records is not None:
            for rec in records:
                request = Request(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5])
                requests.append(request)
            connection.commit()
            return requests
        return None
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()

def get_user_requests(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    qry = f"SELECT * FROM reimbursements where user_id = {user_id};"
    requests = []
    try:
        cursor.execute(qry)
        records = cursor.fetchall()
        if records is not None:
            for rec in records:
                request = Request(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5])
                requests.append(request)
            connection.commit()
            return requests
        return None
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()
