from django import forms
from django.forms import ModelForm
from owner.models import Book
import re

class BookAddForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "copies":forms.NumberInput(attrs={"class":"form-control"}),
            "category":forms.TextInput(attrs={"class":"form-control"})
        }

    # book_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # author = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    # copies = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    # category=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data["price"]
        copies=cleaned_data["copies"]
        author=cleaned_data["author"]
        category=cleaned_data["category"]
        book_name=cleaned_data["book_name"]
        books=Book.objects.filter(book_name__iexact=book_name)
        if books:
            msg="book name is already exist"
            self.add_error("book_name",msg)
        if int(price) < 0:
            msg="invalid price"
            self.add_error("price",msg)
        if int(copies) < 0:
            msg="invalid copies"
            self.add_error("copies",msg)
        x="[a-zA-Z]*"
        matcher=re.fullmatch(x,author)
        if matcher is not None:
            pass
        else:
            msg="please enter valid author name"
            self.add_error("author",msg)
        bookmatcher=re.fullmatch(x,book_name)
        if bookmatcher is not None:
            pass
        else:
            msg = "please enter valid book name"
            self.add_error("book_name", msg)

        catmatcher=re.fullmatch(x,category)
        if catmatcher is not None:
            pass
        else:
            msg = "please enter valid category name"
            self.add_error("category", msg)




class RegisterForm(forms.Form):

    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control k v"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class BookEditForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        widgets = {
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"})
        }

    # book_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # author = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    # copies = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    # category = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

class BookserachForm(forms.Form):
    book_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))




