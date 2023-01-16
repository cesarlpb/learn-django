from django.contrib import admin
from .models import Member
import uuid

class MemberAdmin(admin.ModelAdmin):
  
  list_display = ("id", "firstname", "lastname", "phone", "joined_date", "slug")
  prepopulated_fields = {"slug": ("firstname", "lastname", "slug_hash")}

admin.site.register(Member, MemberAdmin)