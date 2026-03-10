from django.urls import path, include

from .views import skill_views, help_request_views

app_name = "skills"
urlpatterns = [
    path("all-skills/", skill_views.AllSkillsView.as_view(), name="all-skills"),
    path("my-skills/", skill_views.UserSkillsListView.as_view(), name="my-skills"),
    path('auth/', include('django.contrib.auth.urls')),
    path("help-requests-planned/", help_request_views.AllHelpRequestPlannedView.as_view(), name="help-requests-planned"),
]
