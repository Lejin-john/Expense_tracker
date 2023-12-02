from django.db import models

# Create your models here.

# expenses/models.py

from django.db import models
from django.contrib.auth.models import User

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        app_label = 'expenses'

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s {self.category.name} Expense - {self.amount}"

    class Meta:
        app_label = 'expenses'


'''
The Expense model has fields for user (linked to the built-in User model for authentication),
amount, description, category (linked to the ExpenseCategory model), and date.
The ExpenseCategory model has a simple name field.
'''

