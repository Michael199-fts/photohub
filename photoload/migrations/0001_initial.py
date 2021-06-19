# Generated by Django 3.2 on 2021-06-17 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото поста')),
                ('raters', models.SmallIntegerField(default=0, verbose_name='Число оценщиков')),
                ('sum_rate', models.SmallIntegerField(default=0, verbose_name='Сумма оценок')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('upload_date', models.DateTimeField(verbose_name='Время загрузки')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=40, verbose_name='Имя пользователя')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail пользователя')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Аватар')),
                ('id_user', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Value_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.SmallIntegerField(verbose_name='Оценка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoload.user', verbose_name='Автор оценки')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoload.post', verbose_name='Пост')),
            ],
        ),
        migrations.CreateModel(
            name='Value_comm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.SmallIntegerField(verbose_name='Оценка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoload.user', verbose_name='Автор оценки')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoload.post', verbose_name='Комментарий')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoload.user', verbose_name='Автор фото'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300, verbose_name='Текст комментария')),
                ('raters', models.SmallIntegerField(default=0, verbose_name='Число оценщиков')),
                ('sum_rate', models.SmallIntegerField(default=0, verbose_name='Сумма оценок')),
                ('upload_date', models.DateTimeField(verbose_name='Время написания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoload.user', verbose_name='Автор комментария')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoload.post', verbose_name='Пост')),
            ],
        ),
    ]
