# Generated by Django 2.2.4 on 2020-09-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wishapp', '0003_auto_20200921_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_hash',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
