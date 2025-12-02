---
title: "Site événementiel - Salon de l'Agriculture"
description: "Projet académique de création d'un site web événementiel pour la gestion du Salon de l'Agriculture avec système multi-rôles"
technologies: ["Node.js", "Express", "Sequelize", "PostgreSQL", "HTML/CSS", "JavaScript", "Bootstrap"]
date: 2024-04-04
image: "/images/salon_agriculutre.png"
githubUrl: "https://github.com/baptisteDULIEUX/salon-de-l-agriculture/tree/main"
featured: false
ordre: 2
---

## Contexte du projet

Projet réalisé dans le cadre d'une SAE (Situation d'Apprentissage et d'Évaluation) du BUT Informatique en équipe de 5 étudiants.

**Équipe** : Jean-Baptiste FROEHLY, Baptiste DULIEUX, Timothée MEYER, James GENITRINI, Hugues ESTRADE  
**Encadrants** : Stéphane DOMAS, Joseph AZAR, Fabrice AMBERT  
**Contexte** : Salon de l'Agriculture - événement international accueillant des milliers de visiteurs et des dizaines de prestataires

### Enjeux du projet
- **Enjeux écologiques** : Promouvoir une vision positive de l'agriculture durable
- **Enjeux économiques** : Faciliter les échanges commerciaux entre prestataires et visiteurs
- **Enjeux de dynamisation** : Améliorer l'attractivité et la communication autour de l'événement

## Objectifs et fonctionnalités

### Objectifs principaux
- Réaliser un site web événementiel complet pour le Salon de l'Agriculture
- Gérer l'événement depuis plusieurs points de vue (visiteur, prestataire, administrateur)
- Promouvoir le salon en France et à l'international
- Permettre une meilleure communication entre tous les acteurs
- Donner une vision positive de l'agriculture à travers le design et le contenu

### Vision design
- **Esthétique attrayante** : Page d'accueil soignée avec identité visuelle forte
- **Storytelling** : Récit sur les métiers de l'agriculture pour valoriser le secteur
- **Accessibilité** : Interface intuitive adaptée à tous les profils d'utilisateurs

## Fonctionnalités développées

### 1. Système d'authentification multi-rôles
Gestion sécurisée des accès selon le profil utilisateur :

- **Inscription** : Possibilité de s'enregistrer en tant que visiteur ou prestataire
- **Connexion** : Authentification sécurisée avec JWT (JSON Web Token)
- **Gestion des rôles** : 
  - Visiteur : Accès aux informations du salon et inscription aux activités
  - Prestataire : Gestion de stand et de stocks
  - Administrateur : Contrôle complet du site et des données
- **Sécurité** : Routes protégées avec middleware d'authentification, accès bloqué selon les rôles

### 2. Espace Visiteur
Fonctionnalités pour le grand public :

- **Consultation des prestataires** : Accès aux informations détaillées sur chaque stand
- **Découverte des activités** : Liste des événements et animations du salon
- **Inscription aux activités** : Réservation en ligne pour les ateliers et démonstrations
- **Système d'avis** : Possibilité de laisser des commentaires et notes sur les prestataires
- **Carte interactive** : Visualisation de l'emplacement des stands sur le plan du salon

### 3. Espace Prestataire
Dashboard dédié aux exposants :

- **Gestion du stand** : Visualisation de l'emplacement attribué
- **Gestion des stocks** : 
  - Ajout/suppression de produits à présenter
  - Mise à jour des prix et descriptions
  - Consultation du catalogue en temps réel
  - *Note* : La vente se fait en physique, le site sert uniquement de vitrine
- **Gestion des activités** : Création et organisation d'événements sur le stand
- **Liste des participants** : Accès aux visiteurs inscrits aux activités proposées
- **Consultation des avis** : Suivi de la satisfaction client via les commentaires
- **Système de tickets** : Demande d'assistance technique aux administrateurs

### 4. Espace Administrateur
Panel de contrôle complet :

- **Dashboard analytique** : Vue d'ensemble avec statistiques clés
  - Nombre de visiteurs inscrits
  - Nombre de prestataires
  - Activités les plus populaires
  - Indicateurs de fréquentation
- **Gestion des utilisateurs** : 
  - Liste complète des visiteurs et prestataires
  - Modification des informations
  - Activation/désactivation de comptes
- **Gestion de la carte interactive** : 
  - Modification du plan du salon
  - Attribution des emplacements de stands
  - Mise à jour des zones (restauration, animations, etc.)
- **Gestion des événements** : Validation et mise en avant des activités
- **Support technique** : Traitement des tickets de demande d'assistance

### 5. Carte interactive
Fonctionnalité phare pour l'orientation des visiteurs :

- Visualisation du plan complet du salon
- Localisation des stands par prestataire
- Zones thématiques (alimentation, machines agricoles, élevage, etc.)
- Informations détaillées au clic sur chaque stand
- Version mobile-friendly avec zoom et navigation tactile

## Technologies utilisées

