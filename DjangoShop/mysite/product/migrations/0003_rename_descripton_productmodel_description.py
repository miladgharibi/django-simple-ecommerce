# Generated by Django 3.2.8 on 2021-10-12 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_productmodel_discount_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='descripton',
            new_name='description',
        ),
    ]
