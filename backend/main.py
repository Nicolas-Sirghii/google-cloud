from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/greeting")
def greeting():

    db = mysql.connector.connect(
        host="mysql-container",
        user="root",
        password="password",
        database="testdb"
    )

    cursor = db.cursor()

    cursor.execute("SELECT 'Hello from MySQL'")
    result = cursor.fetchone()

    return {"message": result[0]}
