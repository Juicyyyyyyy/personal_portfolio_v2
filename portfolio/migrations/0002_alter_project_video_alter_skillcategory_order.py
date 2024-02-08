# Generated by Django 5.0.2 on 2024-02-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='skillcategory',
            name='order',
            field=models.IntegerField(unique=True),
        ),
    ]