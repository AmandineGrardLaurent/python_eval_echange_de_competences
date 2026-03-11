from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import FormView

from skills.forms import AddUserSkillsForm
from skills.models import Skill, UserSkill


class AllSkillsView(generic.ListView):
    """
    Vue permettant d'afficher toutes les compétences du site
    """
    template_name = "skills/all-skills.html"
    context_object_name = "skill_list"

    def get_queryset(self):
        return Skill.objects.order_by("skill_name")


class UserSkillListView(LoginRequiredMixin, generic.ListView):
    """
    Vue permettant d'afficher les compétences de l'utilisateur connecté
    """
    template_name = "skills/my-skills.html"
    context_object_name = "my_skills_list"

    def get_queryset(self):
        # on récupère les compétences de l'utilisateur connecté
        return UserSkill.objects.filter(user=self.request.user).select_related("skill")


class UserSkillCreateView(LoginRequiredMixin, FormView):
    template_name = "skills/my-skills-add.html"
    form_class = AddUserSkillsForm
    success_url = reverse_lazy('skills:my-skills')

    def get_initial(self):
        """
        Cette méthode définit les valeurs cochées par défaut à l'affichage du formulaire.
        """
        initial = super().get_initial()

        # On récupère les ids des compétences que l'utilisateur a déjà
        current_skills_ids = UserSkill.objects.filter(
            user=self.request.user
        ).values_list('skill_id', flat=True)

        # On pré-remplit le champ 'skills' avec ces ids
        initial['skills'] = list(current_skills_ids)
        return initial

    def form_valid(self, form):
        """
        Cette méthode est appelée uniquement si le formulaire est valide
        """
        # Récupère la liste des objets 'Skill' (nettoyés et validés) cochés dans le formulaire
        selected_skills = form.cleaned_data['skills']

        # On supprime les anciennes compétences de l'utilisateur
        UserSkill.objects.filter(user=self.request.user).delete()

        # On recrée les nouvelles compétences (celles qui sont restées cochées)
        # Ainsi l'utilisateur peut supprimer des compétences qui étaient enregistrées et en ajouter de nouvelles
        for skill in selected_skills:
            UserSkill.objects.create(user=self.request.user, skill=skill)

        return super().form_valid(form)
