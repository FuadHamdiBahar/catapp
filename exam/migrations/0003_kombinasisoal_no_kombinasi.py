# Generated by Django 3.1.1 on 2021-04-25 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_kombinasisoal'),
    ]

    operations = [
        migrations.AddField(
            model_name='kombinasisoal',
            name='no_kombinasi',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
