# Generated by Django 2.2 on 2020-10-12 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0017_hobby_hobby_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_email', models.CharField(max_length=200)),
                ('contact_message', models.CharField(max_length=200)),
            ],
        ),
    ]