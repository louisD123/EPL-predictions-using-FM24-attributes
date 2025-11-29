
import os

# transform.py

def run_sql_file(engine, sql_path):
    print(f"Running SQL script: {sql_path}")

    with open(sql_path, "r", encoding="utf-8") as f:
        sql = f.read()

    with engine.begin() as conn:
        conn.exec_driver_sql(sql)   # ← FIXED

    print(f"✔ Finished running {sql_path}")




def run_transform(engine):
    print("=== Transform step ===")

    sql_folder = "sql"

    # list all .sql files and sort 
    sql_files = sorted(
        f for f in os.listdir(sql_folder)
        if f.endswith(".sql")
    )

    
    for file in sql_files:
        path = os.path.join(sql_folder, file)
        run_sql_file(engine, path)

    print("✔ Transform finished")



if __name__ == "__main__":
    from run_pipeline import get_engine
    engine = get_engine()
    run_transform(engine)



