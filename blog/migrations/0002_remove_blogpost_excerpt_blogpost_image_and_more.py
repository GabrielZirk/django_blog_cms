# Generated by Django 4.0.6 on 2022-07-08 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='excerpt',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, default='blogpost.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(editable=False, max_length=100, unique=True),
        ),
    ]
