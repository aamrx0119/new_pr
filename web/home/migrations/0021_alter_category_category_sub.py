# Generated by Django 3.2.9 on 2022-01-06 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20220106_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='home.category'),
        ),
    ]
