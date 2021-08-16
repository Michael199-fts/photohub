# Generated by Django 3.2 on 2021-07-30 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photoload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='rate',
        ),
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='photoload.post', verbose_name='Пост'),
        ),
    ]