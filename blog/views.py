from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

import re

from .forms import SignupForm, TopicForm
from .models import Blog
from .utils import generate_blog_content


def format_blog_content(text):
    # Add proper paragraph breaks after sentences
    text = re.sub(r'([.!?])\s+', r'\1\n\n', text)
    # Clean extra paragraph breaks
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def extract_title(content: str, fallback: str) -> str:
    first_line = content.splitlines()[0].strip() if content else ""
    if first_line:
        cleaned = first_line.replace("Title:", "").replace("TITLE:", "").strip()
        if len(cleaned) > 3:
            return cleaned
    return fallback


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = SignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. You can log in now.")
        return redirect("login")

    return render(request, "blog/signup.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = AuthenticationForm(request=request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("dashboard")
        messages.error(request, "Invalid username or password.")

    return render(request, "blog/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")


@login_required
def dashboard_view(request):
    form = TopicForm(request.POST or None)
    generated_blog = None
    if request.method == "POST" and form.is_valid():
        topic = form.cleaned_data["topic"]
        try:
            content = generate_blog_content(topic)
            title = extract_title(content, fallback=topic)
            content = format_blog_content(content)
            generated_blog = Blog.objects.create(user=request.user, title=title, content=content)
            messages.success(request, "Blog generated and saved successfully.")
            form = TopicForm()
        except Exception as exc:
            messages.error(request, f"Could not generate blog: {exc}")

    return render(
        request,
        "blog/dashboard.html",
        {"form": form, "generated_blog": generated_blog},
    )


@login_required
def blog_list_view(request):
    blogs = Blog.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "blog/blog_list.html", {"blogs": blogs})


@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, pk=id, user=request.user)
    if request.method == "POST":
        blog.delete()
        messages.success(request, "Blog deleted successfully.")
        return redirect("my_blogs")
    messages.error(request, "Invalid request for deleting the blog.")
    return redirect("my_blogs")


@login_required
def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk, user=request.user)
    return render(
        request,
        "blog/blog_detail.html",
        {"blog": blog, "content": blog.content},
    )
