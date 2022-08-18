from django.db import models

class InstaHP(models.Model):
    location = models.CharField(max_length=15)
    url = models.URLField("인스타 페이지 주소")
    def __str__(self):
    	return f"장소 : {self.location}, 해당 게시물 url : {self.url}"
