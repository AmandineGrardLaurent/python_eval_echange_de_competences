1️. **Consulter les activités planifiées**

- Acteur principal : Visiteur (ou utilisateur connecté)
- Pré-condition : L’utilisateur a accès à l’application.
- Description : 
  - L’utilisateur consulte les prochains créneaux où une aide a été proposée pour une activité.
  - Les utilisateurs impliqués ne sont pas identifiés.
- Résultat : L’utilisateur obtient la liste des activités planifiées et leurs créneaux.
- Règles métier : Les activités affichées ne doivent pas révéler les informations personnelles.

--- 
2️. **Consulter la liste des compétences**

- Acteur principal : Visiteur (ou utilisateur connecté)
- Pré-condition : L’utilisateur a accès à l’application.
- Description : L’utilisateur consulte l’ensemble des compétences disponibles pour échange dans le système.
- Résultat : La liste complète des compétences est affichée.
- Règles métier : Aucune compétence ne peut être modifiée ou ajoutée par le visiteur.

---

3️. **Indiquer ses compétences**

- Acteur principal : Utilisateur connecté
- Pré-condition : L’utilisateur est connecté.
- Description : L’utilisateur sélectionne dans la liste des compétences celles qu’il possède et qu’il est prêt à offrir.
- Résultat : Les compétences de l’utilisateur sont enregistrées dans le système. Il pourra accepter une demande d'aide correspondant à ses compétences.
- Règles métier : L’utilisateur ne peut sélectionner que des compétences présentes dans la liste des compétences du système.

---

4️. **Créer une demande d’aide**

- Acteur principal : Utilisateur connecté
- Pré-condition : L’utilisateur est connecté.
- Description : 
  - L’utilisateur choisit un créneau pour l’activité/le service.
  - Il sélectionne une compétence qu’il ne possède pas.
  - Il saisit une description libre de l’activité.
- Résultat :
  - La demande d’aide est publiée.
  - Chaque créneau est visible individuellement par les utilisateurs connectés possédant la compétence demandée.
- Règles métier :
  - La compétence choisie doit être absente du profil de l’utilisateur.
  - Chaque créneau correspond toujours à une journée entière.

---

5️. **Consulter les demandes d’aide compatibles**

- Acteur principal : Utilisateur connecté
- Pré-condition : L’utilisateur est connecté et possède au moins une compétence.
- Description : L’utilisateur consulte les demandes d’aide publiées par d’autres utilisateurs. Seules les demandes correspondant aux compétences de l’utilisateur sont affichées.
- Résultat : L’utilisateur voit uniquement les demandes compatibles avec ses compétences.
- Règles métier : 
  - Un utilisateur ne peut pas voir les demandes pour lesquelles il ne possède pas la compétence demandée.
  - Un utilisateur ne peut pas voir les demandes qu’il a lui-même publiées.

---

6️. **Accepter une demande d’aide**

- Acteur principal : Utilisateur connecté
- Pré-condition : L’utilisateur est connecté et possède la compétence demandée.
- Description :
  - L’utilisateur indique qu’il est disponible pour aider un autre utilisateur sur un créneau.
  - Le créneau est réservé et retiré de la liste des demandes disponibles.
  - La demande se transforme en activité planifiée.
- Résultat : 
  - La demande est planifiée et visible comme activité pour tous les utilisateurs connectés et les visiteurs.
- Règles métier :
  - Un utilisateur ne peut accepter qu’une demande correspondant à l’une de ses compétences.
  - Un créneau accepté devient réservé et ne peut plus être choisi par d’autres utilisateurs.

---

7️. **Consulter les coordonnées d’un utilisateur**

- Acteur principal : Utilisateur connecté
- Pré-condition : L’utilisateur est impliqué dans une activité planifiée avec un autre utilisateur.
- Description :
  - L’utilisateur peut voir le prénom, le nom et l’adresse email de l’autre utilisateur impliqué.
  - L’adresse email sert à organiser la rencontre.
- Résultat : Les informations sont visibles uniquement pour les deux utilisateurs impliqués dans l’activité.
- Règles métier : Les coordonnées ne sont accessibles que si une activité est planifiée.

---

8️. **Ajouter un utilisateur**

- Acteur principal : Administrateur
- Pré-condition : L’administrateur est connecté au système.
- Description : L’administrateur crée un nouvel utilisateur autorisé à se connecter à l’application.
- Résultat : L’utilisateur est enregistré et peut se connecter après création.
- Règles métier : Seul un administrateur peut créer un nouvel utilisateur.

---

9️. **Ajouter une compétence**

- Acteur principal : Administrateur
- Pré-condition : L’administrateur est connecté.
- Description : L’administrateur ajoute une nouvelle compétence dans la liste des compétences proposées.
- Résultat : La compétence est disponible pour tous les utilisateurs.
- Règles métier : Seul un administrateur peut ajouter une compétence.

--- 

10. **Se connecter**

- Acteur principal : Utilisateur
- Pré-condition : L’utilisateur possède un compte.
- Description : L’utilisateur saisit son identifiant et son mot de passe pour accéder à son espace.
- Résultat : L’utilisateur est authentifié et peut accéder aux fonctionnalités réservées.
- Règles métier : Seuls les utilisateurs enregistrés peuvent se connecter.
