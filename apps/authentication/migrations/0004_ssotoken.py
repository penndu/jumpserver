# Generated by Django 2.2.10 on 2020-07-31 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0003_loginconfirmsetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSOToken',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('authkey', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Token')),
                ('expired', models.BooleanField(default=False, verbose_name='Expired')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]