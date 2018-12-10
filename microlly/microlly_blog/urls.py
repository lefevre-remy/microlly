from django.urls import path
from microlly_blog import views

app_name = 'microlly_blog'
urlpatterns = [
    path('', views.index, name ='index'),
    path('create/', views.post_create, name='create'),
    path('post_user/<str:author>', views.list_post_user, name='list_post_user'),
    path('edit/<int:pk>', views.post_edit, name='edit'),
    path('delete/<int:pk>', views.post_delete, name='delete'),
    path('post/<int:pk>', views.post_details, name = 'details'),
]