from django.db import models

class URLData(models.Model):
    url = models.URLField(max_length=2000)
    domain_name = models.CharField(max_length=255)
    protocol = models.CharField(max_length=10)
    title = models.CharField(max_length=500, null=True, blank=True)
    images = models.JSONField(default=list)
    stylesheets_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
