# Generated by Django 4.2.7 on 2023-11-25 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(default='', max_length=20)),
                ('full_name', models.CharField(blank=True, max_length=35, null=True)),
                ('mobile_number', models.CharField(default='', max_length=15)),
                ('profile_image', models.ImageField(default='User/profile_image/default.jpg', null=True, upload_to='User/profile_image')),
                ('is_verified', models.BooleanField(default=False)),
                ('when_add', models.DateTimeField(auto_now_add=True)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
