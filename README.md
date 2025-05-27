# Snowflake FastAPI CSV Uploader

A FastAPI application for uploading CSV data to Snowflake tables.

## Features

- Upload CSV files to Snowflake tables (departments, jobs, hired_employees)
- Automatic type conversion (handles numpy/pandas types)
- Data validation and error handling
- REST API endpoint for easy integration

## Prerequisites

- Python 3.9+
- Snowflake account with proper credentials
- Required Python packages see requirements.txt

## Project Structure

### Descriptions:

| File/Folder         | Purpose |
|---------------------|---------|
| `app/__init__.py`   | Makes app a Python package |
| `app/db.py`         | Snowflake connection handler |
| `app/main.py`       | FastAPI endpoints and routes |
| `app/models.py`     | Snowflake table DDL definitions |
| `app/upload.py`     | CSV processing and upload logic |
| `data/`             | Sample CSV files for testing |
| `.env`              | Template for environment variables |
| `requirements.txt`  | Python dependencies |
| `init_tables.py`    | Script to initialize database tables |
| `README.md`         | Project documentation |


## Usage

### 1. Start the FastAPI Server
```bash
uvicorn app.main:app --reload
```

### 2. Initialize Snowflake Tables

```bash
python init_tables.py
```

### 3. Upload CSV Files via API Endpoints

#### Upload Departments
```bash
curl -X POST "http://localhost:8000/upload/departments" \
  -F "file=@data/departments.csv"
```

#### Upload Jobs
```bash
curl -X POST "http://localhost:8000/upload/jobs" \
  -F "file=@data/jobs.csv"
```

#### Hired Employees
```bash
curl -X POST "http://localhost:8000/upload/hired_employees" \
  -F "file=@data/hired_employees.csv"
```
