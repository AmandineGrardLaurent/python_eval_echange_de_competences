from django.views import generic

from skills.models import HelpRequest


class AllHelpRequestPlannedView(generic.ListView):
    """
    Vue listant toutes les demandes d'aide ayant déjà un aidant (helper)
    et un demandeur (requester) assignés.
    """
    template_name = "help-requests-planned.html"
    context_object_name = "help_request_planned"

    def get_queryset(self):
        # Récupère les demandes où le demandeur ET l'aidant ne sont pas nuls.
        return HelpRequest.objects.filter(requester__isnull=False, helper__isnull=False).select_related('requester',
                                                                                                        'helper',
                                                                                                        'skill')
