from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Review



def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    #this gets the product fromt he database based on the slug were working with
    #the slugs have to be unique, otherwise mutlipleojectsreturned error will occur
    #when creating the item as admin, slug and name of the item should match

    if request.method == 'POST':
        rating = request.POST.get('rating', '3')
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)

            if reviews.count() > 0:
                 review = reviews.first()
                 review.rating = rating 
                 review.content = content 
                 review.save() 
                 #this code allows only one comment for each user for each dress, it prevents multiple comments by same person, only their latest comment
            else:
                review = Review.objects.create(
                    product=product,
                    content =content,
                    rating=rating,
                    created_by = request.user
                )
                    
            return  redirect('product', slug=slug)

    return render(request, 'product/product.html', {'product': product})


# Create your views here.
