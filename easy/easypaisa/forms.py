from django import forms
from .models import Expenses, Income, Budget

class ExpensesForm(forms.ModelForm):

    class Meta:
        model = Expenses
        fields = '__all__'
        labels = {
            'date_added': 'Date'
        }

    def __init__(self, *args, **kwargs):
        super(ExpensesForm, self).__init__(*args, **kwargs)
        self.fields['date_added'].required = False


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ('income', 'remark', 'date_added')  #(income, remark, date_added)
