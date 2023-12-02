from django.shortcuts import render

# Create your views here.

# expenses/views.py

from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})
'''
The render function takes the request, the template name, and a context dictionary as arguments.
The context dictionary is used to pass data from the view to the template.
The templates include dynamic content using template tags and variables,
making them flexible and capable of displaying data from the server.'''
