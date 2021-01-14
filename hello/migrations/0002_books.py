# Generated by Django 3.1.4 on 2021-01-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50, verbose_name='書籍名')),
                ('publisher', models.CharField(max_length=50, verbose_name='出版社')),
                ('page', models.CharField(max_length=50, verbose_name='ページ')),
            ],
        ),
    ]
