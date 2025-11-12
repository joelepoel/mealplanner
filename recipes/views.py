from django.shortcuts import redirect
from .forms import RecipeForm, ProfileForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe, Profile

class RecipeListView(LoginRequiredMixin,ListView):
    model = Recipe
    context_object_name = 'recipes'

    def get_queryset(self):
        #only shows recipes of logged in user
        return Recipe.objects.filter(user=self.request.user)

class RecipeDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Recipe
    def test_func(self): #only allows access if recipe belongs to user
        recipe = self.get_object()
        return recipe.user == self.request.user
    
class RecipeCreateView(LoginRequiredMixin,CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy('recipes:recipe_list')#redirects to page after success

    def form_valid(self, form):
        #assigns logged in user as author before saving
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy('recipes:recipe_list')

    def test_func(self): #only allows users to update if its their own recipe
        recipe = self.get_object()
        return recipe.user == self.request.user
    
class RecipeDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:recipe_list')

    def test_func(self): #only allows user to delete own recipes
        recipe = self.get_object()
        return recipe.user == self.request.user

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'recipes/profile_update.html'
    success_url = reverse_lazy('recipes:recipe_list')

    def get_object(self, queryset = None):
        # Return the current user's profile only
        return self.request.user.profile