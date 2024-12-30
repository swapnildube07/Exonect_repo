# Generated by Django 4.0.1 on 2022-02-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assigned_at', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Assigned at')),
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='Title')),
                ('submission_date', models.DateField(blank=True, null=True, verbose_name='Submission Date')),
                ('message', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name of the User', max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, help_text='Last Name of the User', max_length=255, null=True, verbose_name='Last Name')),
                ('email_id', models.EmailField(help_text='Email ID of the User', max_length=1023, verbose_name='Email ID')),
                ('message', models.TextField(help_text='Message by the User', verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('code', models.PositiveSmallIntegerField(verbose_name='Subject code')),
            ],
            options={
                'unique_together': {('name', 'code')},
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=10, verbose_name='Grade')),
                ('section', models.CharField(blank=True, max_length=10, null=True, verbose_name='Section')),
            ],
            options={
                'unique_together': {('grade', 'section')},
            },
        ),
    ]