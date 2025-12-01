---
title: "Stage S4 - Application de gestion RH"
description: "Développement d'une application web full-stack pour la gestion des ressources humaines chez SAS Financière The Box"
technologies: ["Vue.js 2", "Quasar", "Node.js", "PostgreSQL", "Sequelize", "Swagger", "Ubuntu Server", "Raspberry Pi"]
date: 2024-06-15
image: "/images/projets/stage-thebox.jpg"
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
- **Hachage des mots de passe** : Protection des données sensibles (bc