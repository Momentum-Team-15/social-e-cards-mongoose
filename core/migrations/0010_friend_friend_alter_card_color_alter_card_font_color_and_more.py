# Generated by Django 4.1.3 on 2022-11-20 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_card_color_alter_card_font_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('DARKRED', 'DARKRED'), ('BLACK', 'BLACK'), ('ORANGE', 'ORANGE'), ('PURPLE', 'PURPLE'), ('BLUE', 'BLUE'), ('GRAY', 'GRAY'), ('GREEN', 'GREEN'), ('RED', 'RED'), ('YELLOW', 'YELLOW'), ('GOLD', 'GOLD')], default='WHITE', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='font_color',
            field=models.CharField(choices=[('DARKRED', 'DARKRED'), ('BLACK', 'BLACK'), ('ORANGE', 'ORANGE'), ('PURPLE', 'PURPLE'), ('BLUE', 'BLUE'), ('GRAY', 'GRAY'), ('GREEN', 'GREEN'), ('RED', 'RED'), ('YELLOW', 'YELLOW'), ('GOLD', 'GOLD')], default='BLACK', max_length=50),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='core.card'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]