# Generated by Django 5.1.6 on 2025-02-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_alter_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
