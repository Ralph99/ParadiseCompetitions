# Generated by Django 3.0.7 on 2020-06-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paradise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='title',
            field=models.CharField(default='Some Random Title', max_length=200),
            preserve_default=False,
        ),
    ]
