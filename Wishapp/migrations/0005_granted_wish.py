# Generated by Django 2.2.4 on 2020-09-21 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Wishapp', '0004_auto_20200921_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Granted_wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('granted_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='granted_wishes', to='Wishapp.User')),
            ],
        ),
    ]
