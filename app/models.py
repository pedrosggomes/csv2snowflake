TABLES_DDL = {
    "departments": """
        CREATE TABLE IF NOT EXISTS departments (
            id NUMBER PRIMARY KEY,
            department VARCHAR
        )
    """,
    "jobs": """
        CREATE TABLE IF NOT EXISTS jobs (
            id NUMBER PRIMARY KEY,
            job VARCHAR
        )
    """,
    "hired_employees": """
        CREATE TABLE IF NOT EXISTS hired_employees (
            id NUMBER PRIMARY KEY,
            name VARCHAR,
            datetime TIMESTAMP_NTZ,
            department_id NUMBER,
            job_id NUMBER,
            FOREIGN KEY (department_id) REFERENCES departments(id),
            FOREIGN KEY (job_id) REFERENCES jobs(id)
        )
    """
}
