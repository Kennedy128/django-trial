# Generated by Django 3.0 on 2020-05-24 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default='category', on_delete=django.db.models.deletion.CASCADE, to='images.Category')),
                ('location', models.ForeignKey(default='location', on_delete=django.db.models.deletion.CASCADE, to='images.Location')),
            ],
        ),
    ]
