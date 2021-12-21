# Generated by Django 2.2.19 on 2021-12-21 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211220_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='text',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
