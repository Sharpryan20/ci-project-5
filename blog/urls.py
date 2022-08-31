from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]