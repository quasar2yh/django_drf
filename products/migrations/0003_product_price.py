# Generated by Django 4.2 on 2024-05-02 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
