# Generated by Django 4.2.9 on 2024-06-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_tasks_employee_remove_customers_user_customers_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='employee',
        ),
        migrations.AddField(
            model_name='tasks',
            name='employee',
            field=models.ManyToManyField(null=True, to='accounts.customers'),
        ),
    ]