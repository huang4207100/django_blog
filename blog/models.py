from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #博客作者
    title = models.CharField(max_length=50, unique=True)   #博客题目
    publish_time = models.DateTimeField(auto_now_add=True) #博客创建时间
    update_time = models.DateTimeField(auto_now=True) #博客更新时间
    content = HTMLField() #博客内容
    blog_id = models.IntegerField(primary_key=True, db_column='blog_id')  #博客id
    star_num = models.IntegerField(default=0) #点赞数
    reply_num = models.IntegerField(default=0) #评论数
    watch_num = models.IntegerField(default=0) #查看数

    class Meta:
        db_table = "blog"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_id = models.IntegerField(primary_key=True, db_column='comment_id')
    father_id = models.IntegerField(default=0) #id默认为0，直接对blog的评论
    content = models.CharField(max_length=200)

    