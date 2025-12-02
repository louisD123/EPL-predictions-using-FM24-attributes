import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import extract
import transform
import load

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





if __name__ == "__main__":
    engine = get_engine()
    extract.run_extract(engine)
    transform.run_transform(engine)
    load.run_load(engine)


