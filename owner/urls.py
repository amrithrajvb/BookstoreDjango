from django.urls import path
from owner import views
urlpatterns=[
    path("",views.home,name="home"),
    path("accounts/register",views.registration,name="signup"),
    path("accounts/Login",views.login,name="login"),
    path("books/add",views.book_add,name="addbook"),
    path("books",views.book,name="allbooks"),
    path("books/change/<int:id>",views.book_change,name="changebook"),
    path("books/remove/<int:id>",views.book_remove,name="removebook"),
    path("accounts/Login/list",views.options,name="op"),
    path("books/details/<int:id>",views.bookdetail,name="bookdetail")
]