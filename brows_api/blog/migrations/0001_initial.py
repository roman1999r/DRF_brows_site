# Generated by Django 4.0 on 2021-12-27 10:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Категорія фото',
                'verbose_name_plural': 'Категорії фото',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='CategoryPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Категорія поста',
                'verbose_name_plural': 'Категорії постів',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=255, unique=True, verbose_name='Url')),
                ('name', models.CharField(max_length=255)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=255, unique=True, verbose_name='Url')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='workphotos', to='blog.categoryphoto')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=255, unique=True, verbose_name='Url')),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.categorypost')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пости',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=255, unique=True, verbose_name='Url')),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('name', models.TextField(max_length=255)),
                ('number', models.TextField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('instagram', models.CharField(max_length=255)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event', to='blog.procedure')),
            ],
        ),
    ]
