from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from Core.views import frontpage, shop, signup, page_404, myaccount, edit_myaccount
from Products.views import product

# Register your models here.



urlpatterns = [

    
    path('', frontpage, name='frontpage'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit', edit_myaccount, name='edit_myaccount'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'), 
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    #path('shop/<slug:slug>', product, name='product'): This pattern includes a dynamic part <slug:slug>, which captures a slug parameter from the URL and passes it to the product view function. This is useful for displaying detailed information about a specific product. The name='product' is a name assigned to this URL pattern.
]

