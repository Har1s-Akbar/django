# Generated by Django 4.2.1 on 2023-05-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]