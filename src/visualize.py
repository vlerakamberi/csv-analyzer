import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

conn = sqlite3.connect("data/processed/titanic.db")

query = "SELECT Pclass, Survived FROM passengers"
df = pd.read_sql_query(query, conn)

conn.close()

survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100
print(survival_by_class)


survival_by_class.plot(kind="bar", color="steelblue")

plt.title("Norma e Mbijetesës sipas Klasës (Titanic)")
plt.xlabel("Klasa")
plt.ylabel("Norma e Mbijetesës (%)")
plt.xticks(rotation=0)

plt.savefig("data/processed/survival_by_class.png")
plt.show()