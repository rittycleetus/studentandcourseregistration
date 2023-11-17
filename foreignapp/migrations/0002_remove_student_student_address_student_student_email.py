# Generated by Django 4.2.6 on 2023-11-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreignapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_address',
        ),
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
