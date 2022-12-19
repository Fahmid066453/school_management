from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    st_class = models.CharField(max_length=100, blank=True)
    section = models.CharField(max_length=50)
    roll = models.IntegerField(max_length=3)
    age = models.IntegerField(max_length=3)

    class Meta:
        verbose_name_plural = 'students'

    def __unicode__(self):
        return u"%s's Info" % self.name