### Backend
- **Node.js** : Environnement d'exécution JavaScript côté serveur
- **Express.js** : Framework web minimaliste et flexible pour Node.js
- **Sequelize** : ORM (Object-Relational Mapper) pour PostgreSQL
  - Modélisation des données simplifiée
  - Gestion automatique des migrations
  - Relations entre tables facilitées
- **JWT (JSON Web Token)** : Authentification stateless et sécurisée
- **bcrypt** : Hachage des mots de passe pour la sécurité

### Base de données
- **PostgreSQL** : Système de gestion de base de données relationnelle
- **Modèle de données évolutif** : 
  - Tables principales : Stand, Prestataire, Event, Localisation, Stock, User, Avis, Ticket
  - Relations complexes avec cardinalités 1-N et N-N
  - Évolution du modèle au cours du projet (voir diagrammes)

### Frontend
- **HTML5/CSS3** : Structure et stylisation des pages
- **JavaScript** : Interactivité et communication avec l'API
- **Bootstrap** : Framework CSS pour un design responsive
- **Fetch API** : Requêtes asynchrones vers le backend

### Outils de développement
- **Git & GitHub** : Gestion de versions et collaboration en équipe
- **Postman** : Tests des endpoints API
- **DBeaver** : Administration de la base de données PostgreSQL
- **VS Code** : Environnement de développement intégré

## Architecture technique

### Architecture MVC (Model-View-Controller)
```
Backend (Node.js + Express)
├── Models (Sequelize)
│   ├── User.js
│   ├── Prestataire.js
│   ├── Stand.js
│   ├── Event.js
│   └── ...
├── Controllers
│   ├── authController.js
│   ├── prestataireController.js
│   └── ...
├── Routes
│   ├── authRoutes.js
│   ├── prestataireRoutes.js
│   └── ...
└── Middlewares
    ├── authMiddleware.js
    └── roleMiddleware.js

Frontend
├── Public
│   ├── index.html
│   ├── prestataire.html
│   └── admin.html
├── Assets
│   ├── css/
│   └── js/
└── Images
```

### API RESTful
Endpoints principaux :
- `POST /api/auth/register` - Inscription
- `POST /api/auth/login` - Connexion
- `GET /api/prestataires` - Liste des prestataires
- `GET /api/prestataires/:id` - Détail d'un prestataire
- `GET /api/events` - Liste des événements
- `POST /api/events/:id/register` - Inscription à un événement
- `GET /api/stands` - Carte des stands
- `POST /api/stocks` - Ajout de stock (prestataire)
- `GET /api/admin/dashboard` - Statistiques (admin)

## Modèle de données

### Évolution du modèle Sequelize

Le modèle de données a évolué au cours du projet pour s'adapter aux besoins :

#### Version initiale (mi-projet)
Modèle complexe avec de nombreuses tables :
- User, Prestataire, Stock, Event, Location
- PaymentHistory, Notation, Ticket, Schedule
- Groupe, JournalUtilisateur

**Problème identifié** : Trop de tables pour un MVP (Minimum Viable Product), complexité excessive pour le temps imparti.

#### Version finale (simplifiée)
Focus sur les fonctionnalités essentielles :
- **Stand** : Informations sur les emplacements
- **Prestataire** : Données des exposants
- **Event** : Activités et animations
- **Localisation** : Coordonnées géographiques sur la carte
- **Stock** : Produits présentés par les prestataires (avec prix ajouté pour visualisation)
- **Avis** : Commentaires des visiteurs
- **Ticket** : Support technique (types de tickets ajoutés)

**Avantages** :
- Modèle simple mais flexible
- Modification facile des relations entre modèles
- Développement plus rapide
- Maintenance facilitée

### Relations principales
```
Stand (1) ---- (N) Prestataire
Stand (1) ---- (N) Localisation
Prestataire (1) ---- (N) Stock
Prestataire (1) ---- (N) Event
```

## Mon rôle dans le projet

En tant que **membre de l'équipe de développement**, j'ai contribué à :

- ✅ Conception de la base de données avec Sequelize
- ✅ Développement de l'API REST (routes et controllers)
- ✅ Implémentation du système d'authentification JWT
- ✅ Création des modèles Sequelize et gestion des relations
- ✅ Développement du dashboard prestataire
- ✅ Tests et débogage des fonctionnalités backend
- ✅ Collaboration via Git avec résolution de conflits

### Organisation du travail en équipe
- **Méthodologie** : Agile avec sprints hebdomadaires
- **Répartition** : Chaque membre responsable de modules spécifiques
- **Communication** : Réunions quotidiennes + Discord pour le suivi
- **Outils collaboratifs** : Git avec branches par fonctionnalité, pull requests pour validation

## Défis rencontrés et solutions

### 1. Complexité initiale du modèle de données
**Problème** : Première version trop ambitieuse avec trop de tables et de relations, risque de ne pas terminer dans les délais.

