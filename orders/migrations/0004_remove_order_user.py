# Generated by Django 4.1.7 on 2024-06-19 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]