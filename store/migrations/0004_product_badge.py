# Generated by Django 4.2.7 on 2023-11-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='badge',
            field=models.CharField(default='', max_length=15),
        ),
    ]
