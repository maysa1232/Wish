# Generated by Django 2.2.4 on 2020-09-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wishapp', '0005_granted_wish'),
    ]

    operations = [
        migrations.AddField(
            model_name='granted_wish',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]