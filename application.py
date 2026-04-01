from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import csv, os

application = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI", "")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    db = client["survey_db"]
    collection = db["users"]
    print("MongoDB connected successfully!")
except Exception as e:
    print(f"MongoDB connection error: {e}")
    client = None
    collection = None

class User:
    def __init__(self, age, gender, income, expenses):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/submit", methods=["POST"])
def submit():
    try:
        age = request.form.get("age")
        gender = request.form.get("gender")
        income = request.form.get("income")
        expenses = {
            "utilities": request.form.get("utilities", 0),
            "entertainment": request.form.get("entertainment", 0),
            "school_fees": request.form.get("school_fees", 0),
            "shopping": request.form.get("shopping", 0),
            "healthcare": request.form.get("healthcare", 0),
        }
        user = User(age, gender, income, expenses)

        if collection is not None:
            collection.insert_one({
                "age": user.age,
                "gender": user.gender,
                "income": user.income,
                "expenses": user.expenses,
            })
            return redirect("/")
        else:
            return f"Database connection error. MONGO_URI set: {bool(MONGO_URI)}", 500

    except Exception as e:
        return f"Error: {str(e)}", 500

@application.route("/export")
def export():
    if collection is None:
        return "Database not connected", 500
    users = list(collection.find())
    os.makedirs("data", exist_ok=True)
    with open("data/users.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Age","Gender","Income","Utilities","Entertainment","School Fees","Shopping","Healthcare"])
        for u in users:
            writer.writerow([
                u["age"], u["gender"], u["income"],
                u["expenses"].get("utilities", 0),
                u["expenses"].get("entertainment", 0),
                u["expenses"].get("school_fees", 0),
                u["expenses"].get("shopping", 0),
                u["expenses"].get("healthcare", 0),
            ])
    return "CSV Exported Successfully!"

@application.route("/debug")
def debug():
    return f"MONGO_URI set: {bool(MONGO_URI)}, URI starts with: {MONGO_URI[:20] if MONGO_URI else 'NOT SET'}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host="0.0.0.0", port=port)
