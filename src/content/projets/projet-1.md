---
title: "Stage S4 - Application de gestion RH"
description: "Développement d'une application web full-stack pour la gestion des ressources humaines chez SAS Financière The Box"
technologies: ["Vue.js 2", "Quasar", "Node.js", "PostgreSQL", "Sequelize", "Swagger", "Ubuntu Server", "Raspberry Pi"]
date: 2024-06-15
image: "/images/image_stage.png"
featured: true
ordre: 1
---

## Contexte du projet

Réalisé lors de mon stage de 2ème année (S4) à la **SAS Financière The Box** d'avril à juin 2025, ce projet avait pour objectif de concevoir, réaliser et déployer une application web hybride de gestion des ressources humaines.

L'entreprise, société holding détenant la SAS Laurthy (entreprise de débit de boissons), souhaitait moderniser sa gestion du personnel en remplaçant les processus manuels par des outils numériques efficaces.

## Problématique

Les employés n'avaient accès qu'à leurs téléphones ou tablettes, tandis que les employeurs préféraient utiliser un ordinateur. Il fallait donc développer une solution compatible avec trois plateformes différentes (Android, iOS, ordinateur) sans multiplier les développements.

**Solution retenue** : Application web hybride accessible via navigateur sur toutes les plateformes.

## Objectifs et fonctionnalités

### Objectifs principaux
- Moderniser la gestion RH de l'entreprise
- Faciliter la communication entre employés et employeurs
- Automatiser les tâches répétitives et chronophages
- Améliorer le suivi des horaires et des services

### Fonctionnalités développées

#### 1. Système de gestion de planning
- **Pointage horaire** : Système permettant aux employés d'enregistrer leurs heures d'arrivée et de départ
- **Historique** : Consultation de l'historique des horaires mensuels
- **Validation** : Approbation des horaires par la direction

#### 2. Gestion des RTT
Outil permettant aux employés et employeurs de suivre et comprendre les jours de RTT (Réduction du Temps de Travail) :
- Calcul automatique des RTT acquis
- Visualisation du solde de RTT
- Demande et validation de prise de RTT

#### 3. Outil de clôture de caisse
Fonctionnalité majeure permettant de gagner du temps sur la fermeture quotidienne :

**Formules de calcul implémentées** :
```
Écart cartes = Somme TPE - Ventes en cartes
Ventes espèces = Balance - Fond de caisse
Écart espèces = Écart total - Écart cartes
Écart total = Ventes espèces - (Balance - Fond de caisse)
```

- Saisie des différents montants (billets, pièces, TPE)
- Calcul automatique des écarts
- Génération de rapports de clôture

#### 4. Système de tickets
Communication interne facilitée entre employés et direction :
- Création de tickets (demandes, problèmes, suggestions)
- Suivi de l'état des tickets
- Système de notifications

