from django.contrib import admin
from NSLCMOperationOccurrences.models import *

admin.site.register(NsLcmOpOcc)
admin.site.register(ResourceChanges)
admin.site.register(AffectedVnf)
admin.site.register(AffectedVirtualLink)
admin.site.register(AffectedVnffg)
admin.site.register(AffectedNs)
admin.site.register(AffectedSap)
admin.site.register(Links)
admin.site.register(ChangedInfo)
admin.site.register(ModifyVnfInfoData)
admin.site.register(ExtVirtualLinkInfo)
admin.site.register(ExtLinkPortInfo)
admin.site.register(ResourceHandle)
# Register your models here.
