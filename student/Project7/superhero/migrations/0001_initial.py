# Generated by Django 5.1.1 on 2024-10-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('identity', models.CharField(max_length=200)),
                ('description', models.TextField(default='None')),
                ('image', models.ImageField(default='default.jpg', upload_to='heroes/')),
                ('strengths', models.CharField(default='None', max_length=200)),
                ('weaknesses', models.CharField(default='None', max_length=200)),
            ],
        ),
    ]
