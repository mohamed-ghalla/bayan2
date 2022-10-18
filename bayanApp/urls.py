from django.urls import path
from . import views, views_deploy
from django.contrib.auth import views as auth_views
#####################################################################
#urlpatterns = [
#    path("", views.index, name="index"),
#]
#################################################################
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signUp, name='signup'),
#    path('signup', views.signupPage, name='signup'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('order', views.orderXo, name='order'),
    path('sales_order', views.salesOrder, name='sales_order'),
    path('change_password', views.changePassword, name='change_password'),
#    path('reset_password', views.resetPassword, name='reset_password'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ="password_reset_complete"),

    path('404', views.my404, name='my404'),
    path('403', views.my403, name='my403'),

#    path('en/login', views.loginPage, name='login'),
#    path('ar/login', views.loginPage, name='login'),

    path('profile', views.profile, name='profile'),
    path('update_profile/', views.updateProfile, name='update_profile'),
    path('update_all_products/', views.updateAllProducts, name='update_all_products'),
    path('update_vendor_products/',views.updateVendorProducts, name="update_vendor_products"),
    path('list_vendors/', views.listVendors, name='list_vendors'),
    path('list_newUsers/', views.listNewUsers, name='list_newUsers'),
    path('list_all_orders/', views.listAllOrders, name='list_all_orders'),
    path('list_orders/<int:VEND_CODE>/', views.listOrders, name='list_orders'),
    path('list_vendor_info/<int:VEND_CODE>/', views.listVendorInfo, name='list_vendor_info'),
    path('list_newUser_info/<int:user_id>/', views.listNewUserInfo, name='list_newUser_info'),
    path('list_products/<int:VEND_CODE>/', views.listProducts, name='list_products'),
    path('list_bills/<int:VEND_CODE>/', views.listBills, name='list_bills'),
#    path('order_details/<int:id>/', views.orderDetails, name='order_details'),
    path('print_order/<int:order_no>/', views.printOrder, name='print_order'),
    path('delete_order/<int:order_no>/', views.deleteOrder, name='delete_order'),
    path('delete_old_orders/<str:month>/<str:day>/<str:year>/',views.deleteOldOrders, name='delete_old_orders'),
#    path('vendor_orders/<int:vendor_id>/', views.vendorOrders, name='vendor_orders'),
#    path('new_vendor', views.newVendor, name='new_vendor'),
    path('upload_chique/', views.uploadChique, name='upload_chique'),
    path('upload_bill/', views.uploadBill, name='upload_bill'),
    path('upload_conf_order/', views.uploadConfOrder, name='upload_conf_order'),
    path('create_group', views_deploy.createGroup, name='create_group'),
    path('create_admin', views_deploy.createAdmin, name='create_admin'),
    path('create_vendor', views_deploy.createVendor, name='create_vendor'),
    path('create_item',views_deploy.createItem, name='create_item'),
    path('create_location', views_deploy.createLocation, name='create_location'), 
    path('list_users/', views_deploy.listUsers, name ='list_users'),
    path('list_items/', views_deploy.listItems, name ='list_items'),
    path('list_transactions/<int:VEND_CODE>/', views.listTransactions, name = 'list_transactions'),
    path('read_transaction/<int:t_no>/', views.readTransaction, name = 'read_transaction'),
#    path('list', views.vendor, name='vendor'),
#    path('items/<int:id>', views.items, name='items'),
    #path('details/<int:id>/', views.details, name='details'),
]