#### 5. Gestion des événements
Publication d'informations importantes pour l'ensemble du personnel (changements d'horaires, annonces, etc.)

## Technologies utilisées

### Frontend
- **Quasar Framework** : Framework permettant de créer des applications web hybrides avec une seule base de code
- **Vue.js 2** : Framework JavaScript pour des interfaces réactives, dynamiques et modulaires
- **Design responsive** : Interface adaptée aux mobiles, tablettes et ordinateurs

### Backend
- **Node.js** : Environnement d'exécution JavaScript côté serveur
- **Express** : Framework web pour Node.js, gestion des routes API REST
- **Sequelize** : ORM (Object-Relational Mapper) permettant d'interagir avec la base de données sans écrire de SQL brut
- **Swagger** : Documentation automatique de l'API REST

### Base de données
- **PostgreSQL** : Système de gestion de base de données relationnelle robuste et performant
- **Modèle relationnel** : Conception d'un MCD (Modèle Conceptuel de Données) complet avec :
  - Table Serveur (employés)
  - Table Service (journées de travail)
  - Table Événements
  - Table Tâches
  - Table Historique horaires mensuels
  - Relations et cardinalités optimisées

### Déploiement
- **Raspberry Pi 5 (8Go)** : Serveur auto-hébergé pour minimiser les coûts
- **Ubuntu Server** : Système d'exploitation Linux stable et sécurisé
- **Apache** : Serveur web pour servir l'application
- **SSD externe** : Stockage rapide et fiable

### Sécurité
- **Firewall** : Filtrage des connexions entrantes et sortantes
- **Hachage des mots de passe** : Protection des données sensibles (bcrypt)
- **Ports non conventionnels** : SSH configuré sur un port personnalisé pour réduire les attaques

## Architecture technique

### Architecture Full-Stack
```
┌─────────────────┐      ┌──────────────┐
│   Frontend      │ ───► │   Backend    │
│                 │      │              │
│  Vue.js/Quasar │ ◄─── │  Node.js API │
│                 │      │              │
└─────────────────┘      └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │  PostgreSQL  │
                         │   Database   │
                         └──────────────┘
```

### Architecture de l'application
- **app.vue** : Point d'entrée de l'application
- **Router** : Gestion de la navigation entre les pages
- **Pages** : Vues principales (planning, clôture, tickets, etc.)
- **Composants** : Éléments réutilisables de l'interface
- **Services** : Couche de communication avec l'API

## Défis rencontrés et solutions

### 1. Manque d'organisation initiale
**Problème** : Difficulté à prioriser les tâches et à estimer le temps nécessaire pour chaque fonctionnalité.

**Solution** : Mise en place d'un système de gestion de projet (Trello) avec découpage des tâches en sprints hebdomadaires. Utilisation de la méthode agile pour s'adapter aux changements de priorités.

### 2. Être le seul informaticien
**Problème** : Pas de collègue développeur pour échanger, relire le code ou partager les connaissances.

**Solution** : 
- Documentation exhaustive du code et de l'architecture
- Veille technologique active (forums, documentation officielle)
- Auto-formation continue sur les technologies utilisées
- Tests rigoureux pour compenser l'absence de code review

### 3. Problèmes de déploiement
**Problème** : Configuration complexe du Raspberry Pi, problèmes de performance initiaux, difficultés avec les permissions et la sécurité.

**Solution** :
- Optimisation des requêtes SQL avec Sequelize
- Mise en cache côté serveur pour réduire la charge
- Configuration fine d'Apache et du pare-feu
- Monitoring des performances avec des outils Linux

### 4. Incompatibilité entre frontend et backend
**Problème** : Liaison entre Vue.js et Node.js non finalisée dans les temps impartis.

**Solution prévue** : 
- Création d'une couche de services dédiée
- Utilisation d'Axios pour les appels HTTP
- Gestion centralisée des erreurs et des tokens d'authentification

## Mon rôle

En tant que **stagiaire développeur full-stack unique**, j'ai été responsable de :

- ✅ Analyse complète des besoins avec la direction
- ✅ Conception de la base de données (MCD, MLD)
- ✅ Développement du backend (API REST) : **95% terminé**
- ✅ Développement du frontend (interface utilisateur) : **90% terminé**
- 🔄 Liaison frontend-backend : **0% (prévu après le stage)**
- 🔄 Déploiement sur Raspberry Pi : **40% (configuration partielle)**
- ✅ Documentation technique complète (Swagger)
- ✅ Tests unitaires et fonctionnels

## Résultats et apprentissages

### Compétences techniques acquises
- **Full-Stack Development** : Maîtrise complète d'une stack JavaScript moderne
- **Vue.js & Quasar** : Création d'applications web hybrides performantes
- **Node.js & Express** : Développement d'API REST robustes
- **PostgreSQL & Sequelize** : Modélisation et gestion de bases de données relationnelles
- **Linux & Administration système** : Configuration de serveurs, sécurité, déploiement
- **Documentation** : Utilisation de Swagger pour documenter une API

### Compétences professionnelles
- **Autonomie** : Gestion complète d'un projet de A à Z
- **Communication** : Échanges réguliers avec les utilisateurs finaux et la direction
- **Adaptation** : Flexibilité face aux demandes changeantes
- **Résolution de problèmes** : Debugging et recherche de solutions autonome
- **Gestion du temps** : Priorisation des tâches dans un contexte de délais serrés

### Points forts du projet
✅ Application répondant aux besoins réels de l'entreprise  
✅ Interface intuitive adaptée aux différents profils d'utilisateurs  
✅ Architecture scalable et maintenable  
✅ Coût minimal grâce à l'auto-hébergement  
✅ Documentation complète facilitant la reprise du projet  

## Évolutions possibles

### Court terme (à finaliser)
- [ ] Liaison complète frontend-backend avec Axios
- [ ] Finalisation du déploiement sur Raspberry Pi
- [ ] Tests d'acceptation utilisateur (UAT)
- [ ] Formation du personnel à l'utilisation de l'application

### Moyen terme (améliorations)
- [ ] Notifications push pour les événements importants
- [ ] Export des données en Excel/PDF
- [ ] Tableau de bord statistiques pour la direction
- [ ] Application mobile native (React Native)

### Long terme (extensions)
- [ ] Module de gestion des congés payés
- [ ] Système de messagerie interne
- [ ] Intégration avec le logiciel de paie
- [ ] Module de gestion des stocks (bar)

## Retour d'expérience

### Ce que je referais
- ✅ Utilisation de Vue.js et Node.js (stack JavaScript cohérente)
- ✅ Documentation continue pendant le développement
- ✅ Tests réguliers avec les utilisateurs finaux
- ✅ Auto-hébergement pour maîtriser l'infrastructure

### Ce que je changerais
- 🔄 **Vue.js 3** au lieu de Vue.js 2 (plus moderne, meilleures performances)
- 🔄 **TypeScript** au lieu de JavaScript (typage statique, moins d'erreurs)
- 🔄 **Meilleure organisation** : Kanban dès le début du projet
- 🔄 **Tests automatisés** : Jest pour le backend, Cypress pour le frontend
- 🔄 **Docker** : Conteneurisation pour faciliter le déploiement

## Conclusion

Ce stage m'a permis de développer une **application full-stack complète et fonctionnelle**, répondant à un besoin réel d'entreprise. Malgré les défis rencontrés (travail en solo, contraintes techniques), j'ai réussi à livrer un produit quasi-finalisé (backend à 95%, frontend à 90%).

L'expérience acquise en tant que **seul développeur sur le projet** m'a forcé à développer mon autonomie, ma capacité d'organisation et ma polyvalence technique. J'ai également appris l'importance de la **communication avec les utilisateurs** et de l'**adaptabilité** face aux changements de priorités.

Ce projet représente une réalisation dont je suis fier, car elle aura un impact concret sur le quotidien des employés de l'entreprise une fois finalisée.

---

**Stage réalisé à** : SAS Financière The Box (Belfort, 90)  
**Durée** : 3 mois (Avril - Juin 2025)  
**Encadrant** : Vincent MARMIER  
**Technologies** : Vue.js, Quasar, Node.js, PostgreSQL, Raspberry Pi