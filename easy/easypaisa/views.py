from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Income, Expenses, Budget
from django.db.models import Q
from .forms import ExpensesForm, IncomeForm

def home(request):
    all_income = Income.objects.all()
    all_expenses = Expenses.objects.all()
    pre_income = 0
    for income in all_income:   # show total income on home page
        pre_income = pre_income + int(income.income)
    pre_expenses = 0
    for enpense in all_expenses:
        pre_expenses = pre_expenses + int(enpense.price)
    return render(request, 'home.html', {'pre_income': pre_income, 'pre_expenses': pre_expenses})


def addincome(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = IncomeForm()
        else:
            income = Income.objects.filter(id=id)
            form = IncomeForm(instance=income)
        return render(request, 'add income.html', {'form': form})
    else:
        if id == 0:
            form = IncomeForm(request.POST)
        else:
            income = Income.objects.get(id=id)
            form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
        return redirect('home')


def addexpenses(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = ExpensesForm()
        else:
            expenses = Expenses.objects.get(id=id)
            form = ExpensesForm(instance=expenses)
        return render(request, 'add expenses.html', {'form': form})
    else:
        if id == 0:
            form = ExpensesForm(request.POST)
        else:
            expenses = Expenses.objects.get(id=id)
            form = ExpensesForm(request.POST, instance=expenses)
        if form.is_valid():
            form.save()
        return redirect('home')


def AllIncome(request):
    all_income = Income.objects.all().order_by('date_added')
    pre_income = 0
    for income in all_income:
        pre_income = pre_income + int(income.income)
    return render(request, 'List income.html', {'all_income': all_income, 'income': pre_income})


def Deleteincome(request, id):
    delete_income = Income.objects.get(id=id)
    delete_income.delete()
    return redirect('list-income')


def AllExpenses(request):
    all_expenses = Expenses.objects.all().order_by('date_added')
    pre_expenses = 0
    for enpense in all_expenses:
        pre_expenses = pre_expenses + int(enpense.price)
    return render(request, 'list expenses.html', {'all_expenses': all_expenses, 'expenses': pre_expenses})


def Deleteexpenses(request, id):
    delete_expenses = Expenses.objects.get(id=id)
    delete_expenses.delete()
    return redirect('list-expenses')


def SetBudget(request):
    if request.method == 'POST':
        data = Budget()
        data.budget = request.POST.get('budget')
        data.save()
        return redirect('home')
    else:
        return render(request, 'budget.html')


def search(request):
    query = request.GET.get('q')
    results = Expenses.objects.filter(Q(category__icontains=query) | Q(remark__icontains=query))
    no_of_results = Expenses.objects.filter(Q(category__icontains=query) | Q(remark__icontains=query)).count()
    context = {'results': results, 'count': no_of_results}
    return render(request, 'search list.html', context)
