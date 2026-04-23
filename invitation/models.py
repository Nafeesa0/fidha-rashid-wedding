from django.db import models

class RSVPResponse(models.Model):
    name = models.CharField(max_length=200)
    response = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} – {self.response}"