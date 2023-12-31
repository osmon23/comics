# Generated by Django 5.0 on 2023-12-11 19:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('author', models.CharField(max_length=255, verbose_name='Author')),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='Rating')),
            ],
            options={
                'verbose_name': 'Comic',
                'verbose_name_plural': 'Comics',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VALUE', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='Value')),
                ('comic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='comics.comic', verbose_name='Comic')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
