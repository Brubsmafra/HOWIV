# Generated by Django 3.2.8 on 2021-11-01 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_assist_necessity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assist',
            old_name='address',
            new_name='endereco',
        ),
        migrations.RenameField(
            model_name='assist',
            old_name='telephone',
            new_name='telefone',
        ),
    ]
