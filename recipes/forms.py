from django import forms
from .models import Recipe, Profile


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['image','title','instructions','ingredients']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 2 * 1024 * 1024:  # 2 MB limit
            raise forms.ValidationError("Image file too large (max 2MB).")
        return image

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar and avatar.size > 1 * 1024 * 1024:  # 1 MB limit
            raise forms.ValidationError("Avatar too large (max 1MB).")
        return avatar