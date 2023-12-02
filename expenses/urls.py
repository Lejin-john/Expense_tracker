# expenses/urls.py

from django.urls import path
from .views import expense_list, add_expense

urlpatterns = [
    path('expenses/', expense_list, name='expense_list'),
    path('add_expense/', add_expense, name='add_expense'),
    # Add more URL patterns as needed for different views
]
