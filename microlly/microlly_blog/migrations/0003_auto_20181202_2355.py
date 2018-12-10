# Generated by Django 2.1.3 on 2018-12-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microlly_blog', '0002_auto_20181122_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-release_date'], 'verbose_name': 'Publication', 'verbose_name_plural': 'Publications'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]