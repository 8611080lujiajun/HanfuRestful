# Generated by Django 2.1.9 on 2019-07-20 15:11

import app.models
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
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='记录活动的标题', max_length=255, verbose_name='标题')),
                ('text', models.TextField(help_text='记录论坛活动内容', verbose_name='内容')),
                ('images', models.ImageField(help_text='记录活动封面图', upload_to=app.models.Activity.get_upload_to, verbose_name='封面图')),
                ('place', models.CharField(help_text='记录活动地点', max_length=255, verbose_name='活动地点')),
                ('verify', models.BooleanField(default=False, help_text='记录活动发布后[是否需要|是否完成]审核', verbose_name='审核')),
                ('start_date', models.DateTimeField(help_text='记录活动开始时间', verbose_name='开始时间')),
                ('end_date', models.DateTimeField(help_text='记录活动结束时间', verbose_name='结束时间')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='记录活动创建时间', verbose_name='创建时间')),
                ('change_date', models.DateTimeField(auto_now=True, help_text='记录活动更新时间', verbose_name='更新时间')),
                ('browse', models.IntegerField(default=0, help_text='记录活动浏览量', verbose_name='浏览量')),
                ('user', models.ForeignKey(help_text='记录活动创建作者', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity_user', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
        ),
        migrations.CreateModel(
            name='Activity_Attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='记录活动参加的时间', verbose_name='参加时间')),
                ('activity', models.ForeignKey(help_text='用户所参加的活动', on_delete=django.db.models.deletion.CASCADE, to='app.Activity', verbose_name='参加的活动')),
                ('user', models.ForeignKey(help_text='参加者', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='参加者')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='C', help_text='记录论坛文章的标题', max_length=255, verbose_name='标题')),
                ('text', models.TextField(default='C', help_text='记录论坛文章内容', verbose_name='内容')),
                ('images', models.ImageField(help_text='记录文章封面图', null=True, upload_to=app.models.Article.get_upload_to, verbose_name='封面图')),
                ('verify', models.BooleanField(default=False, help_text='记录文章发布后[是否需要|是否完成]审核', verbose_name='审核')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='记录文章创建时间', verbose_name='创建时间')),
                ('change_date', models.DateTimeField(auto_now=True, help_text='记录文章更新时间', verbose_name='更新时间')),
                ('browse', models.IntegerField(default=0, help_text='记录文章浏览量', verbose_name='浏览量')),
                ('user', models.ForeignKey(help_text='记录文章创建作者', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='user_attend',
            field=models.ManyToManyField(help_text='记录活动参加人员', related_name='activity_user_attend', through='app.Activity_Attend', to=settings.AUTH_USER_MODEL, verbose_name='报名人员'),
        ),
    ]