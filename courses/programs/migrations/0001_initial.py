# Generated by Django 2.1.3 on 2018-11-17 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('complete', models.BooleanField(default=False)),
                ('audio', models.URLField()),
                ('video', models.URLField()),
                ('article', models.URLField()),
                ('question', models.URLField()),
                ('form', models.URLField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('image', models.URLField(default='https://via.placeholder.com/150')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('progress', models.IntegerField(db_column='progress')),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('pages', models.ManyToManyField(to='programs.Page')),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='weeks',
            field=models.ManyToManyField(to='programs.Week'),
        ),
    ]
