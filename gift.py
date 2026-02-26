# server.py structure

class ChatServer:
    def __init__(self):
        self.clients = {}
        self.database = DatabaseManager()
        
    def authenticate_user(self, username, password):
        pass
        
    def handle_private_message(self, sender, receiver, message):
        pass
        
    def store_message(self, sender, receiver, message):
        pass
        
    def broadcast_online_users(self):
        pass
import sqlite3

conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    sender TEXT,
    receiver TEXT,
    message TEXT
)
""")

conn.commit()
conn.close()
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

