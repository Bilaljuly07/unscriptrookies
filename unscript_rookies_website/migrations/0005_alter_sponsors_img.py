# Generated by Django 4.1.5 on 2023-01-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unscript_rookies_website', '0004_alter_sponsors_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsors',
            name='img',
            field=models.ImageField(upload_to='images/pics'),
        ),
    ]
