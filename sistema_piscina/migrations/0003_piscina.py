# Generated by Django 5.2.1 on 2025-05-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_piscina', '0002_remove_usuario_username_usuario_nome_completo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piscina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
    ]
