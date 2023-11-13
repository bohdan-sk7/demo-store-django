# Generated by Django 4.2.7 on 2023-11-13 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.productinventory'),
        ),
    ]
