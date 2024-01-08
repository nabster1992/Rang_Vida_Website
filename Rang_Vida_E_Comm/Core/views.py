
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from Products.models import Product, Category
from .forms import SignUpForm

# Create your views here
#creating and defining the view for the front page
def frontpage(request):
    #[0:8] means its slicing from objects.all to show the first 8 new products added on front page
    products = Product.objects.all()[0:8]
    return render(request, 'core/front_page.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user )

            return redirect('/')
    else:
            form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})
    
def page_404(request, exception):
    return render(request, 'core/page_404.html', status=404)

@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')


@login_required
def edit_myaccount(request):
    if request.method == 'POST':

        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')



    




def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')
#this is tied to the slug of the category, which admin enters when creating the category, in the input field
# The line active_category = request.GET.get('category', '') is Python code commonly used in a Django view to retrieve the value of a query parameter from the request.
# Let's break it down:
# request: In Django views, the request object contains information about the current HTTP request, including any data sent with the request (such as form data or query parameters).
# .GET: The GET attribute of the request object is a dictionary-like object that contains all the query parameters from the URL.
# .get('category', ''): The .get() method is used to retrieve the value of a specific key from the dictionary. In this case, it's looking for the value associated with the key 'category'.
# If the 'category' key exists in the query parameters, the method returns its value.
# If the key does not exist, it returns an empty string (''), which is the default value provided as the second argument to .get().
    #wrapping the dictionary in 'context' keeps the return render code a bit cleaner


    if active_category:
        products = products.filter(category__slug=active_category)
        #this filters out the products based on category_slug and also if it's active

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    #because the input file for search within the shop.html file contains name=query, were requesting to get that and filter it regardless if its case sensitive when nterd in the search bar
    #thats why its icontains=query
    #Q(description__icontains=query), allows us to return results from descriptions as well


    context = {
        'categories': categories,
        'products': products,
    }

    

    return render(request, 'core/shop.html', context)