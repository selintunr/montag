from django.contrib import admin

from webPage1.models import contactFormModel,contactFormModel2,staticAboutModel,staticAboutModel2, subFormModel,subFormModel2, referansi, referansi2
# Register your models here.


admin.site.register(staticAboutModel)
admin.site.register(contactFormModel)
admin.site.register(subFormModel)
admin.site.register(referansi)


admin.site.register(staticAboutModel2)
admin.site.register(contactFormModel2)
admin.site.register(subFormModel2)
admin.site.register(referansi2)