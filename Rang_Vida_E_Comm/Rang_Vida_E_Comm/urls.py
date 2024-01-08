"""
URL configuration for Rang_Vida_E_Comm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static  
from django.contrib import admin 
from django.urls import path, include



urlpatterns = [
    #frontpaeg is the function created within views.py file which links to core/base.html
    path('',include('Core.urls')),
    #every path which is empty, or does not match below will then be checked to see if theyre are matches within core.urls and cart.urls
    path('cart/',include('cart.urls')),
    path('orders/',include('orders.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'Core.views.page_404'
    

#from django.conf import settings and from django.conf.urls.static import static:
# These import statements are bringing in the necessary components from Django to handle static and media file serving.
# urlpatterns = [...]:

# This is the list of URL patterns for your Django project.
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT):

# This line is using the static function provided by Django to add a URL pattern for serving media files during development.
# settings.MEDIA_URL: This is the base URL under which media files will be served. It is defined in your project's settings.py.
# document_root=settings.MEDIA_ROOT: This is the filesystem path to the directory where your media files are stored. It is also defined in your project's settings.py.
   
   

#explanation of path(add_to_cart/<int:product_id/', add_to_cart, name='add_to_cart)
#path Function:

# path(...): This is a function provided by Django for defining URL patterns.
# URL Pattern String:

# 'add_to_cart/<int:product_id>/': This part defines the URL pattern. It specifies a URL route that starts with 'add_to_cart/' followed by an integer parameter named product_id.

# <int:product_id> Path Converter:
# <int:product_id>: This is a path converter. It tells Django to capture the part of the URL matched by this converter and convert it to an integer. The result is passed as the product_id parameter to the associated view function.
#The path converter helps ensure that the value captured from the URL is of the expected data type, in this case, an integer. This provides a level of validation, and Django will raise a 404 (Page Not Found) error if the value is not an integer. It helps prevent invalid URLs from reaching the view function.
#<int:product_id> is a best practice for URL patterns where an integer value is expected, such as when dealing with identifiers like product IDs. It helps ensure data integrity, improves readability, and contributes to a more robust and maintainable codebase.

# View Function:
# add_to_cart: This is the name of the view function that will be called when the URL pattern is matched.
# name Parameter:
# name='add_to_cart': This is an optional parameter that assigns a name to the URL pattern. Naming URL patterns is useful when you want to refer to them in your Django templates or code using the {% url %} template tag or the reverse function in Python.