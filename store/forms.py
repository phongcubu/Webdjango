from django import  forms
from store.models import *

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields ="__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_availabale_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
    }
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['rating','subject', 'review']

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields =['name_contact', 'email_contact','phone_contact','comment_contact']

        widgets = {
            'name_contact': forms.TextInput(attrs={'class': 'form-control','required':"required"}),
            'email_contact': forms.TextInput(attrs={'class': 'form-control','required':"required"}),
            'phone_contact': forms.TextInput(attrs={'class': 'form-control','required':"required"}),
            'comment_contact': forms.Textarea(attrs={'class': 'form-control','required':"required"}),

        }
        labels= {
            'name_contact':'Họ Và Tên',
            'email_contact': 'Email',
            'phone_contact': 'Số Điện Thoại',
            'comment_contact': 'Nội Dung Phản Hồi',
        }