# Generated by Django 4.0.5 on 2022-06-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApi', '0003_remove_comment_comment_blog_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
