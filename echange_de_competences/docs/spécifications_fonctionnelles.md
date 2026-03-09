# Spécifications fonctionnelles

## Visiteur 

Un visiteur (utilisateur non connecté) peut : 

1. **Consulter les activités déjà planifiées**  
   - Voir les prochains créneaux où une aide a été proposée et acceptée.  
   - L’affichage est **anonyme** : l’identité des utilisateurs impliqués n’est pas visible.

2. **Consulter la liste des compétences**  
   - Voir toutes les compétences proposées dans l’application.

---

## Utilisateur connecté (U1)

Un utilisateur connecté peut participer au système d’échange de compétences.  

1. **Indiquer ses compétences**
   - Sélectionner dans la liste des compétences celles : 
     - qu’il possède
     - qu’il est prêt à offrir.

2. **Créer une demande d’aide**  
   - Indiquer la compétence recherchée (qu’il ne possède pas).  
   - Fournir une description libre de l’activité.  
   - Choisir un créneau (journée entière) pour recevoir l’aide.

3. **Consulter les demandes d’aide compatibles**  
   - Afficher uniquement les demandes d'autres utilisateurs correspondant aux compétences possédées par U1.  

4. **Accepter une demande d’aide**  
   - Se rendre disponible pour aider un autre utilisateur sur un créneau.  
   - Conséquences : 
     - Le créneau n’est plus proposé aux autres utilisateurs.  
     - La demande devient une activité planifiée, visible par un visiteur.

5. **Consulter les coordonnées d’un utilisateur** 
   - Après qu’une activité est planifiée entre deux utilisateurs.  
   - Informations visibles : prénom, nom, adresse email.  
   - L’email permet de contacter l’autre utilisateur pour organiser la rencontre.

---

## Administrateur

1. Ajouter un utilisateur  
2. Ajouter une compétence