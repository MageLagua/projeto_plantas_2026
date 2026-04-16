import csv
import os
import sqlite3

from fastapi import FastAPI

app = FastAPI()

DIRETORIO_DADOS = "/dados"
DB_PATH = f"{DIRETORIO_DADOS}/flowers.db"
CSV_PATH = "/code/flowers.csv"

os.makedirs(DIRETORIO_DADOS, exist_ok=True)


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS flowers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            cut_flowers INTEGER,
            perfumes INTEGER,
            medicine INTEGER,
            poison_to_cats TEXT,
            poison_to_dogs TEXT,
            scientific_name TEXT
        )
    """
    )
    cursor.execute("SELECT COUNT(*) FROM flowers")
    if cursor.fetchone()[0] == 0:
        with open(CSV_PATH, encoding="utf-8-sig") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                cursor.execute(
                    "INSERT INTO flowers (name, cut_flowers, perfumes, medicine, poison_to_cats, poison_to_dogs, scientific_name) VALUES (?,?,?,?,?,?,?)",
                    (
                        row["name"],
                        int(row["cut flowers"]),
                        int(row["perfumes"]),
                        int(row["medicine"]),
                        row["poison to cats"],
                        row["poison to dogs"],
                        row["scientific name"],
                    ),
                )
    conn.commit()
    conn.close()


init_db()


@app.get("/flowers")
def flowers():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM flowers").fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.get("/flowers/{scientific_name}")
def buscar_flor(scientific_name: str):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        "SELECT * FROM flowers WHERE scientific_name LIKE ? LIMIT 1",
        (f"{scientific_name}%",),
    ).fetchone()
    conn.close()
    if row is None:
        return {"erro": "Flor não encontrada"}
    return dict(row)
