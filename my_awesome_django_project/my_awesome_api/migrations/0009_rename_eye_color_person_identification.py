# Generated by Django 3.2.5 on 2021-07-28 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_awesome_api', '0008_alter_pet_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='eye_color',
            new_name='identification',
        ),
    ]
