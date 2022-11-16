# Generated by Django 4.1.3 on 2022-11-16 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='card_msg',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('GRAY', 'GRAY'), ('PURPLE', 'PURPLE'), ('DARKRED', 'DARKRED'), ('GREEN', 'GREEN'), ('GOLD', 'GOLD'), ('RED', 'RED'), ('BLACK', 'BLACK'), ('ORANGE', 'ORANGE'), ('BLUE', 'BLUE'), ('YELLOW', 'YELLOW')], default='WHITE', max_length=50),
        ),
        migrations.AddField(
            model_name='card',
            name='font_color',
            field=models.CharField(choices=[('GRAY', 'GRAY'), ('PURPLE', 'PURPLE'), ('DARKRED', 'DARKRED'), ('GREEN', 'GREEN'), ('GOLD', 'GOLD'), ('RED', 'RED'), ('BLACK', 'BLACK'), ('ORANGE', 'ORANGE'), ('BLUE', 'BLUE'), ('YELLOW', 'YELLOW')], default='BLACK', max_length=50),
        ),
        migrations.AddField(
            model_name='card',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='favorite',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='core.card'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
