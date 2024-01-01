from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView, FormView, View
from django.urls import reverse_lazy, reverse
from .models import Mot
from .forms import AjouterMotForm, RechercherMotForm

# Create your views here.
"""Ajouter un mot un dictionnaire"""
class CreateMotView(CreateView):
    # Le modèle dont on va se servir pour créer un mot en BD
    model = Mot
    # Formulaire lié au modèle Mot
    form_class = AjouterMotForm
    # le template rendu
    template_name = "mot/ajouter.html"
    # redirection en cas de création d'un mot avec succès
    success_url = reverse_lazy("mot:add")

    # Pour envoyer des variables à notre template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Enregistrer"
        context["messages"] = "Mot ajouter avec succès !!!"
        return context

    """Validation du formulaire"""
    def form_valid(self, form):
        return super().form_valid(form)

"""Rechercher un mot"""
class SearchMotView(TemplateView):
    # Le modèle dont on va se servir pour créer un mot en BD
    model = Mot
    # template rendu
    template_name = "mot/rechercher.html"
    # contexte
    context_object_name = 'mots'
    message = ""

    def get(self, request, *args, **kwargs):
        if self.request.method == 'GET':
            mot_recherche = self.request.GET.get('mot_cherche', '')
            self.mot_trouve = Mot.objects.filter(orthographe__icontains=mot_recherche)
            if not self.mot_trouve:
                self.message = f"Le terme '{mot_recherche}' n'existe pas dans le dictionnaire"
                print(self.message)
            else:
                self.message = 'Mot retrouvé'
                print(self.message)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(resultat=self.mot_trouve, message=self.message, **kwargs)

class EditMotView(UpdateView):
    # Le modèle dont on va se servir pour modifier un mot en BD
    model = Mot
    # Formulaire lié au modèle Mot
    form_class = AjouterMotForm
    # template rendu
    template_name = "mot/modifier.html"
    # redirection en cas de création d'un mot avec succès
    success_url = reverse_lazy("mot:search")

    # Pour envoyer des variables à notre template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Sauvegarder"
        context["messages"] = "Mot modifié avec succès !!!"
        return context


