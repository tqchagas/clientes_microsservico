# Generated by Django 2.1.3 on 2018-11-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('f', 'Feminino'), ('m', 'Masculino')], max_length=1)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
    ]
