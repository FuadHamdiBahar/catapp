# Generated by Django 3.1.1 on 2021-04-25 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_kombinasisoal_no_kombinasi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kombinasisoal',
            name='no_kombinasi',
        ),
    ]