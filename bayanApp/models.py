from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager
#from bayan.settings import BASE_DIR, STATICFILES_DIRS
from django.utils.safestring import mark_safe
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

#VERBOSE_NAME = _('accounts')
#verbose_name_plural = _('accounts')

class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class User(AbstractUser):
    objects = CustomUserManager()

    class Meta:
        db_table = "auth_user"
   
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    TITLE_CHOICES = ( (_('Admin'), _('Admin')), (_('Vendor'),_('Vendor')), (_('Sales'),_('Sales')), (_('Accounts'), _('Accounts')) )
    supply_choices = ((_('not vendor'),_('not vendor')), (_('vegetables'),_('vegetables')), (_('beautify'),_('beautify')), (_('Families supplies'),
        _('Families supplies')), (_('Markets and branches'),_('Markets and branches')))
#    supply_choices = (('ﺦﺿﺍﺭ ', 'ﺦﺿﺍﺭ '), ('ﺖﺠﻤﻴﻟ ', 'ﺖﺠﻤﻴﻟ '), ('ﻝﻭﺍﺰﻣ ﻉﺎﺋﻼﺗ', 'ﻝﻭﺍﺰﻣ ﻉﺎﺋﻼﺗ'), ('ﺎﺳﻭﺎﻗ ﻮﻓﺭﻮﻋ', 'ﺎﺳﻭﺎﻗ ﻮﻓﺭﻮﻋ'))
#    person_type             = models.CharField(max_length=200, default="Vendor", verbose_name=_('Person Type'))
    phone                   = PhoneNumberField(null=True, blank=False, unique=False, verbose_name=_('Phone'))
    VEND_DESC_ARABIC        = models.CharField(max_length=200, null=True, verbose_name=_('VEND_DESC_ARABIC'))
    VEND_CODE               = models.IntegerField(null=True, verbose_name=_('VEND_CODE'))
    profile_pic             = models.ImageField  (null=True, blank=True, verbose_name=_('Profile Picture'))

    sign_auth               = models.FileField   (null=True, blank=True, verbose_name=_('Sign Auth'))
    trade_book              = models.FileField   (null=True, blank=True, verbose_name=_('Trade Book'))
    chamber_book            = models.FileField   (null=True, blank=True, verbose_name=_('Chamber Book'))
    trademark               = models.FileField   (null=True, blank=True, verbose_name=_('Trade Mark'))
    import_license          = models.FileField   (null=True, blank=True, verbose_name=_('Import License'))
    healthy_preview         = models.FileField   (null=True, blank=True, verbose_name=_('Healthy Preview'))
    agency_book             = models.FileField   (null=True, blank=True, verbose_name=_('Agency Book'))
    varieties_revealed      = models.FileField   (null=True, blank=True, verbose_name=_('Varieties Revealed'))
    customs_declaration     = models.FileField   (null=True, blank=True, verbose_name=_('Customs Declaration'))
    industrial_facility     = models.FileField   (null=True, blank=True, verbose_name=_('Industrial Facility'))
    federation_of_associations= models.FileField (null=True, blank=True, verbose_name=_('Federation Of Associations'))
#    id =  models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')    
    person_type             = models.CharField(max_length=200, choices=TITLE_CHOICES, verbose_name=_('Person Type'))
    type_of_supply          = models.CharField(max_length=200, choices = supply_choices, verbose_name=_("Type of Supply"))
#    phone                   = models.CharField(max_length=200, null=True, verbose_name=_('Phone'))
#    VEND_CODE               = models.OneToOneField(Vendor.VEND_CODE, unique = True, verbose_name=_('VEND_CODE'))
    
class Vendor(models.Model):
    def __str__(self):
        return self.VEND_DESC_ARABIC
    user             = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name=_('User')) 
    VEND_CODE        = models.IntegerField (unique = True, verbose_name=_('VEND_CODE'))
    VEND_DESC_ARABIC = models.CharField    (null=True, max_length=200, verbose_name=_('VEND_DESC_ARABIC'))
    chique_image     = models.ImageField   (null=True, blank=True, verbose_name=_('Chique_Image'))
#    bill_data        = models.FileField    (null=True, blank=True, verbose_name=_('Bill_Data'))
    
    class Meta:
        verbose_name        = _('Vendor')
        verbose_name_plural = _('Vendors')


##class Bill(models.Model):
##    bill_data  = models.FileField (verbose_name=_('Bill_Image'), null=True, blank=True)
##    vendor     = models.ForeignKey (Vendor, on_delete=models.CASCADE, null=True) 

class Sales(models.Model):
    def __str__(self):
        return self.user

    user             = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name=_('User')) 
    sales_code        = models.IntegerField(unique = True, verbose_name=_('sales_code'))
    class Meta:
        verbose_name =        _('Sale')
        verbose_name_plural = _('Sales')

class Accounts(models.Model):
    def __str__(self):
        return self.user.username

    user             = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name=_('User')) 
#    user             = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name=_('User'))
    accounts_code    = models.IntegerField(unique = True, verbose_name=_('accounts_code'))
    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

