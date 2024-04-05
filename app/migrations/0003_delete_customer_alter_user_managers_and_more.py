# Generated by Django 5.0.2 on 2024-03-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_user_customer_delete_vehicles"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Customer",
        ),
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="user",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="user",
            name="email",
        ),
        migrations.RemoveField(
            model_name="user",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_admin",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_cashier",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_staff",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_superuser",
        ),
        migrations.RemoveField(
            model_name="user",
            name="last_login",
        ),
        migrations.RemoveField(
            model_name="user",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="password",
        ),
        migrations.RemoveField(
            model_name="user",
            name="user_permissions",
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=100),
        ),
    ]