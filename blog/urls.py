from . import views
from django.urls import path

urlpatterns = [
    path('',views.HomePage.as_view(),name = 'home'),
    path('browse',views.PostList.as_view(),name = 'bloglist'),
    path('share_post',views.SharePost.as_view(),name = 'share_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('edit_post/<int:pk>', views.EditPost.as_view(), name='edit_post'),
    path('post/<int:post_id>/like/',views.PostLike.as_view(),name='post_like'),
    path('news',views.NewsPage.as_view(),name='news_page')
]