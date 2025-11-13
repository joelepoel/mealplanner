from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeUpdateView, RecipeCreateView, RecipeDeleteView, ProfileUpdateView, recipe_plan

app_name = 'recipes'
urlpatterns = [
    path('', RecipeListView.as_view(), name = 'recipe_list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name = 'recipe_detail'),
    path('create/', RecipeCreateView.as_view(), name = 'recipe_create'),
    path('<int:pk>/update/', RecipeUpdateView.as_view(), name = 'recipe_update'),
    path('<int:pk>/delete/', RecipeDeleteView.as_view(), name = 'recipe_confirm_delete'),
    path('profile_update/', ProfileUpdateView.as_view(), name = 'profile_update'),
    path('plan/', recipe_plan, name='recipe_plan'),
]