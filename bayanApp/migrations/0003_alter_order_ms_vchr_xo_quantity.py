# Generated by Django 4.1 on 2022-09-04 21:44

import bayanApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bayanApp', '0002_user_vend_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_ms_vchr_xo',
            name='quantity',
            field=models.PositiveIntegerField(null=True, validators=[bayanApp.models.Order_MS_VCHR_XO.validate_nonzero], verbose_name='quantity'),
        ),
    ]