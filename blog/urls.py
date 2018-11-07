from django.urls import path
from . import views,blog_interface

urlpatterns = [
    #账号登录相关接口
    path('index', views.index, name='index'),
    path('register',views.register,name='register'),
    path('do_register', views.do_register),
    path('login', views.user_login, name='login'),
    path('do_login',views.do_user_login,name='do_login'),
    path('logout', views.user_logout, name='logout'),
    
    #博客相关接口
    path('<int:blog_id>/', blog_interface.get_blog, name="blogs"),
    path('add_blog',blog_interface.add_blog, name='add_blog'),
    path('do_add_blog',blog_interface.do_add_blog), 
    path('<int:blog_id>/edit_blog', blog_interface.edit_blog, name='edit_blog'),
    path('<int:blog_id>/do_edit_blog', blog_interface.do_edit_blog, name='do_edit_blog'),
    path('<int:blog_id>/delete_blog', blog_interface.delete_blog, name='delete_blog')
]