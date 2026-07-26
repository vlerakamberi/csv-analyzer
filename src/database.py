import sqlite3


def get_connection(db_path="data/processed/titanic.db"):
    """Krijon (ose lidh me) bazën SQLite."""
    return sqlite3.connect(db_path)


def save_to_db(df, db_path="data/processed/titanic.db", table_name="passengers"):
    """Ruan DataFrame-in si tabelë në SQLite."""
    conn = get_connection(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"U ruajtën {len(df)} rreshta në tabelën '{table_name}' te {db_path}")


def query_db(query, db_path="data/processed/titanic.db"):
    """Ekzekuton një pyetje SQL dhe kthen rezultatin si DataFrame."""
    import pandas as pd
    conn = get_connection(db_path)
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result