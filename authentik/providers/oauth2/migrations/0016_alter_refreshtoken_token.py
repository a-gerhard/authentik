# Generated by Django 4.1.7 on 2023-05-06 16:18

from django.db import migrations, models

import authentik.providers.oauth2.models


class Migration(migrations.Migration):
    dependencies = [
        (
            "authentik_providers_oauth2",
            "0015_accesstoken_auth_time_authorizationcode_auth_time_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="refreshtoken",
            name="token",
            field=models.TextField(
                default=authentik.providers.oauth2.models.generate_client_secret
            ),
        ),
        migrations.AlterField(
            model_name="oauth2provider",
            name="sub_mode",
            field=models.TextField(
                choices=[
                    ("hashed_user_id", "Based on the Hashed User ID"),
                    ("user_id", "Based on user ID"),
                    ("user_uuid", "Based on user UUID"),
                    ("user_username", "Based on the username"),
                    (
                        "user_email",
                        "Based on the User's Email. This is recommended over the UPN method.",
                    ),
                    (
                        "user_upn",
                        "Based on the User's UPN, only works if user has a 'upn' attribute set. Use this method only if you have different UPN and Mail domains.",
                    ),
                ],
                default="hashed_user_id",
                help_text="Configure what data should be used as unique User Identifier. For most cases, the default should be fine.",
            ),
        ),
    ]