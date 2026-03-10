from django.views import generic

from skills.models import Skill


class AllSkillsView(generic.ListView):
    template_name = "skill_list.html"
    context_object_name = "skill_list"

    def get_queryset(self):
        return Skill.objects.order_by("skill_name")
