from fastapi import FastAPI, UploadFile, File, HTTPException
import io
import pandas as pd
from app.upload import upload_csv_to_table

app = FastAPI()

VALID_TABLES = {
    "departments": {
        "columns": ["id", "department"],
        "description": "Department IDs and names"
    },
    "jobs": {
        "columns": ["id", "job"],
        "description": "Job IDs and titles"
    },
    "hired_employees": {
        "columns": ["id", "name", "datetime", "department_id", "job_id"],
        "description": "Employee hiring records"
    }
}

@app.post("/upload/{table_name}")
async def upload_file(table_name: str, file: UploadFile = File(...)):
    table_name = table_name.lower()
    
    if table_name not in VALID_TABLES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid table name. Valid options: {list(VALID_TABLES.keys())}"
        )

    try:
        contents = await file.read()
        df = pd.read_csv(
            io.StringIO(contents.decode('utf-8')),
            header=None,
            names=VALID_TABLES[table_name]["columns"],
            dtype={'id': 'Int64', 'department_id': 'Int64', 'job_id': 'Int64'}
        )
        
        # Basic validation
        if df.empty:
            raise ValueError("File is empty")
        if list(df.columns) != VALID_TABLES[table_name]["columns"]:
            raise ValueError("Column mismatch")
            
        upload_csv_to_table(df, table_name)
        return {
            "status": "success",
            "table": table_name,
            "rows_uploaded": len(df)
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Upload failed: {str(e)}"
        )