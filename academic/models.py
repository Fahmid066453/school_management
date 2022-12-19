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


class Teachers(models.Model):
    name = models.CharField(max_length=100)
    expert_in_sub= models.CharField(max_length=50, blank=True, null=True)
    phone_number= models.CharField(max_length=20)
    joining_date= models.DateField()
    active_status= models.BooleanField()

    class Meta:
        verbose_name_plural = 'teachers'

    def __unicode__(self):
        return u"%s's Info" % self.name
