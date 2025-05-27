import pandas as pd
import numpy as np
from app.db import get_connection
from app.models import TABLES_DDL

def convert_numpy_types(value):
    """Convert numpy types to native Python types"""
    if pd.isna(value):
        return None
    if isinstance(value, (np.integer, np.int64)):
        return int(value)
    if isinstance(value, (np.floating, np.float64)):
        return float(value)
    if isinstance(value, (np.bool_)):
        return bool(value)
    return str(value) if isinstance(value, (np.str_, np.object_)) else value

def create_tables():
    """Initialize all tables in Snowflake"""
    conn = None
    try:
        conn = get_connection()
        with conn.cursor() as cs:
            for table_name, ddl in TABLES_DDL.items():
                print(f"Creating table {table_name}...")
                cs.execute(ddl)
        conn.commit()
        print("✅ All tables created successfully!")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()

def upload_csv_to_table(df: pd.DataFrame, table_name: str):
    """Upload DataFrame to specified table"""
    conn = None
    try:
        # Convert all data to proper types
        df = df.applymap(convert_numpy_types)
        
        # Replace any remaining NA/NaN with None
        df = df.where(pd.notnull(df), None)
        
        conn = get_connection()
        with conn.cursor() as cs:
            # Prepare data - convert to list of tuples with native types
            data = []
            for row in df.itertuples(index=False, name=None):
                cleaned_row = tuple(convert_numpy_types(x) for x in row)
                data.append(cleaned_row)
            
            # Generate INSERT statement
            cols = ', '.join(df.columns)
            placeholders = ', '.join(['%s'] * len(df.columns))
            query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
            
            # Execute in batches
            cs.executemany(query, data)
            conn.commit()
            
        print(f"Successfully uploaded {len(data)} rows to {table_name}")
        
    except Exception as e:
        print(f"Upload error: {e}")
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()