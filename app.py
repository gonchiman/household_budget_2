from datetime import date
from flask import Flask, render_template, request, redirect

from src.transaction import TransactionType
from src.transaction_repository import TransactionRepository
from src.transaction_service import TransactionService


app = Flask(__name__)

repository = TransactionRepository()
service = TransactionService(repository)


@app.route("/")
def index():
    return render_template(
        "index.html",
        transactions=service.get_all_transactions()
    )


@app.route("/add", methods=["POST"])
def add():
    service.add_transaction(
        date.fromisoformat(request.form["transaction_date"]),
        int(request.form["amount"]),
        TransactionType(request.form["transaction_type"]),
        request.form["memo"],
    )
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)