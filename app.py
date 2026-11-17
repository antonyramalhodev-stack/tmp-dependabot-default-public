"""Tiny Flask app used as a baseline for a code scanning test."""
import sqlite3

from flask import Flask, jsonify

app = Flask(__name__)


def get_connection():
    return sqlite3.connect("app.db")


@app.route("/users/<int:user_id>")
def get_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return jsonify({"user": row})


if __name__ == "__main__":
    app.run()
