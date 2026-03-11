from django import forms
from skills.models import Skill, HelpRequest


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


class AddHelpRequestForm(forms.ModelForm):
    """
    Formulaire permettant à un utilisateur de créer une nouvelle demande d'aide.
    """

    # Champ de sélection pour la compétence
    skill = forms.ModelChoiceField(
        queryset=Skill.objects.all(),
        label="Compétence requise",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Champ pour la date avec un sélecteur de date
    date = forms.DateField(
        label="Date de l'activité/service",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = HelpRequest
        fields = ['skill', 'date', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
