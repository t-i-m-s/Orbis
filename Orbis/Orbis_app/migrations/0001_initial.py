# Generated by Django 3.0 on 2021-02-24 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Essence',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('child', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Orbis_app.Essence')),
            ],
            options={
                'db_table': 'essence',
            },
        ),
    ]
