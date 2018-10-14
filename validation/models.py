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
