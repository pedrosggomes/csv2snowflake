import os
from dotenv import load_dotenv
import snowflake.connector

load_dotenv()

def get_connection():
    print("SNOWFLAKE_ACCOUNT:", os.getenv("SNOWFLAKE_ACCOUNT"))  # debug print
    
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        role=os.getenv("SNOWFLAKE_ROLE"),
        authenticator="externalbrowser"
    )
