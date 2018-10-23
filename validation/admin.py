from django.contrib import admin

from .models import AnchoringResult, Company, Data, Useful


class AnchoringResultAdmin(admin.ModelAdmin):
    list_display = ('result', 'version', 'created', )
    model = AnchoringResult
    ordering = ('version', )


admin.site.register(AnchoringResult, AnchoringResultAdmin)
admin.site.register(Company)
admin.site.register(Data)
admin.site.register(Useful)
