from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import pandas as pd

from .models import Post,Tag,Comment,Category, About, Staff, SiteUsers
from .forms import Search, CommentForm, SignUpForm, LoginForm

# Create your views here.

posts = Post.objects.all()
categories = Category.objects.all()
tags = Tag.objects.all()

def refresh():
    new_tags = []
    for tg in tags:
        tg.refresh_from_db()
        new_tags.append(tg)
    new_cats = []
    for cat in categories:
        cat.refresh_from_db()
        new_cats.append(cat)
    return {"tags":new_tags, "categories":new_cats}


desc_ordered_posts = posts.order_by('-date','title')[:3]

header = {"home":"home","about":"about","blog":"blog","contact":"contact", "lg":"login"}

def df_banner():
    slugs = []
    total_cmts = []
    for pst in posts:
        slugs.append(pst.slug)
        total_cmts.append(pst.comments.all().count())
    slug_dict = {'slug':slugs,'total_cmts':total_cmts}
    df = pd.DataFrame(slug_dict)
    top_slug = df.sort_values('total_cmts', ascending= False).head()['slug']
    banner = []
    for i in top_slug:
        banner.append(i)
    return banner

def banner_slug(slug):
    return Post.objects.get(slug=slug) 

def home(request):
    active = ["home"]
    banner_posts = list(map(banner_slug,df_banner()))


    return render(request,'blog/index.html',{
        "posts" : desc_ordered_posts,
        "categories" : refresh()['categories'],
        "tags" : refresh()['tags'],
        "active": active,
        "home" : header["home"],
        "banners" : banner_posts,
    })

def about(request):
    about = About.objects.all()
    staff = Staff.objects.all()

    active = ["about"]
    if about is None or len(about)==0:
        is_about = False
    else:
        is_about = True

    upper_layer = []
    mid_layer = []
    lower_layer = []
    for i in staff:
        pos = int(i.position)
        if pos == 1:
            upper_layer.append(Staff.objects.get(name=i.name))
        elif pos == 2:
            mid_layer.append(Staff.objects.get(name=i.name))
        else:
            lower_layer.append(Staff.objects.get(name=i.name))
    context = {
        "abouts" : about,
        "staff_first_row" : upper_layer,
        "staff_second_row" : mid_layer,
        "staff_last_row" : lower_layer,
        "is_about" : is_about,
        "active" : active,
        "about" : header["about"],
    }
    return render(request,'blog/about.html', context)

def contact(request):
    active = ["contact"]
    context = {
        "active": active,
        "contact" : header["contact"]
        
    }
    return render(request,'blog/contact.html', context)

def blog(request):
    active = ["blog"]

    paginator = Paginator(posts.order_by('-date','title'), 6) # Show 6 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request,'blog/blog.html',{
        "categories" : refresh()['categories'],
        "tags" : refresh()['tags'],
        "page_obj" : page_obj,
        "active" : active,
        "blog" : header["blog"],
        "posts" : desc_ordered_posts,
    })

def tag_posts(request,tag):
    caption = get_object_or_404(Tag,caption=tag)
    tg_posts = caption.post_set.all()
    paginator = Paginator(tg_posts,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/tag-posts.html',{
        "page_obj" : page_obj,
        "title" : tag,
        "categories" : categories,
        "tags" : tags,
        "rec_posts" : desc_ordered_posts,
    })

def category_post(request,cat):
    caption = get_object_or_404(Category,caption=cat)
    cp_posts = caption.categories.all()
    paginator = Paginator(cp_posts.order_by("-date","title"),6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/category-posts.html',{
        "page_obj" : page_obj,
        "title" : cat,
        "categories" : categories,
        "tags" : tags,
        "rec_posts" : desc_ordered_posts,
    })

def post_details(request,slug):
    post = get_object_or_404(Post,slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            comment = Comment(name=username,comment=comment, post=post)
            comment.save()
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
        else:
           return HttpResponseRedirect(reverse("post_detail", args=[slug]))

    num_comment = post.comments.all().count()
    Post.objects.get(slug=slug)
    post_tags = post.tags.all()
    post_comments = post.comments.all()
    return render(request, 'blog/post-details.html',{
        "post_dtl" : post,
        "posts" : posts,
        "num_cmts" : num_comment,
        "post_tgs" : post_tags,
        "post_cmts" : post_comments,
        "categories" : categories,
        "tags" : tags,
        "rec_posts" : desc_ordered_posts,
    })

def result(request):
    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            search_results = Post.objects.filter(title__icontains=form.cleaned_data['search'])
            paginator = Paginator(search_results.order_by('-date','title'), 6)
            page_obj = paginator.page(1)
            return render(request,'blog/blog.html',{
                "posts" : search_results,
                "tags" : tags,
                "categories" : categories,
                "page_obj" : page_obj,
            })

def signUp(request):
    error = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(request,username=username,password=raw_password)
            if user is not None:
                SiteUsers.objects.create(user=user)
                messages.success(request, 'Account Created')
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
            else:
                error = True
                return render(request,'blog/signup.html',{
                    "form":form,
                    "error":error,
                })
        else:
            error = True
            return render(request,'blog/signup.html',{
                "form":form,
                "error":error,
            })
    form = SignUpForm()
    return render(request,'blog/signup.html',{
        "form":form,
        "error":error,
    })

def logIn(request):
    active = ["login"]
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                # error = False
                return HttpResponseRedirect(reverse("home"))
            else:
                error = True
                return render(request,'blog/login.html',context={
                    'error':error
                })
    return render(request,'blog/login.html',{
        "form":LoginForm(),
        "active": active,
        "login" : header["lg"],
    })

def logOut(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))