from django.shortcuts import render,redirect

from owner import forms

from owner.models import Book
from django.contrib import messages
# Create your views here.

def registration(request):
    form=forms.RegisterForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.RegisterForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data["first_name"]
            username = form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password1=form.cleaned_data["password1"]
            confirm_password=form.cleaned_data["confirm_password"]
            print(firstname,username,email,password1,confirm_password)
            return redirect("login")
    return render(request,"registration.html",context)

def login(request):
    form=forms.LoginForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            print(username,password)
            return redirect("op")
    return render(request,"login.html",context)

#8000/owner/books/add
def book_add(request):
   form=forms.BookAddForm()
   context={"form":form}
   if request.method=="POST":
       form=forms.BookAddForm(request.POST)
       if form.is_valid():
           # book_name=form.cleaned_data["book_name"]
           # author=form.cleaned_data["author"]
           # price=form.cleaned_data["price"]
           # copies=form.cleaned_data["copies"]
           # category=form.cleaned_data["category"]
           # # context={"book_name":book_name,"author":author,"price":price,"copies":copies}
           # book = Book(book_name=book_name, author=author, price=price, copies=copies,category=category)
           # book.save()

           form.save()
           messages.success(request,"Book added successfully")
           return redirect('allbooks')
       else:
           return  render(request,'book_add.html',{"form":form})
   return render(request,'book_add.html',context)






        # # first class
        # # print("inside post book")
        # # print(request.headers)
        # # print(request.POST)
        # # book_name=request.POST["Book_name"]
        # # author=request.POST["Author"]
        # # book_price=request.POST["Book_price"]
        # # book_copies=request.POST["Book_copies"]
        # # print(book_name,author,book_price,book_copies)
        # return render(request, "book_add.html")


def book(request):
    form=forms.BookserachForm()
    book=Book.objects.all()
    context={}
    context["books"]=book
    context["form"]=form
    if request.method=="POST":
        form=forms.BookserachForm(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data["book_name"]
            book=Book.objects.filter(book_name__contains=book_name)|Book.objects.filter(author__contains=book_name)
            context["books"]=book
            return render(request, "books.html", context)

    return render(request,"books.html",context)

#8000/owner/books/change/{id}
def book_change(request,id):
     book=Book.objects.get(id=id)
     # data={
     #     "book_name":book.book_name,
     #     "author":book.author,
     #     "price":book.price,
     #     "copies":book.copies,
     #     "category":book.category
     # }
     # form = forms.BookEditForm(initial=data)
     form=forms.BookEditForm(instance=book)
     context={"form":form}
     if request.method=="POST":
         form=forms.BookEditForm(request.POST,instance=book)
         if form.is_valid():
             # book_name = form.cleaned_data["book_name"]
             # author = form.cleaned_data["author"]
             # price = form.cleaned_data["price"]
             # copies = form.cleaned_data["copies"]
             # category = form.cleaned_data["category"]
             # book.book_name=book_name
             # book.author=author
             # book.price=price
             # book.copies=copies
             # book.category=category
             # book.save()
             form.save()
             return redirect('allbooks')
         else:
             return render(request, "books_change.html", {"form":form})

     return render(request,"books_change.html",context)

#8000/owner/books/remove/{id}
def book_remove(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('allbooks')

def home(request):
    if request.method=="GET":
        return render(request,"index.html")

def options(request):
    if request.method=="GET":
        return render(request,"tasks.html")

def bookdetail(request,id):
    book=Book.objects.get(id=id)
    context={"book":book}
    return render(request,"bookdetails.html",context)





