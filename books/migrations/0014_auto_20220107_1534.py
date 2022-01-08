# Generated by Django 3.2.6 on 2022-01-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20220103_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='autor',
        ),
        migrations.AddField(
            model_name='autor',
            name='books',
            field=models.ManyToManyField(to='books.Book'),
        ),
    ]
