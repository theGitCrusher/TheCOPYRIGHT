# Generated by Django 5.1 on 2024-08-31 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcrapp', '0003_alter_product_created_at_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='product_image'),
        ),
    ]
