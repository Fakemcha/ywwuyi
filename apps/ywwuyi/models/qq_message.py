from django.db import models


class QQMessage(models.Model):

    id = models.AutoField(
        primary_key=True
    )
    subject = models.CharField(
        max_length=32, null=False, blank=False
    )
    user_id = models.CharField(
        max_length=32, null=False, blank=False
    )
    content = models.CharField(
        max_length=2048, null=False
    )
    type = models.CharField(
        max_length=16, null=False, blank=False
    )
    timestamp = models.BigIntegerField(
        null=False
    )

    class Meta:
        db_table = "qq_message"