# Generated by Django 4.0.6 on 2022-07-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_ordermodel_city_ordermodel_email_ordermodel_is_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
    ]
