# Generated by Django 4.2.3 on 2023-07-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake_app', '0006_alter_customizedcake_decore_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customizedcake',
            name='inscription',
            field=models.TextField(blank=True, help_text='Мы можем разместить на торте любую надпись, например: «С днем рождения!»', max_length=15, null=True, verbose_name='Надпись на торте'),
        ),
        migrations.AlterField(
            model_name='readycake',
            name='inscription',
            field=models.TextField(blank=True, help_text='Мы можем разместить на торте любую надпись, например: «С днем рождения!»', max_length=15, null=True, verbose_name='Надпись на торте'),
        ),
    ]
