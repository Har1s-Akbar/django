# Generated by Django 4.2.1 on 2023-05-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.TextField(max_length=25),
        ),
    ]
