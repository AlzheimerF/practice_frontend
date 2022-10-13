from django.urls import path
from . import views

urlpatterns = [
    path('news_list/', views.list_news, name='list_'),
    path('news_detail/<int:id>/', views.detail_news, name='detail_'),
    path('news_create/', views.create_news, name='create_'),
    path('news_update/<int:id>/', views.update_news, name='update_'),
    path('news_delete/<int:id>/', views.delete_news, name='delete_')
]