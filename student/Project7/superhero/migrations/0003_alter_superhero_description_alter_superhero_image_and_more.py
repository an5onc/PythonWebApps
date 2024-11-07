# Generated by Django 5.1.1 on 2024-10-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superhero', '0002_alter_superhero_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='description',
            field=models.TextField(blank=True, default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='strengths',
            field=models.CharField(blank=True, default=' ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='weaknesses',
            field=models.CharField(blank=True, default=' ', max_length=200, null=True),
        ),
    ]
