# Generated by Django 3.1.3 on 2020-11-14 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('benefits', models.CharField(max_length=1000)),
                ('desc', models.CharField(max_length=1000)),
                ('edu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policy.education')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policy.state')),
            ],
        ),
    ]