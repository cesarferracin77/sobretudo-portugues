# Generated by Django 4.0.3 on 2022-04-28 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0006_article_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='link',
            field=models.URLField(max_length=250, null=True),
        ),
    ]
