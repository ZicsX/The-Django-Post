from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm
from users.models import User

def home(request):
    all_blogs = Blog.objects.all().order_by('-date_posted')
    paginator = Paginator(all_blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    if request.user.is_authenticated:
        user_blogs = Blog.objects.filter(author=request.user).order_by('-date_posted')
    else:
        user_blogs = None

    all_users = None  # Initialize all_users variable as None

    if request.user.is_authenticated and request.user.is_staff:
        all_users = User.objects.all()  # Retrieve all users if the user is admin

    return render(request, 'blog/home.html', {'page_obj': page_obj, 'user_blogs': user_blogs, 'all_users': all_users})

def blog_new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', blog_id=blog.pk)  # Redirect to the detail view of the newly created blog
    else:
        form = BlogForm()
    
    return render(request, 'blog/blog_new.html', {'form': form})

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

@login_required
def blog_edit(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', blog_id=blog_id)
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/blog_edit.html', {'form': form, 'blog': blog})

@login_required
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'blog/blog_delete.html', {'blog': blog})
