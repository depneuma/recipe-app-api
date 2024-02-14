"""
Url mappings for the recipe API.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
