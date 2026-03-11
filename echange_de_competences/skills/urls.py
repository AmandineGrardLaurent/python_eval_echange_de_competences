from django.urls import path, include

from .views import skill_views, help_request_views

app_name = "skills"
urlpatterns = [
    # URL pour accéder à toutes les compétences
    path("all/", skill_views.AllSkillsView.as_view(), name="all-skills"),

    # URL pour accéder aux compétences de l'utilisateur connecté
    path("my/", skill_views.UserSkillListView.as_view(), name="my-skills"),

    # URL pour ajouter/retirer des compétences à l'utilisateur connecté
    path("my/add/", skill_views.UserSkillCreateView.as_view(), name="my-skills-add"),

    # URL pour l'authentification
    path('auth/', include('django.contrib.auth.urls')),

    # URL pour accéder aux demandes d'aide planifiées
    path("help/requests/planned/",
         help_request_views.AllHelpRequestPlannedView.as_view(),
         name="help-requests-planned"),

    # URL pour accéder aux demandes en lien avec les compétences de l'utilisateur connecté
    path("help/requests/matching-skills/",
         help_request_views.AllHelpRequestBySkillView.as_view(),
         name="help-requests-matching-skills")
]
