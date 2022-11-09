import datetime
from user_authentication.utils import Util
from user_authentication.models import User
from django.template.loader import render_to_string
from datetime import datetime
from .services.expense_stats_generator import ExpenseStatsGenerator
from .services.income_stats_generator import IncomeStatsGenerator


def my_scheduled_job():
    users = User.objects.filter(is_active=True, is_staff=False)
    for user in users:
        service = ExpenseStatsGenerator(user=user)
        expense_final = service.execute()
        service = IncomeStatsGenerator(user=user)
        income_final = service.execute()
        message = render_to_string('send_message_template.html', {
            'user': user,
            'expense_category_data': expense_final,
            'income_source_data': income_final,
            'time': datetime.now().strftime('%d.%m.%Y в %H:%M:%S')
        })
        mail_subject = 'Ваша статистика'

        data = {'email_body': message, 'to_email': user.email, 'email_subject': mail_subject}
        Util.send_email(data)
