# Generated by Django 5.1.7 on 2025-04-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manutentores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ni', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('abertura', models.DateTimeField()),
                ('fechamento', models.DateField()),
                ('status', models.CharField(choices=[('Aberto', 'Aberto'), ('Em andamento', 'Em andamento'), ('Fechado', 'Fechado')], default='Aberto', max_length=50)),
                ('prioridade', models.CharField(choices=[('Alta', 'Alta'), ('Média', 'Média'), ('Baixa', 'Baixa')], default='Baixa', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Patrimonios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ni', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100)),
                ('localizacao', models.CharField(max_length=50)),
            ],
        ),
    ]
