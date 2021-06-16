# Generated by Django 3.2 on 2021-06-16 13:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('sum_rating', models.IntegerField(default=0)),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2021, 6, 16, 16, 56, 20, 414597))),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=30)),
                ('raters', models.IntegerField(default=0)),
                ('sum_rating', models.IntegerField(default=0)),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2021, 6, 16, 16, 56, 20, 412597))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('id_user', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=1)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photoload.user')),
                ('target_com', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photoload.comment')),
                ('target_post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photoload.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoload.user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoload.user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoload.post'),
        ),
    ]