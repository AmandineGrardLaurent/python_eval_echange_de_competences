from django.urls import path

from .views import skill_views

app_name = "skills"
urlpatterns = [
    path("all_skills/", skill_views.AllSkillsView.as_view(), name="all_skill"),
]
