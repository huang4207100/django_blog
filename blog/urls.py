from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('register',views.register,name='register'),
    path('do_register', views.do_register),
    path('login', views.user_login, name='login'),
    path('do_login',views.do_user_login,name='do_login'),
    path('logout', views.user_logout, name='logout'),
    path('<int:blog_id>/', views.get_blog, name="blogs"),
    path('add_blog',views.add_blog, name='add_blog'),
    path('do_add_blog',views.do_add_blog), 
    path('<int:blog_id>/edit_blog', views.edit_blog, name='edit_blog'),
    path('<int:blog_id>/delete_blog', views.delete_blog, name='delete_blog')
]