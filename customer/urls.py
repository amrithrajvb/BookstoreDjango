from django.urls import path
from customer import views

urlpatterns=[
    path("accounts/signup",views.signup_view,name="signup"),
    path("accounts/signin",views.signin_view,name="signin"),
    path("accounts/signout",views.signout,name="signout")
]