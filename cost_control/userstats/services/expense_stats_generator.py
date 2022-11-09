import datetime
from cost_app.models import Expense


class ExpenseStatsGenerator:
    def __init__(self, user):
        self.user = user

    def get_amount_for_category(self, expense_list, category):
        expenses = expense_list.filter(category=category)
        amount = 0

        for expense in expenses:
            amount += expense.amount
        return {'amount': str(amount)}

    def get_category(self, expense):
        return expense.category

    def execute(self):
        todays_date = datetime.date.today()
        ayear_ago = todays_date - datetime.timedelta(days=30 * 12)
        expenses = Expense.objects.filter(owner=self.user, date__gte=ayear_ago, date__lte=todays_date)
        final = {}
        categories = list(set(map(self.get_category, expenses)))

        for expense in expenses:
            for category in categories:
                final[category] = self.get_amount_for_category(expenses, category)
        return final
