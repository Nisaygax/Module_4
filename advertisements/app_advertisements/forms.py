from django import forms
from django.forms import ModelForm
from .models import Advertisement

# class AdvertisementForm(forms.Form):
#     title = forms.CharField(
#         max_length=64, widget = forms.TextInput(attrs = {'class': 'form-control form-control-lg'})
#         )
#     description = forms.CharField(
#         widget = forms.Textarea(attrs = {'class': 'form-control form-control-lg'})
#         )
#     price = forms.DecimalField(
#         widget = forms.NumberInput(attrs = {'class': 'form-control form-control-lg'})
#         )
#     auction = forms.BooleanField(
#         required = False, widget = forms.CheckboxInput(attrs = {'class': 'form-check-input'})
#         )
#     image = forms.ImageField(
#         widget = forms.FileInput(attrs = {'class': 'form-control form-control-lg'})
#         )  
    
class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {'title': forms.TextInput(attrs = {'class': 'form-control form-control-lg'}),
                   'description': forms.Textarea(attrs = {'class': 'form-control form-control-lg'}),
                   'price': forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}),
                   'auction': forms.CheckboxInput(attrs = {'class': 'form-check-input'}),
                   'image': forms.FileInput(attrs = {'class': 'form-control form-control-lg'})}

    def clean(self):
        title = self.cleaned_data.get('title')

        if title.startswith('?'):
            self.errors['title'] = self.error_class(['Заголовок не может начинаться с "?"'])
        
        return self.cleaned_data