**Solution** : 
- Révision du modèle à mi-parcours
- Priorisation des fonctionnalités essentielles (MVP)
- Simplification des relations entre tables
- Résultat : Gain de temps significatif et meilleure maintenabilité

### 2. Coordination de l'équipe
**Problème** : 5 développeurs travaillant simultanément sur la même base de code, risque de conflits Git importants.

**Solution** :
- Adoption d'un workflow Git clair (GitFlow)
- Branches par fonctionnalité avec nommage cohérent
- Code reviews obligatoires avant merge
- Communication constante sur les modifications

### 3. Synchronisation frontend-backend
**Problème** : Équipes frontend et backend travaillant en parallèle, difficultés d'intégration.

**Solution** :
- Documentation de l'API dès le début
- Tests avec Postman pour valider les endpoints
- Mock data côté frontend pour ne pas bloquer le développement
- Intégration progressive module par module

### 4. Gestion des rôles et permissions
**Problème** : Sécuriser l'accès aux routes selon les rôles utilisateurs (visiteur/prestataire/admin).

**Solution** :
- Création de middlewares d'authentification et d'autorisation
- Vérification du JWT et du rôle à chaque requête sensible
- Messages d'erreur explicites (401 Unauthorized, 403 Forbidden)

## Résultats et apprentissages

### Compétences techniques acquises
- **Travail en équipe** : Collaboration sur un projet complexe à 5 développeurs
- **Architecture backend** : Conception d'une API REST complète et cohérente
- **ORM Sequelize** : Maîtrise de la modélisation et des relations
- **Authentification** : Implémentation de JWT et gestion des rôles
- **Git avancé** : Workflow collaboratif, résolution de conflits, pull requests
- **Gestion de projet** : Méthode agile, priorisation des tâches

### Compétences professionnelles
- **Communication** : Échanges quotidiens avec l'équipe et les encadrants
- **Adaptabilité** : Révision du modèle de données à mi-projet
- **Esprit critique** : Remise en question des choix initiaux pour optimiser
- **Organisation** : Respect des deadlines avec répartition efficace des tâches

### Points forts du projet
✅ Application fonctionnelle répondant au cahier des charges  
✅ Système multi-rôles sécurisé et robuste  
✅ Modèle de données flexible et évolutif  
✅ Expérience de travail en équipe réussie  
✅ Documentation technique complète  

## Évolutions possibles

### Fonctionnalités additionnelles
- [ ] **Paiement en ligne** : Intégration Stripe pour la vente de billets
- [ ] **Notifications** : Système d'alertes par email/SMS pour les événements
- [ ] **Chat en direct** : Messagerie entre visiteurs et prestataires
- [ ] **Application mobile** : Version native iOS/Android avec React Native
- [ ] **Tableau de bord analytique avancé** : Graphiques interactifs avec Chart.js
- [ ] **Système de recommandation** : Suggestions de stands selon les intérêts

### Améliorations techniques
- [ ] **Tests automatisés** : Jest pour le backend, Cypress pour le frontend
- [ ] **CI/CD** : Pipeline d'intégration continue avec GitHub Actions
- [ ] **Docker** : Conteneurisation pour faciliter le déploiement
- [ ] **Migration vers TypeScript** : Typage statique pour plus de robustesse
- [ ] **API GraphQL** : Alternative à REST pour des requêtes plus flexibles
- [ ] **Cache Redis** : Optimisation des performances pour les requêtes fréquentes

## Retour d'expérience

### Ce qui a bien fonctionné
✅ **Simplification du modèle** : Décision courageuse mais payante  
✅ **Communication d'équipe** : Réunions quotidiennes efficaces  
✅ **Documentation** : API bien documentée dès le début  
✅ **Méthodologie agile** : Sprints courts et itératifs adaptés au projet  

### Ce que nous améliorerions
🔄 **Planification initiale** : Mieux estimer la complexité dès le début  
🔄 **Tests unitaires** : Les intégrer dès le développement  
🔄 **Design UI/UX** : Consacrer plus de temps à l'expérience utilisateur  
🔄 **Performances** : Optimiser les requêtes SQL plus tôt dans le projet  

## Conclusion

Ce projet SAE m'a permis de **développer une application web complète en équipe**, avec une véritable réflexion sur l'architecture et la gestion d'un événement complexe. L'expérience de travailler à 5 sur un projet ambitieux m'a appris l'importance de la **communication, de l'organisation et de l'adaptabilité**.

La révision du modèle de données à mi-parcours démontre notre capacité à **prendre du recul et à ajuster notre approche** face aux contraintes. Cette décision a été clé pour livrer une application fonctionnelle dans les délais.

Ce projet représente également ma première expérience significative de **développement backend avec Node.js et Sequelize**, compétences que j'ai pu approfondir lors de mon stage S4.

---

**Projet réalisé dans le cadre** : SAE BUT Informatique S3/S4  
**Établissement** : IUT Nord Franche-Comté  
**Équipe** : 5 étudiants  
**Technologies** : Node.js, Express, Sequelize, PostgreSQL