# Generated by Django 5.0.2 on 2024-02-07 16:14

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
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('short_description', models.CharField(blank=True, max_length=300, null=True)),
                ('content', models.TextField()),
                ('thumbnail_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('thumbnail_url', models.URLField(blank=True, null=True)),
                ('category', models.CharField(default='uncategorized', max_length=255)),
                ('slug', models.CharField(max_length=100)),
                ('time', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
