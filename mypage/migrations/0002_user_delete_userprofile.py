# Generated by Django 5.0 on 2023-12-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('tel', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]