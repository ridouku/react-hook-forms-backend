# Generated by Django 3.2.5 on 2021-07-22 22:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('my_awesome_api', '0003_alter_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
