# Generated by Django 3.2.13 on 2022-10-06 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('issue_a', models.CharField(max_length=200)),
                ('issue_b', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick', models.CharField(choices=[('BLUE', 'BLUE'), ('RED', 'RED')], max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.vote')),
            ],
        ),
    ]
