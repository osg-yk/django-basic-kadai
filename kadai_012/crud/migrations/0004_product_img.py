# Generated by Django 5.1.6 on 2025-02-24 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='noImase.png', upload_to=''),
        ),
    ]
