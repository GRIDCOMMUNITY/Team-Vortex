"""Expense Splitter - Hack Day Haldia x GRID community starter. Build the core tasks from README.md."""
import os
import sqlite3

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder=None)
DB_PATH = os.path.join(app.root_path, "data.db")


def db():
    """SQLite connection whose rows behave like dicts. Use:  with db() as conn: ..."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with db() as conn:
        conn.executescript("""
            -- TODO: create your tables here, for example:
            -- CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
        """)


init_db()


@app.get("/")
def home():
    return send_from_directory(app.root_path, "index.html")


@app.get("/api/health")
def health():
    return jsonify(ok=True)


# ---- TODO(core): fill these in ------------------------------------------
@app.route("/api/members", methods=['GET', 'POST'])
def ep1_api_members(**kwargs):
    # TODO(core): list / add members
    return jsonify(error="not implemented"), 501


@app.route("/api/expenses", methods=['GET', 'POST'])
def ep2_api_expenses(**kwargs):
    # TODO(core): list / add expenses
    return jsonify(error="not implemented"), 501


@app.route("/api/expenses/<int:eid>", methods=['PUT', 'DELETE'])
def ep3_api_expenses_int_eid(**kwargs):
    # TODO(core): edit / delete an expense
    return jsonify(error="not implemented"), 501


@app.route("/api/balances", methods=['GET'])
def ep4_api_balances(**kwargs):
    # TODO(core): net balance per member
    return jsonify(error="not implemented"), 501


@app.route("/api/settle", methods=['GET'])
def ep5_api_settle(**kwargs):
    # TODO(core): minimum settle-up payments
    return jsonify(error="not implemented"), 501


@app.route("/api/settlements/<int:sid>/paid", methods=['POST'])
def ep6_api_settlements_int_sid_paid(**kwargs):
    # TODO(core): mark a settlement paid
    return jsonify(error="not implemented"), 501



if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
