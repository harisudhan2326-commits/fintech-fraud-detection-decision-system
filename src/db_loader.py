import sqlite3
conn = sqlite3.connect('data/fraud.db')
cursor = conn.cursor()

print("connected")
