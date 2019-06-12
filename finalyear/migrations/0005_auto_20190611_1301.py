# Generated by Django 2.1 on 2019-06-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalyear', '0004_annualpayment_annual_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annualpayment',
            old_name='annual_fee',
            new_name='net_pay',
        ),
        migrations.AlterField(
            model_name='annualpayment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='annualpayment',
            name='kilos',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
