# Generated by Django 4.1.3 on 2022-11-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_card_color_alter_card_font_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('BLUE', 'BLUE'), ('BLACK', 'BLACK'), ('ORANGE', 'ORANGE'), ('GREEN', 'GREEN'), ('YELLOW', 'YELLOW'), ('PURPLE', 'PURPLE'), ('GOLD', 'GOLD'), ('RED', 'RED'), ('GRAY', 'GRAY'), ('DARKRED', 'DARKRED')], default='WHITE', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='font_color',
            field=models.CharField(choices=[('BLUE', 'BLUE'), ('BLACK', 'BLACK'), ('ORANGE', 'ORANGE'), ('GREEN', 'GREEN'), ('YELLOW', 'YELLOW'), ('PURPLE', 'PURPLE'), ('GOLD', 'GOLD'), ('RED', 'RED'), ('GRAY', 'GRAY'), ('DARKRED', 'DARKRED')], default='BLACK', max_length=50),
        ),
    ]
