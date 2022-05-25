# Generated by Django 2.2 on 2022-05-25 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfis', '0003_perfil_contatos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='email',
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
