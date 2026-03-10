from django.contrib.auth.models import User
from django.db import models


class Skill(models.Model):
    """
    Modèle représentant une compétence
    """
    skill_name = models.CharField(max_length=250)

    def __str__(self):
        return self.skill_name


class HelpRequest(models.Model):
    """
    Modèle représentant une demande d'aide

    Une demande d'aide comprend :
        - l'aidant (null par défaut car on ne le connaît pas lors de la création de la demande)
        - le demandeur
        - la compétence demandée
        - un descriptif de l'activité/service
        - le créneau
        - la date de publication
    """
    helper = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="help_requests_as_helper",
        null=True, blank=True)

    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="help_requests_as_requester")

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        helper = self.helper if self.helper else "Personne"
        return f"{self.description} - {self.skill} - {self.date} - Demandeur : {self.requester} - Aidant : {helper}"


class UserSkill(models.Model):
    """
    modèle représentant les compétences d'un utilisateur
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="skills")
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="users")

    class Meta:
        unique_together = ('user', 'skill')

    def __str__(self):
        return f"{self.user} a la compétence : {self.skill}"
