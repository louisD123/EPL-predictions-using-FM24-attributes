import os 
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv




load_dotenv()


# prep the connection to the pgsql server

def get_engine():
    
    # get the url from your .env

    user = os.getenv("PG_USER")
    password = os.getenv("PG_PASS")
    host = os.getenv("PG_HOST")
    port = os.getenv("PG_PORT")
    db = os.getenv("PG_DB")

    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    # returns the connection switch to be used later
    return create_engine(url)


def load_csv_to_db(csv_path: str, table_name: str, engine):
    """Load a CSV into PostgreSQL."""
    print(f"Loading {csv_path} into table '{table_name}'...")
    df = pd.read_csv(csv_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",   # or "append"
        index=False
    )
    print(f"✔ Loaded {len(df)} rows into {table_name}")

def main():
    engine = get_engine()

    # Example: two CSVs
    load_csv_to_db("data/attributes.csv", "players", engine)
    load_csv_to_db("data/epl.csv", "matches", engine)

    print("All done.")

if __name__ == "__main__":
    main()

