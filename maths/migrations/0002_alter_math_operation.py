# Generated by Django 3.2.7 on 2021-09-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='math',
            name='operation',
            field=models.CharField(max_length=6),
        ),
    ]
