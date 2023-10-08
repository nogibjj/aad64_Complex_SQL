"""Query the database"""
import os
from databricks import sql
from dotenv import load_dotenv


def general_query(query):
    """runs a query a user inputs"""

    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
        c.close()
    return result


def run_queries_from_file(sql_file_path, md_file_path):
    with open(sql_file_path, "r") as f:
        sql_file = f.read()
    queries = sql_file.split(";")
    with open(md_file_path, "w") as f:
        for query in queries:
            if query.strip():
                result = general_query(query)
                f.write(f"```sql\n{query}\n```\n\n")
                f.write(f"```response from database\n{result}\n```\n\n")
