# Register your models here.
from django.contrib import admin
from .models import User, Vendor, Sales, Accounts, Product, Location, Order_MS_VCHR_XO, ConfirmedOrders
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as UA
from .forms import SignUpForm, CustomerForm

# Register your models here.
#class UserAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(Vendor)
#admin.site.register(Product)
#admin.site.register(Location)

admin.site.site_header = _('Bayan Co. Administration')
#admin.site.site_url = 'http://3.12.104.158:8000/'
#print("aaaaaaaaaaaaaaaaaa    admin : ",admin.site)

#admin.site.register(User, UA)
#class UserAdmin(UA):
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
#    form = SignUpForm #CustomerForm
#    fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'phone', 'VEND_DESC_ARABIC', 'email', 'person_type', 'type_of_supply', 
#            'is_staff', 'is_superuser', 'is_active', 'date_joined', 'profile_pic', 'groups', 
#            'sign_auth', 'trade_book', 'chamber_book', 'trademark', 'import_license', 'healthy_preview', 'agency_book', 
#            'varieties_revealed', 'federation_of_associations', 'industrial_facility', 'customs_declaration']

    search_fields = ('username', 'phone')

    list_display = ('username', 'id', 'first_name', 'last_name', 'email', 
            'phone', 'person_type', 'VEND_DESC_ARABIC')
    
    list_filter = ('person_type',)

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.form = CustomerForm
            if obj.person_type == _('Vendor'):
                self.fields = ['username', 'first_name', 'last_name', 'phone', 'VEND_DESC_ARABIC', 'email', 'person_type', 'type_of_supply',
                'is_staff', 'is_superuser', 'is_active', 'date_joined', 'profile_pic', 'groups',
                'sign_auth', 'trade_book', 'chamber_book', 'trademark', 'import_license', 'healthy_preview', 'agency_book',
                'varieties_revealed', 'federation_of_associations', 'industrial_facility', 'customs_declaration']

            else:
                self.fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'person_type',
                'is_staff', 'is_superuser', 'is_active', 'date_joined', 'profile_pic', 'groups']

        else:
            self.form = SignUpForm
            self.fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'phone', 'VEND_DESC_ARABIC', 'email', 'person_type', 'type_of_supply',
            'is_staff', 'is_superuser', 'is_active', 'date_joined', 'profile_pic', 'groups',
            'sign_auth', 'trade_book', 'chamber_book', 'trademark', 'import_license', 'healthy_preview', 'agency_book',
            'varieties_revealed', 'federation_of_associations', 'industrial_facility', 'customs_declaration']
            
        return super(UserAdmin, self).get_form(request, obj, **kwargs)
#    def add_view(self, request, extra_content=Nona):
#        pass

#    def change_view(self, request, object_id, extra_content=None):
#        pass
#        self.exclude = ('password1', 'password2',)
#        return super(UserAdmin, self).change_view(request, object_id)

#    readonly_fields=['password1', 'password2',]
#    form.base_fields['password1'].disabled = True
#    form.base_fields['password2'].disabled = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    search_fields = ('ARABIC_NAME', 'VEND_CODE',)
    list_display = ('ARABIC_NAME', 'VEND_CODE', 'PACK_ID', 'UNIT_DESC', 
            'NO_OF_ITEMS', 'PURCH_PRICE', 'SALE_PRICE', 'BARCODE' )

    list_filter = ('UNIT_DESC',)

    def account_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Deposit</a>&nbsp;'
            '<a class="button" href="{}">Withdraw</a>',
            reverse('admin:account-deposit', args=[obj.pk]),
            reverse('admin:account-withdraw', args=[obj.pk]),
        )
    account_actions.short_description = 'Account Actions'
    account_actions.allow_tags = True

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    fields = ['user', 'VEND_CODE', "VEND_DESC_ARABIC"]
    list_display = ('VEND_CODE', 'VEND_DESC_ARABIC', 'user')
    search_fields = ('VEND_CODE', 'VEND_DESC_ARABIC',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('sales_code', 'user')
    search_fields = ('sales_code', 'user__username',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
 #   list_display = ('accounts_code', 'user')
 #   search_fields= ('accounts_code', 'user__username',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ('LOCN_NAME',)
    list_display = ('LOCN_ID', 'LOCN_NAME')

@admin.register(Order_MS_VCHR_XO)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_no', 'order_date', 'order_state', 'location', 'notes', 'image_tag', 'order_image' )
    search_fields = ('order_no', 'location',)
    list_filter = ('order_state', 'location')

    filter_horizontal = ()
    fieldsets = ()


#@admin.register(ConfirmedOrders)
#class ConfirmedOrderAdmin(admin.ModelAdmin):
#    list_display = ('order_no', 'order_image', 'vendor')
