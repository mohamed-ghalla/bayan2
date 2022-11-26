from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import ModelForm, TextInput
from django import forms
from .models import * #User, Order_MS_VCHR_XO, ConfirmedOrders, Product, Vendor, ChiqueImage, Location
from datetime import datetime
from phone_field import PhoneField
from django.utils.translation import gettext_lazy as _
from .validators import validate_billFile_type, validate_image_type, validate_file_type, validate_products_file_type
class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        field = ['username', 'password']

    old_password    = forms.CharField   (required=True, max_length=32, widget=forms.PasswordInput, label =_('old_password'))
    new_password1   = forms.CharField   (required=True, max_length=32, widget=forms.PasswordInput, label =_('new_password1'))
    new_password2   = forms.CharField   (required=True, max_length=32, widget=forms.PasswordInput, label =_('new_password2'))

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
#        widgets = {
#                'password': forms.PasswordInput,
#                }
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone', 'VEND_DESC_ARABIC', 'person_type', 'type_of_supply', 
                'sign_auth', 'trade_book', 'chamber_book', 'trademark', 'import_license', 'healthy_preview', 
                'agency_book', 'varieties_revealed', 'customs_declaration', 'industrial_facility', 'federation_of_associations']

    person_choices = ( (_('Admin'),_('Admin')), (_('Vendor'),_('Vendor')) , (_('Sales'),_('Sales')), (_('Accounts'), _('Accounts' )))
    supply_choices = ((_('not vendor'),_('not vendor')), (_('vegetables'),_('vegetables')), (_('beautify'),_('beautify')), (_('Families supplies'),_('Families supplies')),
        (_('Markets and branches'),_('Markets and branches')))
#    supply_choices = (('خضار', 'خضار'), ('تجميل ', 'تجميل'), ('لوازم عائلات', 'لوازم عائلات'), ('اسواق وفروع', 'اسواق وفروع'))

    first_name       = forms.CharField   (required=True, max_length=20, label=_("First Name"))
    last_name        = forms.CharField   (required=True, max_length=20, label=_("Last Name"))
    username         = forms.CharField   (required=True, max_length=20, label=_("Username"))
    email            = forms.EmailField  (required=True, label=_("Email"))
    password1 = forms.CharField(required=False, widget=forms.PasswordInput())
    password2 = forms.CharField(required=False, widget=forms.PasswordInput())
#    phone            = forms.CharField   (required=True, label=_("Phone")) 
    phone     = forms.CharField   (required=True, label=_("Phone"))
    VEND_DESC_ARABIC = forms.CharField   (required=True, label=_("The trade name of the company"))
    type_of_supply   = forms.ChoiceField (required=False, initial=_('not vendor'), widget=forms.Select, choices = supply_choices, label=_("Type of Supply"))
    person_type      = forms.ChoiceField (required=True, initial=_('Vendor'), widget=forms.Select, choices = person_choices, label=_("Person Type")) 
#    person_type      = forms.ChoiceField (required=True, widget=forms.Select, choices = person_choices, label=_("Person Type"), initial=_('Vendor'))
    password1        = forms.CharField   (required=True, max_length=32, widget=forms.PasswordInput, label=_('password1'))
    password2        = forms.CharField   (required=True, max_length=32, widget=forms.PasswordInput, label=_('passowrd2'))

    sign_auth        = forms.FileField   (required=False, validators=[validate_file_type], label=_('Sign Auth'))
    trade_book       = forms.FileField   (required=False, validators=[validate_file_type], label=_('Trade Book'))
    chamber_book     = forms.FileField   (required=False, validators=[validate_file_type], label=_('Chamber Book'))
    trademark        = forms.FileField   (required=False, validators=[validate_file_type], label=_('Trade Mark'))
    import_license   = forms.FileField   (required=False, validators=[validate_file_type], label=_('Import License'))
    healthy_preview  = forms.FileField   (required=False, validators=[validate_file_type], label=_('Healthy Preview'))
    agency_book      = forms.FileField   (required=False, validators=[validate_file_type], label=_('Agency Book'))
    varieties_revealed= forms.FileField  (required=False, validators=[validate_file_type], label=_('Varieties Revealed'))
    customs_declaration = forms.FileField (required=False, validators=[validate_file_type], label=_('Customs Declaration'))
    industrial_facility = forms.FileField (required=False, validators=[validate_file_type], label=_('Industrial Facility'))    
    federation_of_associations= forms.FileField(required=False, validators=[validate_file_type], label=_('Federation Of Associations'))

    person_type.widget.attrs['readonly'] = True

class CustomerForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'email', 'profile_pic',  'VEND_DESC_ARABIC', #'person_type'
                 'type_of_supply', 
                'sign_auth', 'trade_book',
                'chamber_book', 'trademark', 'import_license', 'healthy_preview', 'agency_book', 'varieties_revealed', 
                'customs_declaration', 'industrial_facility', 'federation_of_associations']

    person_choices = ( (_('Admin'),_('Admin')), (_('Vendor'),_('Vendor')) , (_('Sales'),_('Sales')), (_('Accounts'), _('Accounts' )))
    supply_choices = ((_('vegetables'),_('vegetables')), (_('beautify'),_('beautify')), (_('Families supplies'),_('Families supplies')),
        (_('Markets and branches'),_('Markets and branches')))

    first_name          = forms.CharField   (required=True, max_length=20, label=_("First Name"))
    last_name           = forms.CharField   (required=True, max_length=20, label=_("Last Name"))
    username            = forms.CharField   (required=True, max_length=20, label=_("Username"))
    email               = forms.EmailField  (required=True, label=_("Email"))
    phone               = forms.CharField   (required=True, label=_("Phone")) 
    profile_pic         = forms.ImageField(required=False, validators=[validate_image_type], label=_('Profile Picture'))

    VEND_DESC_ARABIC = forms.CharField   (required=False, label=_("The trade name of the company"))
    type_of_supply   = forms.ChoiceField (required=False, widget=forms.Select, choices = supply_choices, label=_("Type of Supply"))
#    person_type      = forms.ChoiceField (required=False, initial=_('Vendor'), widget=forms.Select, choices = person_choices, label=_("Person Type"))

    sign_auth           = forms.FileField (required=False, validators=[validate_file_type], label=_('Sign Auth'))
    trade_book          = forms.FileField (required=False, validators=[validate_file_type], label=_('Trade Book'))
    chamber_book        = forms.FileField (required=False, validators=[validate_file_type], label=_('Chamber Book'))
    trademark           = forms.FileField (required=False, validators=[validate_file_type], label=_('Trade Mark'))
    import_license      = forms.FileField (required=False, validators=[validate_file_type], label=_('Import License'))
    healthy_preview     = forms.FileField (required=False, validators=[validate_file_type], label=_('Healthy Preview'))
    agency_book         = forms.FileField (required=False, validators=[validate_file_type], label=_('Agency Book'))
    varieties_revealed  = forms.FileField (required=False, validators=[validate_file_type], label=_('Varieties Revealed'))
    customs_declaration = forms.FileField (required=False, validators=[validate_file_type], label=_('Customs Declaration'))
    industrial_facility = forms.FileField (required=False, validators=[validate_file_type], label=_('Industrial Facility'))
    federation_of_associations  = forms.FileField(required=False, validators=[validate_file_type], label=_('Federation Of Associations'))

class OrderForm(ModelForm):
    class Meta:
        model = Order_MS_VCHR_XO
        fields = ['order_no', 'order_date', 'order_state', 'location', 'VEND_CODE', 'VEND_DESC_ARABIC', 'notes', 'table_data']
