from django.shortcuts import render, redirect
from .forms import NewBlog
from .models import Blog
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.

@login_required(login_url="userLogin")
def blogHome(request):
    allBlogs= Blog.object.all()
    return render (request, "blog/blogHome.html", {"allBlogs":allBlogs})


#....add new blog logic
def addblog(request):
    if request.method== "POST":
       form = NewBlog(request.POST)
       if form.is_valid():
           form.save()
           return redirect ("blogHome")
       else:
           newform = NewBlog()
           return render (request, "blog/addBlog.html", {"form": newform})
       

def blogHome(request): 
    allblogs = Blog.objects.all()
    return render(request, "blog/blogHome.html", {"allBlogs": allblogs})


#...... ADD A NEW BLOG LOGIC

def addBlog(request):
    if request.method == "POST":
        form = NewBlog(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:    
        newForm = NewBlog
    return render(request, "blog/addBlog.html", {"form": newForm})

#..... A BLOG DETAILS LOGIC

def blogDetails(request, pk):
    blog = Blog.objects.get(pk = pk)
    return render(request, "blog/blogDetails.html", {"blog": blog})


#create a delete function that will delete the blog post and redirect to the bloghome

def is_admin(user):
    return user.is_superuser or user.is_staff

@user_passes_test(is_admin)
#delete blog
def deleteBlog(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == "POST":
        blog.delete()
        return redirect ("blogHome")
