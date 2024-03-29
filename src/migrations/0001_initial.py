# Generated by Django 2.2 on 2021-04-17 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
                ('salt', models.CharField(default='', max_length=16)),
                ('name', models.CharField(default='', max_length=200)),
                ('type', models.IntegerField(default=0)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UsersToken',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('access_token', models.CharField(db_index=True, max_length=40, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Users', unique=True)),
            ],
            options={
                'db_table': 'users_access_token',
            },
        ),
    ]
