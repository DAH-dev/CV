from django.contrib import admin
from .models import Personne, Experience, Formation, Competence, Langue, Contact, CV, Loisir

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    # Champs affichés dans la liste des CVs
    list_display = ['title', 'personne', 'user', 'design', 'contact_info', 'get_experiences', 'get_formations']
    
    # Champs pour filtrer
    list_filter = ['design', 'personne__nom']
    
    # Champs éditables directement depuis la liste
    list_editable = ['design']
    
    # Champs de recherche
    search_fields = ['title', 'personne__nom', 'personne__prenom', 'contact__telephone']
    
    # Méthode pour afficher les informations de contact
    def contact_info(self, obj):
        return obj.contact.telephone if obj.contact else "Non renseigné"
    contact_info.short_description = 'Téléphone'

    # Méthode pour afficher les expériences associées
    def get_experiences(self, obj):
        experiences = obj.experiences.all()
        return ", ".join([exp.titre for exp in experiences]) if experiences else "Aucune"
    get_experiences.short_description = 'Expériences'

    # Méthode pour afficher les formations associées
    def get_formations(self, obj):
        formations = obj.formations.all()
        return ", ".join([formation.diplome for formation in formations]) if formations else "Aucune"
    get_formations.short_description = 'Formations'


# Enregistrement des autres modèles avec une personnalisation minimale
@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'date_naissance', 'user']
    search_fields = ['nom', 'prenom']
    list_filter = ['date_naissance']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['titre', 'entreprise', 'date_debut', 'date_fin', 'user']
    search_fields = ['titre', 'entreprise']
    list_filter = ['date_debut', 'date_fin']

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ['diplome', 'institution', 'date_debut', 'date_fin', 'user']
    search_fields = ['diplome', 'institution']
    list_filter = ['date_debut', 'date_fin']

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ['nom', 'niveau', 'user']
    search_fields = ['nom']
    list_filter = ['niveau']

@admin.register(Langue)
class LangueAdmin(admin.ModelAdmin):
    list_display = ['langue', 'niveau', 'user']
    search_fields = ['langue']
    list_filter = ['niveau']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'telephone', 'adresse', 'user']
    search_fields = ['email', 'telephone']

@admin.register(Loisir)
class LoisirAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description', 'user']
    search_fields = ['nom']
