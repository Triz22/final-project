from . import views
from django.urls import path

urlpatterns = [
    path('',views.PostList.as_view(),name = 'bloglist'),
    path('share_post',views.SharePost.as_view(),name = 'share_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]