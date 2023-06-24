from django.contrib import admin
from .models import Loan


class LoanAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'cpf',
        'address',
        'loan_amount'
    ]

admin.site.register(Loan, LoanAdmin)
