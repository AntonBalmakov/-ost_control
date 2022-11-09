import datetime
from income.models import Income


class IncomeStatsGenerator:

    def __init__(self, user):
        self.user = user

    def get_amount_for_source(self, income_list, source):
        income = income_list.filter(source=source)
        amount = 0

        for i in income:
            amount += i.amount
        return {'amount': str(amount)}

    def get_source(self, income):
        return income.source

    def execute(self):
        todays_date = datetime.date.today()
        ayear_ago = todays_date - datetime.timedelta(days=30 * 12)
        income = Income.objects.filter(owner=self.user, date__gte=ayear_ago, date__lte=todays_date)
        final = {}
        sources = list(set(map(self.get_source, income)))

        for i in income:
            for source in sources:
                final[source] = self.get_amount_for_source(income, source)
        return final
