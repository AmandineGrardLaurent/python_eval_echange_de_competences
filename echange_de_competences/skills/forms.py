from django import forms
from skills.models import UserSkill, Skill


class AddUserSkillsForm(forms.Form):
    """
    Formulaire permettant de sélectionner et d'enregistrer plusieurs compétences
    via des cases à cocher
    """
    # Définition du champ de sélection multiple basé sur le modèle Skill
    skills = forms.ModelMultipleChoiceField(
        # On affiche toutes les compétences par défaut
        queryset=Skill.objects.all(),
        # On utilise un formulaire à choix multiples
        widget=forms.CheckboxSelectMultiple,
        label="Vos compétences :"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

