from django.db import models

# Create your models here.

class MultiModel(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=1024, null=True, blank=True, default='')
    content_fr = models.CharField(max_length=1024, null=True, blank=True, default='')
    content_de = models.CharField(max_length=1024, null=True, blank=True, default='')

    language = models.CharField(max_length=16, null=False, blank=False)

    def save(self, *args, **kwargs):
            return super(MultiModel, self).save(*args, **kwargs)
 
    def __unicode__(self):
        return "{}:{}".format(self.content, self.language)