class Product(models.Model):
    #vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    def __str__(self):
        return ( self.ARABIC_NAME)
    
    ID          = models.CharField(auto_created=True, max_length=8, blank=False, verbose_name=_('ID'))
    VEND_CODE   = models.IntegerField(null=True, verbose_name=_('VEND_CODE'))
    PACK_ID     = models.IntegerField(null=True, verbose_name=_('PACK_ID'))
    NO_OF_ITEMS = models.IntegerField(null=True, verbose_name=_('NO_OF_ITEMS'))
    ARABIC_NAME = models.CharField   (null=True, max_length=200, verbose_name=_('ARABIC_NAME'))
    UNIT_DESC   = models.CharField   (null=True, max_length=200, verbose_name=_('UNIT_DESC'))
    PURCH_PRICE = models.CharField   (null=True, max_length=200, verbose_name=_('PURCH_PRICE'))
    SALE_PRICE  = models.CharField   (null=True, max_length=200, verbose_name=_('SALE_PRICE'))
    BARCODE     = models.CharField   (null=True, max_length=200, verbose_name=_('BARCODE'))
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

#########################################################################################################
class Location(models.Model):
    def __str__(self):
        return(self.LOCN_NAME)
   
    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    LOCN_ID   = models.IntegerField(verbose_name=_('LOCN_ID'))
    LOCN_NAME = models.CharField(verbose_name=_('LOCN_NAME'), max_length=200)

########################################################################################################
class Order_MS_VCHR_XO(models.Model):
    class Meta:
        get_latest_by = 'order_no'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
    TITLE_CHOICES = ( (_('Opened'),_('Opened')) , (_('Closed'),_('Closed')))

    order_no        = models.BigIntegerField(verbose_name=_('Order_No'), unique=True)
    order_date      = models.DateField      (verbose_name=_('Order_Date'),)
    order_state     = models.CharField      (verbose_name=_('Order_State'), max_length=200, choices=TITLE_CHOICES)
    order_image     = models.ImageField     (verbose_name=_('Order_Image'), null=True, blank=True)
    VEND_CODE       = models.IntegerField   (verbose_name=_('VEND_CODE'), null=True)
    VEND_DESC_ARABIC= models.CharField      (verbose_name=_('VEND_DESC_ARABIC'), max_length=200)
    vendor          = models.ForeignKey     (Vendor, on_delete=models.CASCADE, null=True)
    location        = models.CharField      (verbose_name=_('Location'), max_length=200, blank=False) 
    notes           = models.CharField      (verbose_name=_('Notes'), max_length=1000, blank=True)
    table_data      = models.CharField      (verbose_name=_('table_data'), max_length=1000, blank=False)
    image_data      = models.ImageField     (verbose_name=_('Order_data_Image'), null=True, blank=True)

    def __str__(self):
        return(self.order_no)

    def image_tag(self):
        if self.order_image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.order_image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = _('Image')

    def validate_nonzero(value):
        if value < 0:
            raise ValidationError(
            _('Quantity %(value)s is not allowed'),
            params={'value': value},
            )
    quantity        = models.PositiveIntegerField(verbose_name=_('quantity'), null=True, validators=[validate_nonzero])

class ConfirmedOrders(models.Model):    
    class Meta:
        db_table = "accounts_confirmed_orders"

    vendor          = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    order_image     = models.ImageField(null=True, blank=True)
    order_no        = models.IntegerField(unique=True)

class Transaction(models.Model):
    class Meta:
        verbose_name        = _('Transaction')
        verbose_name_plural = _('Transactions')

    state_choices= [(_('read'), _('read')),(_('unread'),_('unread'))]
    type_choices = [(_('new order'),_('new order')), (_('confirm order'), _('confirm order')), (_('update products'), _('update products')), (_('upload chique'), _('upload chique'))]

    t_no        = models.BigIntegerField(verbose_name=_('T_No'), unique=True)
    t_date      = models.DateField      (verbose_name=_('T_Date') )
    t_type      = models.CharField      (verbose_name=_('T_Type'), max_length=20, choices=type_choices)
    t_state     = models.CharField      (verbose_name=_('T_State'), max_length=10, choices=state_choices)
    t_details   = models.CharField      (verbose_name=_('T_Details'), max_length=500)
    VEND_CODE   = models.IntegerField   (verbose_name=_('VEND_CODE'))
    parameter   = models.CharField      (verbose_name=_('Parameter'), max_length=50)

    def __str__(self):
        return(self.t_type)

class Bill(models.Model):
    class Meta:
        verbose_name        = _('Bill')
        verbose_name_plural = _('Bills')

    b_date      = models.DateField      (verbose_name=_('B_Date') )
    b_details   = models.CharField      (verbose_name=_('B_Details'), max_length=500)
    VEND_CODE   = models.IntegerField   (verbose_name=_('VEND_CODE'))
    vendor      = models.ForeignKey     (Vendor, on_delete=models.CASCADE, null=True)
    bill_file   = models.FileField    (null=True, blank=True, verbose_name=_('Bill_File'))

    def __str__(self):
        return(self.id)

class Chique(models.Model):
    class Meta:
        verbose_name        = _('Chique')
        verbose_name_plural = _('Chiques')

    c_date      = models.DateField      (verbose_name=_('C_Date') )
    chique_image= models.ImageField     (verbose_name=_('Chique_Image'), null=True, blank=True)
    vendor      = models.ForeignKey     (Vendor, on_delete=models.CASCADE, null=True) 
    VEND_CODE   = models.IntegerField   (verbose_name=_('VEND_CODE'))

