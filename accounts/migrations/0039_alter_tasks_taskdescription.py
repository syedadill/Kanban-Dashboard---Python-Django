# Generated by Django 4.2.9 on 2024-06-11 11:39

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='TaskDescription',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
