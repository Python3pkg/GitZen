from django.db import models

class Association(models.Model):
    git = models.IntegerField()
    zen = models.IntegerField()
    notes = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Z%s->G%s' % (self.zen, self.git)
