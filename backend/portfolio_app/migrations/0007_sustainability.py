# Generated by Django 5.0.6 on 2024-05-26 07:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_alter_skill_skill_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sustainability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sustainability_title', models.CharField(max_length=512, null=True)),
                ('sustainability_description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
