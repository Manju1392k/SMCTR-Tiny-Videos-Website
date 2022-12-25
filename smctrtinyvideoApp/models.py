from django.db import models

# Create your models here.
class TinyVideo(models.Model):
    TinyVideo_Tittle = models.CharField(max_length=20)
    TinyVideo_Video = models.FileField(upload_to="tinyvideos")
    Time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.TinyVideo_Tittle