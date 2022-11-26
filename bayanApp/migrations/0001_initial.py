# Generated by Django 4.1.2 on 2022-11-22 07:43

import bayanApp.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Phone')),
                ('VEND_DESC_ARABIC', models.CharField(max_length=200, null=True, verbose_name='VEND_DESC_ARABIC')),
                ('VEND_CODE', models.IntegerField(null=True, verbose_name='VEND_CODE')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Profile Picture')),
                ('sign_auth', models.FileField(blank=True, null=True, upload_to='', verbose_name='Sign Auth')),
                ('trade_book', models.FileField(blank=True, null=True, upload_to='', verbose_name='Trade Book')),
                ('chamber_book', models.FileField(blank=True, null=True, upload_to='', verbose_name='Chamber Book')),
                ('trademark', models.FileField(blank=True, null=True, upload_to='', verbose_name='Trade Mark')),
                ('import_license', models.FileField(blank=True, null=True, upload_to='', verbose_name='Import License')),
                ('healthy_preview', models.FileField(blank=True, null=True, upload_to='', verbose_name='Healthy Preview')),
                ('agency_book', models.FileField(blank=True, null=True, upload_to='', verbose_name='Agency Book')),
                ('varieties_revealed', models.FileField(blank=True, null=True, upload_to='', verbose_name='Varieties Revealed')),
                ('customs_declaration', models.FileField(blank=True, null=True, upload_to='', verbose_name='Customs Declaration')),
                ('industrial_facility', models.FileField(blank=True, null=True, upload_to='', verbose_name='Industrial Facility')),
                ('federation_of_associations', models.FileField(blank=True, null=True, upload_to='', verbose_name='Federation Of Associations')),
                ('person_type', models.CharField(choices=[('Admin', 'Admin'), ('Vendor', 'Vendor'), ('Sales', 'Sales'), ('Accounts', 'Accounts')], max_length=200, verbose_name='Person Type')),
                ('type_of_supply', models.CharField(choices=[('not vendor', 'not vendor'), ('vegetables', 'vegetables'), ('beautify', 'beautify'), ('Families supplies', 'Families supplies'), ('Markets and branches', 'Markets and branches')], max_length=200, verbose_name='Type of Supply')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', bayanApp.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOCN_ID', models.IntegerField(verbose_name='LOCN_ID')),
                ('LOCN_NAME', models.CharField(max_length=200, verbose_name='LOCN_NAME')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VEND_CODE', models.IntegerField(null=True, verbose_name='VEND_CODE')),
                ('PACK_ID', models.IntegerField(null=True, verbose_name='PACK_ID')),
                ('NO_OF_ITEMS', models.IntegerField(null=True, verbose_name='NO_OF_ITEMS')),
                ('ARABIC_NAME', models.CharField(max_length=200, null=True, verbose_name='ARABIC_NAME')),
                ('UNIT_DESC', models.CharField(max_length=200, null=True, verbose_name='UNIT_DESC')),
                ('PURCH_PRICE', models.CharField(max_length=200, null=True, verbose_name='PURCH_PRICE')),
                ('SALE_PRICE', models.CharField(max_length=200, null=True, verbose_name='SALE_PRICE')),
                ('BARCODE', models.CharField(max_length=200, null=True, verbose_name='BARCODE')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_no', models.BigIntegerField(unique=True, verbose_name='T_No')),
                ('t_date', models.DateField(verbose_name='T_Date')),
                ('t_type', models.CharField(choices=[('new order', 'new order'), ('confirm order', 'confirm order'), ('update products', 'update products'), ('upload chique', 'upload chique')], max_length=20, verbose_name='T_Type')),
                ('t_state', models.CharField(choices=[('read', 'read'), ('unread', 'unread')], max_length=10, verbose_name='T_State')),
                ('t_details', models.CharField(max_length=500, verbose_name='T_Details')),
                ('VEND_CODE', models.IntegerField(verbose_name='VEND_CODE')),
                ('parameter', models.CharField(max_length=50, verbose_name='Parameter')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VEND_CODE', models.IntegerField(unique=True, verbose_name='VEND_CODE')),
                ('VEND_DESC_ARABIC', models.CharField(max_length=200, null=True, verbose_name='VEND_DESC_ARABIC')),
                ('chique_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Chique_Image')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Vendor',
                'verbose_name_plural': 'Vendors',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_code', models.IntegerField(unique=True, verbose_name='sales_code')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
            },
        ),
        migrations.CreateModel(
            name='Order_MS_VCHR_XO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.BigIntegerField(unique=True, verbose_name='Order_No')),
                ('order_date', models.DateField(verbose_name='Order_Date')),
                ('order_state', models.CharField(choices=[('Opened', 'Opened'), ('Closed', 'Closed')], max_length=200, verbose_name='Order_State')),
                ('order_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Order_Image')),
                ('VEND_CODE', models.IntegerField(null=True, verbose_name='VEND_CODE')),
                ('VEND_DESC_ARABIC', models.CharField(max_length=200, verbose_name='VEND_DESC_ARABIC')),
                ('location', models.CharField(max_length=200, verbose_name='Location')),
                ('notes', models.CharField(blank=True, max_length=1000, verbose_name='Notes')),
                ('table_data', models.CharField(max_length=1000, verbose_name='table_data')),
                ('image_data', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Order_data_Image')),
                ('quantity', models.PositiveIntegerField(null=True, validators=[bayanApp.models.Order_MS_VCHR_XO.validate_nonzero], verbose_name='quantity')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bayanApp.vendor')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'get_latest_by': 'order_no',
            },
        ),
        migrations.CreateModel(
            name='ConfirmedOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('order_no', models.IntegerField(unique=True)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bayanApp.vendor')),
            ],
            options={
                'db_table': 'accounts_confirmed_orders',
            },
        ),
        migrations.CreateModel(
            name='Chique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_date', models.DateField(verbose_name='C_Date')),
                ('chique_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Chique_Image')),
                ('VEND_CODE', models.IntegerField(verbose_name='VEND_CODE')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bayanApp.vendor')),
            ],
            options={
                'verbose_name': 'Chique',
                'verbose_name_plural': 'Chiques',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_date', models.DateField(verbose_name='B_Date')),
                ('b_details', models.CharField(max_length=500, verbose_name='B_Details')),
                ('VEND_CODE', models.IntegerField(verbose_name='VEND_CODE')),
                ('bill_file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Bill_File')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bayanApp.vendor')),
            ],
            options={
                'verbose_name': 'Bill',
                'verbose_name_plural': 'Bills',
            },
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accounts_code', models.IntegerField(unique=True, verbose_name='accounts_code')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
