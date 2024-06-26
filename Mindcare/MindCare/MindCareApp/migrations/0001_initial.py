# Generated by Django 3.2.23 on 2024-02-14 09:55

from django.db import migrations, models

def insert_user_data(apps, schema_editor):
    User = apps.get_model('MindCareApp', 'User')
    # Add your data insertion logic here
    User.objects.create(
        user_type='admin',
        name='Admin',
        contact='1234567890',
        email='admin@example.com',
        password='admin',
        address='admin address',
    )

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(error_messages={'unique': 'This contact number is already exist.'}, max_length=50, unique=True)),
                ('email', models.EmailField(error_messages={'unique': 'This email address is already exist.'}, max_length=100, unique=True)),
                ('password', models.CharField(default=None, max_length=10)),
                ('image', models.ImageField(default=None, upload_to='user/')),
                ('address', models.TextField(default=None)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_enabled', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.RunPython(insert_user_data),

    ]
