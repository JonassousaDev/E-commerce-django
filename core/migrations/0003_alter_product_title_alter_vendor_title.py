# Generated by Django 4.2.5 on 2023-09-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='Product title', max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='title',
            field=models.CharField(default='Vendor', max_length=100),
        ),
    ]
