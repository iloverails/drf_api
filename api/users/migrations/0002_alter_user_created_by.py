# Generated by Django 4.1.2 on 2022-10-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_by',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
