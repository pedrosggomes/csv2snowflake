from app.upload import create_tables

if __name__ == "__main__":
    print("Initializing database tables...")
    create_tables()
    print("Done!")