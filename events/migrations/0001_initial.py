# Generated by Django 4.1.5 on 2023-01-31 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('description', models.TextField()),
                ('eventImage', models.ImageField(blank=True, upload_to='images/')),
                ('category', models.CharField(choices=[('Music', 'Music'), ('Cinema', 'Cinema'), ('Sport', 'Sport')], max_length=8)),
                ('state', models.BooleanField(default=False)),
                ('nbrParticipants', models.IntegerField(default=0)),
                ('eventDate', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
