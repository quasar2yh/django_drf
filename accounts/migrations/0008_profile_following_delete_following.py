# Generated by Django 4.2 on 2024-05-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_user_self_introduction_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='followers', to='accounts.profile'),
        ),
        migrations.DeleteModel(
            name='Following',
        ),
    ]
