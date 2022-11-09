from django.db import models
from user_authentication.models import User


class Expense(models.Model):

    CATEGORY_OPTIONS = [
        ('SELF-CARE', 'SELF-CARE'),
        ('HEALTH-AND-FITNESS', 'HEALTH-AND-FITNESS'),
        ('CAFES-AND-RESTAURANTS', 'CAFES-AND-RESTAURANTS'),
        ('CAR', 'CAR'),
        ('EDUCATION', 'EDUCATION'),
        ('LEISURE-AND-ENTERTAINMENT', 'LEISURE-AND-ENTERTAINMENT'),
        ('PAYMENTS-COMMISSIONS', 'PAYMENTS-COMMISSIONS'),
        ('SHOPPING', 'SHOPPING'),
    ]
    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)

    class Meta:
        ordering: ['-date']

    def __str__(self):
        return str(self.owner)+'s income'
