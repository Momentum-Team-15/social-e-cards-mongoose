# Generated by Django 4.1.3 on 2022-11-22 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_friend_friend_alter_card_color_alter_card_font_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('PURPLE', 'PURPLE'), ('ORANGE', 'ORANGE'), ('GREEN', 'GREEN'), ('GOLD', 'GOLD'), ('DARKRED', 'DARKRED'), ('YELLOW', 'YELLOW'), ('BLACK', 'BLACK'), ('RED', 'RED'), ('GRAY', 'GRAY'), ('BLUE', 'BLUE')], default='WHITE', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='font_color',
            field=models.CharField(choices=[('PURPLE', 'PURPLE'), ('ORANGE', 'ORANGE'), ('GREEN', 'GREEN'), ('GOLD', 'GOLD'), ('DARKRED', 'DARKRED'), ('YELLOW', 'YELLOW'), ('BLACK', 'BLACK'), ('RED', 'RED'), ('GRAY', 'GRAY'), ('BLUE', 'BLUE')], default='BLACK', max_length=50),
        ),
        migrations.AlterField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]