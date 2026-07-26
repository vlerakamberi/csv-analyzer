import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)

from validate import validate_data
from database import save_to_db, query_db
import pandas as pd


def load_data(filepath):
    df = pd.read_csv(filepath)
    logger.info(f"U lexuan {len(df)} rreshta nga {filepath}")
    return df


def clean_data(df):
    median_age = df["Age"].median()
    df["Age"] = df["Age"].fillna(median_age)
    logger.info(f"Mosha u mbush me: {median_age}")

    df = df.drop(columns=["Cabin"])
    logger.info("Kolona Cabin u hoq")

    rreshta_para = len(df)
    df = df.dropna(subset=["Embarked"])
    rreshta_pas = len(df)
    logger.info(f"U hoqën {rreshta_para - rreshta_pas} rreshta pa Embarked")

    return df


def analyze(df):
    print()
    print("=== Norma e mbijetesës sipas gjinisë ===")
    print(df.groupby("Sex")["Survived"].mean())

    print()
    print("=== Norma e mbijetesës sipas klasës ===")
    print(df.groupby("Pclass")["Survived"].mean())


def main():
    df = load_data("data/raw/titanic.csv")
    df = clean_data(df)
    df = validate_data(df) 
    analyze(df)

    save_to_db(df)
    print()
    print("=== Pyetje SQL: mosha mesatare sipas klasës ===")
    result = query_db("""
        SELECT Pclass, AVG(Age) as avg_age, COUNT(*) as total
        FROM passengers
        GROUP BY Pclass
    """)
    print(result)


if __name__ == "__main__":
    main()