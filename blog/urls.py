from django.urls import path

from .views import (
    blog_detail_view,
    blog_list_view,
    dashboard_view,
    delete_blog,
    login_view,
    logout_view,
    signup_view,
)

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("blogs/", blog_list_view, name="blog_list"),
    path("my-blogs/", blog_list_view, name="my_blogs"),
    path("blogs/delete/<int:id>/", delete_blog, name="delete_blog"),
    path("blogs/<int:pk>/", blog_detail_view, name="blog_detail"),
]
