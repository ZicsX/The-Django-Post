from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserChangeForm
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import UserUpdateForm
from django import forms
from .models import User
from blog.models import Blog

from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAdminUser

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

class UserUpdateForm(UserChangeForm):
    password1 = forms.CharField(label='New Password', strip=False, widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirm New Password', strip=False, widget=forms.PasswordInput, required=False)

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['email', 'designation', 'age', 'gender']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('home')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)


@staff_member_required
def get_user_info(request, username):
    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        user_info = {
            'username': user.username,
            'email': user.email,
            'designation': user.designation,
            'age': user.age,
            'gender': user.gender
        }
        return JsonResponse(user_info)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@staff_member_required
def export(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    users = User.objects.all()

    if start_date and end_date:
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)

        users = users.filter(
            date_of_registration__date__range=(start_date, end_date)
        )

    data = []
    for user in users:
        user_data = {
            'mail_id': user.email,
            'password': user.password,
            'designation': user.designation,
            'age': user.age,
            'gender': user.gender,
            'date_of_registration': user.date_of_registration,
        }
        data.append(user_data)
    return JsonResponse(data, safe=False)

@staff_member_required
def export_data(request):
    username = request.GET.get('username')
    email = request.GET.get('email')

    users = User.objects.all()

    if username:
        users = users.filter(username=username)
    if email:
        users = users.filter(email=email)

    data = []
    for user in users:
        user_data = {
            'mail_id': user.email,
            'password': user.password,
            'designation': user.designation,
            'age': user.age,
            'gender': user.gender,
            'date_of_registration': user.date_of_registration,
        }
        data.append(user_data)
    return JsonResponse(data, safe=False)

@staff_member_required
def export_records(request):
    username = request.GET.get('username')
    email = request.GET.get('email')

    blogs = Blog.objects.all()

    if username:
        blogs = blogs.filter(author__username=username)
    if email:
        blogs = blogs.filter(author__email=email)

    data = []
    for blog in blogs:
        blog_data = {
            'title': blog.title,
            'content': blog.content,
            'author': blog.author.username,
            'date_posted': blog.date_posted,
        }
        data.append(blog_data)
    return JsonResponse(data, safe=False)

@login_required
def export_user_blogs(request):
    user = request.user

    blogs = Blog.objects.filter(author=user)

    data = []
    for blog in blogs:
        blog_data = {
            'title': blog.title,
            'content': blog.content,
            'date_posted': blog.date_posted,
        }
        data.append(blog_data)
    return JsonResponse(data, safe=False)

# class UserViewSet(viewsets.ViewSet):
#     permission_classes = [IsAdminUser]
    
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

