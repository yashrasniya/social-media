# Generated by Django 3.1.1 on 2021-06-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_comment',
            field=models.ManyToManyField(null=True, related_name='comments', to='home_page.PostComments'),
        ),
    ]