# Generated by Django 3.2.6 on 2022-11-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0003_alter_restaurantes_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantes',
            name='telefone',
            field=models.TextField(),
        ),
    ]