---
title: "[Nom du projet académique]"
description: "Projet réalisé en équipe dans le cadre du BUT Informatique"
technologies: ["PHP", "Symfony", "MySQL", "Bootstrap"]
date: 2024-03-10
image: "/images/projets/projet-sae.jpg"
githubUrl: "https://github.com/votre-username/projet-sae"
featured: false
ordre: 3
---

## Contexte académique

Projet réalisé dans le cadre de la SAE (Situation d'Apprentissage et d'Évaluation) [numéro] du BUT Informatique S[X].

**Durée** : [X] semaines  
**Équipe** : [Nombre] étudiants  
**Mon rôle** : [Votre rôle principal]

## Cahier des charges

L'objectif était de développer [description du besoin] pour [client/utilisateur cible].

### Contraintes techniques
- Utilisation obligatoire de Symfony pour le back-end
- Base de données relationnelle MySQL
- Interface responsive et accessible
- Respect des normes W3C

### Besoins fonctionnels
1. [Besoin 1]
2. [Besoin 2]
3. [Besoin 3]
4. [Besoin 4]

## Architecture et conception

### Modèle de données
Conception d'une base de données relationnelle avec [X] tables principales :
- **Table 1** : Description et utilité
- **Table 2** : Description et utilité
- **Table 3** : Description et utilité

### Architecture MVC
Utilisation du pattern MVC avec Symfony :
- **Modèles** : Entités Doctrine pour la gestion des données
- **Contrôleurs** : Logique métier et traitement des requêtes
- **Vues** : Templates Twig pour l'affichage

## Répartition du travail

En tant que [votre rôle], j'ai été responsable de :

- ✅ Conception et implémentation de la base de données
- ✅ Développement des contrôleurs pour [fonctionnalité X]
- ✅ Intégration front-end avec Bootstrap
- ✅ Tests fonctionnels et corrections de bugs

**Collaboration** : Utilisation de Git avec workflow GitFlow pour la gestion des branches et des merges.

## Technologies et outils

```
Back-end:
├── PHP 8.1
├── Symfony 6
└── Doctrine ORM

Front-end:
├── Twig (moteur de templates)
├── Bootstrap 5
└── JavaScript vanilla

Base de données:
└── MySQL 8.0

Outils:
├── Git & GitHub
├── Composer
├── PHPUnit (tests)
└── Symfony CLI
```

## Défis rencontrés

### Gestion de la sécurité
Mise en place d'un système d'authentification robuste et sécurisé.

**Solution** : Utilisation du système de sécurité intégré de Symfony avec hashage des mots de passe et gestion des rôles.

### Optimisation des requêtes SQL
Les requêtes initiales causaient des problèmes de performance.

**Solution** : Optimisation avec Doctrine QueryBuilder, ajout d'index et utilisation du cache de requêtes.

## Méthode de travail

- **Gestion de projet** : Méthode agile avec sprints de 2 semaines
- **Communication** : Réunions quotidiennes stand-up
- **Documentation** : Documentation technique complète avec PHPDoc
- **Tests** : Tests unitaires avec PHPUnit (couverture > 70%)

## Résultats

- ✅ Projet livré dans les délais
- ✅ Toutes les fonctionnalités demandées implémentées
- ✅ Application stable sans bugs majeurs
- 📊 Note obtenue : [X]/20

## Compétences développées

Ce projet m'a permis de renforcer :
- La maîtrise du framework Symfony et du pattern MVC
- La conception de bases de données relationnelles
- Le travail en équipe avec méthodologie agile
- La gestion de versions avec Git
- Les tests unitaires et l'assurance qualité

## Points d'amélioration identifiés

- Migration vers une architecture API REST
- Ajout d'une couche de tests d'intégration
- Amélioration de l'UX/UI
- Implémentation d'un système de cache avancé