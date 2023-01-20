from django.db import models

class ChatGptQuery(models.Model):
    model = models.CharField(max_length=20)
    prompt = models.TextField()
    tags = models.JSONField(default=dict)
    response = models.TextField()
    temperature = models.FloatField(default=0.5)
    max_tokens = models.IntegerField(default=20)
    top_p = models.FloatField(default=1)
    n = models.IntegerField(default=1)
    stream = models.BooleanField(default=False)
    logprobs = models.IntegerField(default=0)
    stop = models.CharField(max_length=1, default="")

    def __str__(self):
        return f"{self.prompt}"
