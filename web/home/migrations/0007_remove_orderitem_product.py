# Generated by Django 3.2.9 on 2021-12-12 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
    ]