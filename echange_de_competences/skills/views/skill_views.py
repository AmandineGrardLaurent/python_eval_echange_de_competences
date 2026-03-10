from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from skills.models import Skill, UserSkill


class AllSkillsView(generic.ListView):
    """
    Vue permettant d'afficher toutes les compétences du site
    """
    template_name = "skill-list.html"
    context_object_name = "skill_list"

    def get_queryset(self):
        return Skill.objects.order_by("skill_name")


class UserSkillsListView(LoginRequiredMixin, generic.ListView):
    """
    Vue permettant d'afficher les compétences de l'utilisateur connecté
    """
    template_name = "my-skills.html"
    context_object_name = "my_skills_list"

    def get_queryset(self):
        # on récupère les compétences de l'utilisateur connecté
        return UserSkill.objects.filter(user=self.request.user).select_related("skill")
