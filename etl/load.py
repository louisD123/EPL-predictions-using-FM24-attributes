import pandas as pd
import os

def table_to_csv(engine, table_name, out_folder="data"):
    os.makedirs(out_folder, exist_ok=True)

    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql(query, engine)

    out_path = os.path.join(out_folder, f"{table_name}.csv")
    df.to_csv(out_path, index=False)

    print(f"[LOAD] Saved {table_name} → {out_path}")


def run_load(engine):
    
    tables = ["train"]  # add more tables if needed
    for t in tables:
        table_to_csv(engine, t)

