# Generated by Django 4.2.9 on 2024-05-24 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_status_projectname_status_currentdate_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Tasks',
        ),
    ]
