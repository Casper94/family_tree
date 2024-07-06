from django.contrib import admin
from .models import FamilyMember

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'child_number', 'parent', 'spouse', 'sex', 'user')
    list_filter = ('sex', 'user')
    search_fields = ('name',)
    ordering = ('child_number', 'name')