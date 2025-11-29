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



