from django.urls import path
from .views import family_tree_api, family_tree

urlpatterns = [
    path('api/family_tree/', family_tree_api, name='family_tree_api'),
    path('', family_tree, name='family_tree'),
]
