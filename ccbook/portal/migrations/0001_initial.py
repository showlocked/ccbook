# Generated by Django 2.0.5 on 2018-05-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('uni_uuid', models.CharField(max_length=40, unique=True)),
                ('create_time', models.CharField(max_length=40)),
                ('update_time', models.CharField(max_length=40)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('author', models.CharField(db_index=True, max_length=100)),
                ('url', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('uni_uuid', models.CharField(max_length=40, unique=True)),
                ('create_time', models.CharField(max_length=40)),
                ('update_time', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=225)),
                ('url', models.CharField(max_length=225)),
                ('aync_status', models.BooleanField(help_text='是否同步章节内容到数据库')),
            ],
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('uni_uuid', models.CharField(max_length=40, unique=True)),
                ('create_time', models.CharField(max_length=40)),
                ('update_time', models.CharField(max_length=40)),
                ('parent_uuid', models.CharField(db_index=True, max_length=40)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=225)),
            ],
        ),
    ]