# Generated by Django 3.2.8 on 2021-10-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
