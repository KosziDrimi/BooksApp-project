# Generated by Django 3.2.5 on 2021-07-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210729_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='numer_isbn',
            field=models.BigIntegerField(help_text='numer powinien składać się z 10 lub 13 cyfr'),
        ),
    ]
