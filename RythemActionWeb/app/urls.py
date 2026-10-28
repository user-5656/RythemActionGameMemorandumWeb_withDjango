from django.urls import path
from django.urls import path,include
from django.contrib import admin

from . import views


app_name = 'app'

urlpatterns = [
    path('index/', views.showall, name='index'),
    path('', views.post_list, name='post_list'),
    path('001/', views.page_001, name='page_1'),
    path("admin/", admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path("posts/", views.post_list, name="post_list"),
]