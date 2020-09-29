from django.db import models


class Blog(models.Model):
	tital = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to='images/')
	body = models.TextField()
	