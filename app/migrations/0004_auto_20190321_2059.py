# Generated by Django 2.1.5 on 2019-03-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_article_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(default='C', help_text='记录论坛文章的标题', max_length=255, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(default='C', help_text='记录论坛文章内容', verbose_name='内容'),
        ),
    ]