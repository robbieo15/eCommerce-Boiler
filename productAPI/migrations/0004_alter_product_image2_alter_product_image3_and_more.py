# Generated by Django 4.1.1 on 2022-12-06 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAPI', '0003_alter_product_image2_alter_product_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
