from fastapi import FastAPI
import mysql.connector

app = FastAPI()

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nimi@191",
    database="chinook"
)

cursor = db.cursor(dictionary=True)

@app.get("/artists")
def get_artists():
    cursor.execute("SELECT * FROM Artist LIMIT 10")
    result = cursor.fetchall()
    return {"artists": result}