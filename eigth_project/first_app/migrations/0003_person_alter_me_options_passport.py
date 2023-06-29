# Generated by Django 4.2.2 on 2023-06-28 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_friend_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cities', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='me',
            options={'ordering': ['id']},
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_number', models.IntegerField()),
                ('page', models.IntegerField()),
                ('validity', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='first_app.person')),
            ],
        ),
    ]
