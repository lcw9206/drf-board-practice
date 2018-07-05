from django.db import models


class Posting(models.Model):
    name = models.CharField(max_length=30, blank=False)
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name + ':' + self.title


class Comment(models.Model):
    posting = models.ForeignKey(Posting)
    name = models.CharField(max_length=30, blank=False)
    text = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name + ':' + self.text
