# Generated by Django 4.1.7 on 2023-10-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_reservation', '0010_ticket_total_fare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
