# Generated by Django 5.1 on 2024-10-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='taskaddmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=30)),
                ('Priority', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='add_task',
        ),
    ]
