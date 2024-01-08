from django.contrib import admin
from .models import Category, Product, Review

# Register your models here.

# class ReviewInline(admin.TabularInline):
#     model = Review
#     raw_id_fields = ['product']


# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ['product', 'content', 'rating', 'created_by']
#     list_filter = [ 'created_at']
#     search_fields = [ 'created_by', 'content']
#     inlines = [ReviewInline]

admin.site.register(Review)    
admin.site.register(Category)
admin.site.register(Product)





