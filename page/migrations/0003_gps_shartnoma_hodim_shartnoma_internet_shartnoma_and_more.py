# Generated by Django 4.1.6 on 2023-02-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_dastur_shartnoma'),
    ]

    operations = [
        migrations.AddField(
            model_name='gps',
            name='shartnoma',
            field=models.FileField(blank=True, null=True, upload_to='shartnoma'),
        ),
        migrations.AddField(
            model_name='hodim',
            name='shartnoma',
            field=models.FileField(blank=True, null=True, upload_to='shartnoma'),
        ),
        migrations.AddField(
            model_name='internet',
            name='shartnoma',
            field=models.FileField(blank=True, null=True, upload_to='shartnoma'),
        ),
        migrations.AddField(
            model_name='kamera',
            name='shartnoma',
            field=models.FileField(blank=True, null=True, upload_to='shartnoma'),
        ),
        migrations.AddField(
            model_name='kompyuter',
            name='shartnoma',
            field=models.FileField(blank=True, null=True, upload_to='shartnoma'),
        ),
        migrations.AddField(
            model_name='server',
            name='shartnoma',
            field=models.FileField(blank=True, null=True, upload_to='shartnoma'),
        ),
        migrations.AddField(
            model_name='wifi',
            name='shartnoma',
            field=models.FileField(blank=True, null=True, upload_to='shartnoma'),
        ),
    ]
