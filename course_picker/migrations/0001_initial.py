# Generated by Django 3.2.5 on 2021-07-26 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('special', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('FOMO', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('prof', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('specialisation', models.ForeignKey(blank=True, db_column='special', null=True, on_delete=django.db.models.deletion.CASCADE, to='course_picker.spec')),
            ],
        ),
        migrations.CreateModel(
            name='CourseContent',
            fields=[
                ('ID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('semester', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=50)),
                ('course_credits', models.CharField(max_length=50)),
                ('modality', models.CharField(max_length=5)),
                ('faculty', models.ForeignKey(blank=True, db_column='prof', null=True, on_delete=django.db.models.deletion.CASCADE, to='course_picker.prof')),
            ],
        ),
    ]
