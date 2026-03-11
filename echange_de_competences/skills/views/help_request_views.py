from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.contrib import messages

from skills.forms import AddHelpRequestForm
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


class HelpRequestDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Vue permettant d'accéder à la page détaillée d'une demande d'aide
    et ainsi accéder aux coordonnées du demandeur
    """
    model = HelpRequest
    template_name = "skills/help-requests-detail.html"
    context_object_name = "help_request"

    def post(self, request, *args, **kwargs):
        """
        Cette méthode gère la confirmation d'aide d'un utilisateur sur une demande spécifique.
        Elle assigne l'utilisateur connecté comme 'helper' de la demande si aucun
        autre aidant n'est déjà enregistré.
        """
        # On récupère la demande d'aide actuelle
        help_request = self.get_object()

        # On vérifie si la demande n'a pas déjà un helper
        if help_request.helper is None:
            help_request.helper = request.user
            help_request.save()
            messages.success(request, "Bravo ! Vous êtes maintenant inscrit comme aidant.")
        else:
            messages.warning(request, "Désolé, quelqu'un a déjà proposé son aide pour cette demande.")

        # On redirige l'utilisateur sur la page des demandes planifiées
        return redirect('skills:help-requests-planned')


class HelpRequestCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Vue permettant à l'utilisateur connecté de créer une demande d'aide
    """
    model = HelpRequest
    form_class = AddHelpRequestForm
    template_name = "skills/help-requests-add.html"

    # Redirection vers la liste des compétences de l'utilisateur après succès
    success_url = reverse_lazy('skills:my-skills')

    def form_valid(self, form):
        """
        Cette méthode est appelée lorsque le formulaire est valide.
        Elle permet d'ajouter des données automatiques avant la sauvegarde.
        """
        # On injecte l'utilisateur actuellement connecté dans le champ 'requester'
        form.instance.requester = self.request.user

        # On appelle la méthode parente pour finaliser l'enregistrement et la redirection
        return super().form_valid(form)
