# Generated by Django 2.1 on 2019-06-11 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalyear', '0003_annualpayment_deductions'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualpayment',
            name='annual_fee',
            field=models.DecimalField(decimal_places=2, default=500000, max_digits=10),
            preserve_default=False,
        ),
    ]
