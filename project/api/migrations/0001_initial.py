# Generated by Django 4.1.7 on 2023-04-21 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StreamInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sid', models.CharField(default=0, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('adult', models.BooleanField(default=False)),
                ('backdrop_path', models.CharField(blank=True, max_length=255, null=True)),
                ('belongs_to_collection', models.CharField(blank=True, max_length=255, null=True)),
                ('budget', models.IntegerField(blank=True, null=True)),
                ('homepage', models.CharField(blank=True, max_length=255, null=True)),
                ('imdb_id', models.CharField(blank=True, max_length=255, null=True)),
                ('original_language', models.CharField(max_length=255)),
                ('original_title', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('popularity', models.FloatField(blank=True, null=True)),
                ('poster_path', models.CharField(blank=True, max_length=255, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('revenue', models.IntegerField(blank=True, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('tagline', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('video', models.BooleanField(default=False)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('vote_count', models.IntegerField(blank=True, null=True)),
                ('rating', models.FloatField(default=0.0)),
                ('ratingcount', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('genres', models.ManyToManyField(to='api.genre')),
                ('streaminfo', models.ManyToManyField(to='api.streaminfo')),
            ],
        ),
    ]
