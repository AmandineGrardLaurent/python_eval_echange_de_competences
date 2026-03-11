from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views import generic

from skills.models import HelpRequest, UserSkill


class AllHelpRequestPlannedView(generic.ListView):
    """
    Vue listant toutes les demandes d'aide ayant déjà un aidant (helper)
    et un demandeur (requester) assignés.
    """
    template_name = "skills/help-requests-planned.html"
    context_object_name = "help_request_planned"

    def get_queryset(self):
        # Récupère les demandes où le demandeur ET l'aidant ne sont pas nuls.
        return (HelpRequest.objects
                .filter(requester__isnull=False, helper__isnull=False)
                .select_related('requester', 'helper', 'skill'))


class AllHelpRequestBySkillView(LoginRequiredMixin, generic.ListView):
    """
    Vue listant les demandes d'aide en attente dont la compétence correspond
    au profil de l'utilisateur connecté et dont la date n'est pas passée.
    """
    template_name = "skills/help-requests-matching-skills.html"
    context_object_name = "help_requests"

    def get_queryset(self):
        # Liste des ids des compétences de l'utilisateur
        user_skill_ids = (UserSkill.objects
                          .filter(user=self.request.user)
                          .values_list('skill_id', flat=True))

        # La date du jour pour exclure les dates passées
        today = timezone.now().date()

        # On filtre la liste en fonction des critères suivants :
        # - la correspondance des compétences
        # - sans aidant (donc non planifié)
        # - date >= aujourd'hui
        return (HelpRequest.objects
                .filter(skill_id__in=user_skill_ids)
                .filter(helper__isnull=True)
                .filter(date__gte=today)
                .select_related('requester', 'skill')
                .order_by('date'))
