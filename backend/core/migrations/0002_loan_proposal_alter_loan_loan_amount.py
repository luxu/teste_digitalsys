# Generated by Django 4.2.2 on 2023-06-24 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='proposal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_amount',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor do Empréstimo'),
        ),
    ]