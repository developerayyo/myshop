# index.py
# index.py

from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

# import algoliasearch_django as algoliasearch

from .models import Category, Product

# algoliasearch.register(Category)
# algoliasearch.register(Product)

@register(Category)
class CategoryModelIndex(AlgoliaIndex):
    fields = ('name')
    geo_field = 'name'
    settings = {'searchableAttributes': ['name']}
    index_name = 'category_index'


@register(Product)
class YourModelIndex(AlgoliaIndex):
    fields = ('name')
    geo_field = 'name'
    settings = {'searchableAttributes': ['name']}
    index_name = 'product_index'