#        error_messages = {
#            'name': {
#                'required': _("Please select item in the list."),
#            },
#        }
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.fields['location'].error_messages.update({
            'required':_("Please select location"),
            })
    state_CHOICES = ( (_('Opened'), _('Opened')), (_('Closed'), _('Closed')))

    order_no        = forms.IntegerField(required=True)
    order_date      = forms.DateField(input_formats=['%y-%m-%d'])
    order_state     = forms.ChoiceField(required=True, widget=forms.Select(attrs={}), choices=state_CHOICES)
    VEND_CODE       = forms.IntegerField()
#    location        = forms.CharField(required=True)
    location        = forms.ModelChoiceField(queryset=Location.objects.all(), error_messages={"required": "Please select locaion from the list."})
#    item            = forms.ModelChoiceField(queryset=Product.objects.values_list('ARABIC_NAME').filter(VEND_CODE=1).distinct())
    VEND_DESC_ARABIC= forms.CharField(required=True)
    notes           = forms.CharField(widget=forms.Textarea(), required=True)
    quantity        = forms.IntegerField(required=False, min_value=1)
#    order_image     = forms.ImageField(required=False)

#    def clean_location(self):
#        location = self.cleaned_data.get("location")
#        if not location:
#            raise forms.ValidationError("please select a location")
#        return location

#    def clean_quantity(self):
#        quantity = self.cleaned_data.get("quantity")
#        if quantity != 2:
#            raise forms.ValidationError("wrong number")
#        return quantity

class SalesOrderForm(ModelForm):
    class Meta:
        model = Order_MS_VCHR_XO
        fields = ['order_no', 'order_date', 'order_state', 'location', 'VEND_DESC_ARABIC', 'notes', 'image_data']
    def __init__(self, *args, **kwargs):
        super(SalesOrderForm, self).__init__(*args, **kwargs)
    
    state_CHOICES = ( (_('Opened'), _('Opened')), (_('Closed'), _('Closed')))
    order_no        = forms.IntegerField    (required=True)
    order_state     = forms.ChoiceField     (required=True, widget=forms.Select(attrs={ } ), initial=_('Closed'),  choices=state_CHOICES)
    notes           = forms.CharField       (required=True, widget=forms.Textarea())
    image_data      = forms.ImageField      (required=True, validators=[validate_image_type], label=_('Order Data'),  error_messages={'required': _("Please upload data File")})
    order_date      = forms.DateField       (input_formats=['%y-%m-%d'])
    location        = forms.ModelChoiceField(queryset=Location.objects.all(),   error_messages={'required': _("Please select location from the list.")})
    VEND_DESC_ARABIC= forms.ModelChoiceField(queryset=Vendor.objects.all(),     error_messages={'required': _("Please select vendor from the list.")})
#    order_image     = forms.ImageField(required=False)
#    order_state.widget.attrs['readonly'] = True

class ConfirmedOrderForm(ModelForm):
    class Meta:
        model = Order_MS_VCHR_XO
        fields = ['order_no', 'order_image']
    
    
    order_no        = forms.IntegerField(required=True, label='Your order')
    order_image     = forms.FileField(required=True, validators=[validate_file_type])
    order_no.widget.attrs['readonly'] = True

class ProductsSheetForm(ModelForm):
    class Meta:
        model = Product
        fields = ['VEND_CODE', 'products_sheet']

    VEND_CODE = forms.IntegerField(required=False, label='Vendor vend code')
    products_sheet = forms.FileField(required=True, label='File', validators=[validate_products_file_type])
    VEND_CODE.widget.attrs['readonly'] = True


class ChiqueForm(ModelForm):
    class Meta:
        model = Chique 
        fields = ['vendor_id', 'chique_image']

    vendor_id    = forms.IntegerField(required=True, label='vendor_id')
    chique_image = forms.ImageField(required=True, label='File', validators=[validate_image_type])
    vendor_id.widget.attrs['readonly'] = True


class BillForm(ModelForm):
    class Meta:
        model =  Bill
        fields = ['bill_file' ]
    bill_file = forms.FileField(required=True, label='File', validators=[validate_billFile_type])

