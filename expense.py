# --- expense.py ---
import uuid
from datetime import datetime

class Expense:
    def __init__(self, id, amount, category, date):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            id=data["id"],
            amount=float(data["amount"]),
            category=data["category"],
            date=data["date"]
        )

    @staticmethod
    def create(amount, category):
        return Expense(
            id=str(uuid.uuid4())[:8],
            amount=amount,
            category=category,
            date=datetime.now().strftime("%Y-%m-%d")
        )
