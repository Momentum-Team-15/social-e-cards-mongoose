# Generated by Django 4.1.3 on 2022-11-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_card_color_alter_card_font_color'),
        ('core', '0017_alter_card_color_alter_card_font_color_and_more')
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('GRAY', 'GRAY'), ('RED', 'RED'), ('ORANGE', 'ORANGE'), ('YELLOW', 'YELLOW'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN'), ('PURPLE', 'PURPLE'), ('BLACK', 'BLACK'), ('GOLD', 'GOLD'), ('DARKRED', 'DARKRED')], default='WHITE', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='font_color',
            field=models.CharField(choices=[('GRAY', 'GRAY'), ('RED', 'RED'), ('ORANGE', 'ORANGE'), ('YELLOW', 'YELLOW'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN'), ('PURPLE', 'PURPLE'), ('BLACK', 'BLACK'), ('GOLD', 'GOLD'), ('DARKRED', 'DARKRED')], default='BLACK', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
