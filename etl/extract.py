import pandas as pd


def load_csv_to_db(csv_path: str, table_name: str, engine):
    
    print(f"Loading {csv_path} into table '{table_name}'...")

    df = pd.read_csv(csv_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into '{table_name}'")




def run_extract(engine):
    

    load_csv_to_db( "data/attributes.csv" , "players" , engine )
    load_csv_to_db("data/epl.csv", "matches", engine)

    print("✔ Table loaded into pgsql")


if __name__ == "__main__":
    from run_pipeline import get_engine
    engine = get_engine()
    run_extract(engine)

