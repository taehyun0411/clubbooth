# Generated by Django 4.2.17 on 2024-12-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0012_article_remove_user_value그레이스_remove_user_value뉴턴_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="stocks",
        ),
        migrations.AlterField(
            model_name="user",
            name="money",
            field=models.DecimalField(decimal_places=0, default=1000000, max_digits=40),
        ),
    ]
