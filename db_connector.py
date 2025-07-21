import psycopg2
import mysql.connector

def connect_db(config):
    if config["db_type"] == "PostgreSQL":
        return psycopg2.connect(
            host=config["host"],
            port=config["port"],
            dbname=config["database"],
            user=config["user"],
            password=config["password"]
        )
    elif config["db_type"] == "MySQL":
        return mysql.connector.connect(
            host=config["host"],
            port=config["port"],
            database=config["database"],
            user=config["user"],
            password=config["password"]
        )
    else:
        raise ValueError("Unsupported database type")

def test_connection(config):
    try:
        conn = connect_db(config)
        conn.close()
        return True, "Connection successful!"
    except Exception as e:
        return False, str(e)
