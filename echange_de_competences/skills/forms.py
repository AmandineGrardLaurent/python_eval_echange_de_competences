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

        # Liste des champs du modèle à inclure dans le formulaire
        fields = ['skill', 'date', 'description']

        # Personnalisation de l'affichage des champs
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Initialise le formulaire en filtrant les compétences,
        on n'affiche que celles que l'utilisateur ne possède pas encore.
        """
        # On récupère l'utilisateur passé par la vue
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            # On cherche les ids des compétences présentes dans UserSkill pour cet utilisateur
            user_skill_ids = user.skills.values_list('skill_id', flat=True)

            # On exclut ces compétences de la liste déroulante
            self.fields['skill'].queryset = Skill.objects.exclude(id__in=user_skill_ids).order_by('skill_name')
