# Troc & Astuces

Plateforme web pour échanger des compétences entre utilisateurs.  
Permet aux utilisateurs de proposer ou de demander de l’aide sur des activités variées, en fonction de leurs compétences.

---

## Fonctionnalités

- Affichage des compétences disponibles sur le site.
- Consultation des demandes d’aide planifiées et en cours.
- Gestion des compétences d’un utilisateur connecté.
- Création de nouvelles demandes d’aide.
- Proposer son aide pour des demandes existantes.
- Authentification : connexion/déconnexion.
- Interface stylisée avec Tailwind CSS.

---

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/AmandineGrardLaurent/python_eval_echange_de_competences.git
cd echhange_de_competences
```

2. Créer un environnement virtuel :

``` bash
python -m venv venv
venv\Scripts\activate
```

3. Installer les dépendances : 

``` bash
pip install -r requirements.txt
```

4. Appliquer les migrations : 

``` bash
python manage.py migrate
```

5. Créer un superutilisateur :

``` bash
python manage.py createsuperuser
```

---

## Développement

Pour travailler sur le projet, lancez ces deux commandes dans des terminaux séparés :

**Compilateur CSS**
``` bash
python manage.py tailwind start
```

**Serveur**
``` bash
python manage.py runserver
```

Accéder à l’application sur http://127.0.0.1:8000/skills/auth/login/

---

## Structure du projet

```
python_eval_echange_de_competences/
├─ echange_de_competences/
│  ├─ config/
│  ├─ docs/
│  ├─ skills/
│  │  ├─ migrations
│  │  ├─ templates
│  │  ├─ views
│  │  ├─ models.py
│  │  ├─ forms.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  ├─ tailwindtheme/
│  ├─ templates/
│  ├─ templates/
│  │  ├─ skills/
│  │  │  ├─ all_skills.html
│  │  │  ├─ my_skills.html
│  │  │  ├─ help_requests_planned.html
│  │  │  ├─ help_requests_detail.html
│  │  │  └─ add_help_request.html
│  ├─ manage.py
│  ├─ requirements.txt
│  └─ db.sqlite3

```
---
## Architecture des données

Le projet repose sur trois piliers :

- Skill : Le catalogue des savoir-faire.

- UserSkill : Table de liaison gérant les compétences acquises par chaque utilisateur.

- HelpRequest : Les annonces postées, reliant un demandeur, un potentiel aidant et une compétence.

---

## Technologies utilisées

- Python 3.13.7
- Django 5.2.12
- Tailwind CSS
- SQLite 
- django-browser-reload
