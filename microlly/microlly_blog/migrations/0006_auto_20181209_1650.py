# Generated by Django 2.1.3 on 2018-12-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microlly_blog', '0005_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
