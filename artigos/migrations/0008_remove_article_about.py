# Generated by Django 4.0.3 on 2022-04-28 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0007_alter_article_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='about',
        ),
    ]