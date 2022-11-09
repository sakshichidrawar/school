from django.contrib import admin
from school.models import firstclass,secondclass,thirdclass,fourthclass

# Register your models here.

class fadmin(admin.ModelAdmin):
    list_display=['stuname','stusurname','sturoll_no']
admin.site.register(firstclass,fadmin)

class sadmin(admin.ModelAdmin):
    list_display=['stuname','stusurname','sturoll_no']
admin.site.register(secondclass,sadmin)

class tadmin(admin.ModelAdmin):
    list_display=['stuname','stusurname','sturoll_no']
admin.site.register(thirdclass,tadmin)

class fadmin(admin.ModelAdmin):
    list_display=['stuname','stusurname','sturoll_no']
admin.site.register(fourthclass,fadmin)
