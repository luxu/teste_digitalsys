from django.db import models

class Loan(models.Model):
    name = models.CharField(
        'Nome',
        max_length=50,
    )
    cpf = models.CharField(
        'CPF',
        max_length=11,
    )
    address = models.CharField(
        'Endereço',
        max_length=50,
    )
    loan_amount = models.DecimalField(
        'Valor do Empréstimo',
        max_digits=9,
        decimal_places=2
    )
    proposal = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Empréstimo'
        verbose_name_plural='Empréstimos'
