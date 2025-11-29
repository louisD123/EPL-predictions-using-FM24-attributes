import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


# create engine


def get_engine():
   
    user = os.getenv("PG_USER")
    password = os.getenv("PG_PASS")
    host = os.getenv("PG_HOST")
    port = os.getenv("PG_PORT")
    db = os.getenv("PG_DB")

    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url)