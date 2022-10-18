from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.contrib import messages
from django.conf import settings

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect 
from django.template import RequestContext
from django.http import HttpResponse

#from random_username.generate import generate_username
#from random_password import random_password
from .forms import SignUpForm, CustomerForm, OrderForm
from .decorators import *
from datetime import datetime
from .models import *
import pandas as pd
import xlrd, os
from django.utils.translation import gettext_lazy as _

from project import settings as st
###############################################################################
def createGroup(request):
    Group.objects.create(name=_('admins'))
    Group.objects.create(name=_('vendors'))
    Group.objects.create(name=_('sales'))
    Group.objects.create(name=_('financials'))
    Group.objects.create(name=_('users'))
    return redirect('list_users')
################################################################################
def createAdmin(request):
    user = User.objects.create(
            username="admin", 
            password=make_password("aIDGJS2hCZ"),
            first_name="sayed", 
            last_name="ayad",
            is_staff = True,
            is_superuser= True,
            email="sayed@gmail.com",
            person_type= _("Admin"),
        )
    group = Group.objects.get(name=_('admins'))
    user.groups.add(group)
    context={}
    return redirect('list_users') 
################################################################################
def createVendor(request):
    loc = os.path.join(os.getcwd(),"vendors.xlsx")
    usernames = [line.rstrip('\n') for line in open(os.path.join(os.getcwd(),'usernames'))]
    passwords = [line.rstrip('\n') for line in open(os.path.join(os.getcwd(),'passwords'))]
#    wb = xlrd.open_workbook(loc)
#    sheet = wb.sheets()[0]
#    sheets = pd.ExcelFile(loc)
    file = pd.read_excel(loc, 'VENDORS')
    vendors_list=[]
    for i,row in file[0:200].iterrows():
        data = {"VEND_CODE" : int(row[0]), "VEND_DESC_ARABIC" : row[1]}
        vendors_list.append(data)
        user = User.objects.create(username=usernames[i], password=make_password(passwords[i]), person_type=_("Vendor"), VEND_DESC_ARABIC= row[1], VEND_CODE=row[0])
        user.groups.add(2)
        vendor = Vendor.objects.create(user=user, VEND_CODE=row[0], VEND_DESC_ARABIC= row[1])
        ######################################################################################################################
    for i,row in file[1201:1230].iterrows():
        user = User.objects.create(username=usernames[i], password=make_password(passwords[i]), person_type=_("Sales"))
        user.groups.add(3)
        Sales.objects.create(user=user, sales_code=i)
        ######################################################################################################################
    for i,row in file[1231:1250].iterrows():
        user = User.objects.create(username=usernames[i], password=make_password(passwords[i]), person_type=_("Financial"))
        user.groups.add(4)
        Accounts.objects.create(user=user, accounts_code=i)
    
    return redirect('list_users')
##############################################################################
def createLocation(request):
    #loc = os.path.join(os.getcwd(),"vendors.xlsx")
    #wb = xlrd.open_workbook(loc)
    #sheet = wb.sheet_by_index(0)
    #loc_sheet = wb.sheet_by_index(0)
    #for x in range(1,loc_sheet.nrows):
    loc = os.path.join(os.getcwd(),"vendors.xlsx")
    file = pd.read_excel(loc, 'LOCATION')
    print("location")
    loc_list=[]
    for i,row in file[0:].iterrows():
        print(row[0])
        print(row[1])
        data = {"LOCN_ID" : int(row[0]), "LOCN_NAME" : row[1]}
        loc_list.append(data)
        Location.objects.create(LOCN_ID=int(row[0]), LOCN_NAME=row[1])
    context = {'locs' : loc_list}
    return redirect('list_users')
###############################################################################
def createItem(request):
    loc = os.path.join(os.getcwd(),"ITEMS_SITE__2_10.xlsx")
    file = pd.read_excel(loc, 'Sheet1')
    items_list=[]
    for i,row in file[1:].iterrows():
        print(row)
        data = { 
                "ID"         : row[0],
                "ARABIC_NAME": row[1],
                "VEND_CODE"  : int(row[2]),
                "PACK_ID"    : row[3],
                "NO_OF_ITEMS": row[4],
                "UNIT_DESC"  : row[5],
                "PURCH_PRICE": row[6],
                "SALE_PRICE" : row[7],
                "BARCODE"    : row[8]
                }
        items_list.append(data)
        Product.objects.create(
#                vendor_id=int(row[2]), 
#                ID=row[0], 
                ARABIC_NAME=row[1], 
                VEND_CODE=int(row[2]), 
                PACK_ID=int(row[3]), 
                NO_OF_ITEMS=int(row[4]), 
                UNIT_DESC=row[5], 
                PURCH_PRICE=row[6], 
                SALE_PRICE=row[7], 
                BARCODE=row[8])
        print("after")

    context={
            "items_list" : items_list,
            }
    return redirect('list_items')
###############################################################################
def listItems(request):
    items = Product.objects.all()
    context = {'items' : items}
    return render(request, 'deploy/lst_items.html', context)
###############################################################################
def listUsers(request):
    users = User.objects.all()
    vendors = Vendor.objects.all()
    products = Product.objects.all()
    locations= Location.objects.all()
    groups = Group.objects.all()
    print("aaaaaaaaaaaaaa")
    context = {
            'users':users,
            'vendors':vendors,
            'locations':locations,
            'groups':groups,
            }
    return render(request, 'deploy/lst_users.html', context )
###############################################################################

