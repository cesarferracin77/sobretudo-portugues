# Generated by Django 4.0.3 on 2022-04-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0008_remove_article_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=65, null=True)),
                ('last_name', models.CharField(max_length=65, null=True)),
            ],
        ),
    ]
