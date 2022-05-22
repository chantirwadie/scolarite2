# Generated by Django 4.0.2 on 2022-05-06 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filliere', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('label', models.CharField(error_messages={'unique': 'label must be unique'}, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('filliere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filliere_module', to='filliere.filiere')),
            ],
        ),
    ]
