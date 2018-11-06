from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('logout', views.logout, name='logout'),
    path('<int:blog_id>/', views.get_blog, name="blogs"),
    path('add_blog',views.add_blog, name='add_blog'),
    path('<int:blog_id>/edit_blog', views.edit_blog, name='edit_blog'),
    path('<int:blog_id>/delete_blog', views.delete_blog, name='delete_blog')
]