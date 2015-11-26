from django.db import models


class RandomCard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="upload")

    @classmethod
    def random_item(cls):
        return cls.objects.order_by('?')[0]

    def __unicode__(self):
        return self.title

    def link(self):
        if self.url:
            return self.url
        else:
            return "htpp://www.google.com/search?q=%s" % (self.title)

    def linked(self):
        return "<a href=\"%s\" title=\"%s\">%s</a>" % (self.link(), self.description, self.title)

    class Meta:
        abstract = True
