# Generated by Django 5.1.2 on 2024-10-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sustainability', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SustainabilityPractice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('benefits', models.TextField()),
                ('implementation_steps', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='SustainablePractice',
        ),
        migrations.RenameField(
            model_name='incentive',
            old_name='points',
            new_name='reward_points',
        ),
        migrations.RemoveField(
            model_name='incentive',
            name='title',
        ),
        migrations.AddField(
            model_name='incentive',
            name='criteria',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
