from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("about/",views.about,name="about"),
    path("blog/",views.blog,name="blog"),
    path("blog/results/", views.result, name="results"),
    path("blog/<slug:slug>",views.post_details,name="post_detail"),
    path("blog/tag/<str:tag>/",views.tag_posts,name="tag_posts"),
    path("blog/category/<str:cat>/",views.category_post,name="category_posts"),
    path("signup/", views.signUp,name="signup"),
    path("login/",views.logIn,name="login"),
    path("contact/",views.contact,name="contact"),
    path("logout/",views.logOut, name= "logout")
]