from django.db import models


class BilibiliSubscription(models.Model):

    id = models.AutoField(
        primary_key=True
    )
    user_id = models.CharField(
        max_length=32, null=False, blank=False
    )
    group_id = models.CharField(
        max_length=32, null=False, blank=False
    )
    bilibili_id = models.CharField(
        max_length=32, null=False, blank=False
    )

    class Meta:
        db_table = "bilibili_subscription"
        unique_together = ('user_id', 'group_id', 'bilibili_id')