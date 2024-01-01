from django import forms
from mot.models import Mot

# Create your models here.
"""Formulaire lié à la classe Modèle Mot"""
class AjouterMotForm(forms.ModelForm):
    class Meta:
        model=Mot
        # Si l'on veut que notre formulaire contient tous les champs du modèle, on fera fields = "__all__"
        fields = "__all__"

        # Personnalisation des champs du formulaire
        labels={
            'orthographe':'Orthographe du mot:',
            'signification':'Donnez la signification du mot:',
            'traduction_ang':'Traduction anglaise du mot:',
            'traduction_mat':'Traduction maternelle du mot:',
            'context':'Contexte d\'utilisation du mot:',
            'exemple':'Exemple d\'utisation du mot:'
        }
        
        widgets={
            'orthographe':forms.TextInput(attrs={'placeholder': 'Ex: Bonjour'}),
            'signification':forms.Textarea(attrs={'rows':3, 'cols':10, 'placeholder':'Ex: Bonjour mon ami'}),
            'traduction_ang':forms.TextInput(attrs={'placeholder': 'Ex: Good morning'}),
            'traduction_mat':forms.TextInput(attrs={'placeholder': 'Ex: Mbembe kiri'}),
            'context':forms.TextInput(attrs={'placeholder':'Ex: Salutations'}),
            'exemple': forms.Textarea(attrs={'rows':3, 'cols':10, 'placeholder':'Ex: Bonjour mon ami'})
        }

class RechercherMotForm(forms.Form):
    mot_recherche = forms.CharField(max_length=100, required=True)

