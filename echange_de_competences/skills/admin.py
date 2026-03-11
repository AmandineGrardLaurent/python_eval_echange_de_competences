from django.contrib import admin

from skills.models import Skill, UserSkill, HelpRequest


class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "skill_name")


class UserSkillAdmin(admin.ModelAdmin):
    list_display = ("id", "user__username", "skill__skill_name")


class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "skill__skill_name", "requester__username", "helper__username", "date")


admin.site.register(Skill, SkillAdmin)
admin.site.register(UserSkill, UserSkillAdmin)
admin.site.register(HelpRequest, HelpRequestAdmin)
