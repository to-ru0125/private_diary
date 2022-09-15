from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name="blog.html"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry_b"),
]
