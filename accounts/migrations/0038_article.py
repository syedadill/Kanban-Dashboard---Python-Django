# Generated by Django 4.2.9 on 2024-06-11 11:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0037_projects_assign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('datePosted', models.CharField(default='', max_length=20)),
                ('timePosted', models.CharField(default='', max_length=20)),
                ('category', models.CharField(max_length=300)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('contentImage', models.ImageField(upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
