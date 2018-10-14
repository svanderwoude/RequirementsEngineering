from django.contrib import admin

from .models import AnchoringResult


class AnchoringResultAdmin(admin.ModelAdmin):
    list_display = ('result', 'version', 'created', )
    model = AnchoringResult
    ordering = ('version', )


admin.site.register(AnchoringResult, AnchoringResultAdmin)
