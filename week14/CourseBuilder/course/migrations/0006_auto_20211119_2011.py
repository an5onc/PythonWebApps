# Generated by Django 3.2.7 on 2021-11-19 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='book',
            new_name='course',
        ),
        migrations.AlterField(
            model_name='image',
            name='folder',
            field=models.CharField(default='course', max_length=100),
        ),
    ]
