# Generated by Django 4.1 on 2022-09-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bayanApp', '0010_alter_product_arabic_name_alter_product_no_of_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='BARCODE',
            field=models.CharField(max_length=200, null=True, verbose_name='BARCODE'),
        ),
    ]