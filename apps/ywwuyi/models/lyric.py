from django.db import models

class Lyric(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        max_length=32, null=False, blank=False
    )
    singer = models.CharField(
        max_length=32, null=False, blank=False
    )
    lyric = models.CharField(
        max_length=4096, null=False, blank=False
    )
    url = models.CharField(
        max_length=256, null=False, blank=False
    )

    class Meta:
        db_table = 'mqmmw_lyric'