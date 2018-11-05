# Generated by Django 2.1.3 on 2018-11-05 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('title', models.CharField(max_length=50, unique=True)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=5000000)),
                ('blog_id', models.IntegerField(db_column='blog_id', primary_key=True, serialize=False)),
                ('star_num', models.IntegerField(default=0)),
                ('reply_num', models.IntegerField(default=0)),
                ('watch_num', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]