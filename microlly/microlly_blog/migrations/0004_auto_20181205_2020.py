# Generated by Django 2.1.3 on 2018-12-05 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microlly_blog', '0003_auto_20181202_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Publication', 'verbose_name_plural': 'Publications'},
        ),
        migrations.AlterField(
            model_name='post',
            name='edit_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
