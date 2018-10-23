from django.db import models


class MetaMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AnchoringResult(MetaMixin):
    version = models.FloatField(verbose_name='Getoond gemiddelde')
    result = models.FloatField()


class AuthorityResult(MetaMixin):
    version = models.PositiveIntegerField(
        verbose_name='Getoond bedrijfsformaat')
    result = models.FloatField()


class Company(MetaMixin):
    name = models.CharField(max_length=64)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Data(MetaMixin):
    company = models.ForeignKey('validation.Company', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    
    def __str__(self):
        return '{} - {}'.format(self.company, self.title)


class Useful(MetaMixin):
    company = models.ForeignKey('validation.Company', on_delete=models.CASCADE)
    useful = models.BooleanField()

    def __str__(self):
        return '{} - {}'.format(self.company, self.useful)
