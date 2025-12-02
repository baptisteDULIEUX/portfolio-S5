---
title: "SAMSOUL - Système de détection d'état second"
description: "Projet IoT de détection d'état second via capteurs Arduino et tests de réaction, avec architecture distribuée et intelligence artificielle"
technologies: ["Vue.js 3", "Arduino", "Java", "Python", "Node.js", "MongoDB", "Docker", "IA/ML"]
date: 2024-12-02
image: "/images/arduinos.webp"
featured: false
ordre: 3
---

## 🚧 Projet en cours de développement (30%)

> **Note** : Ce projet est actuellement en développement dans le cadre d'une SAE de fin d'année (S5/S6). Certaines fonctionnalités sont encore en phase de conception ou d'implémentation.

## Contexte du projet

Projet réalisé dans le cadre d'une **SAE (Situation d'Apprentissage et d'Évaluation) annuelle** du BUT Informatique S5/S6.

**Équipe** : 5 étudiants  
**Durée** : Année complète (S5/S6)  
**Fin prévue** : Juin 2025  
**Contrainte** : Architecture logicielle imposée avec services distribués

### Problématique

Comment détecter de manière fiable si une personne se trouve dans un **état second** (fatigue, stress, altération des capacités) en combinant :
- Des données physiologiques (capteurs portables)
- Des tests de réaction cognitive (mobile/écran)
- De l'intelligence artificielle pour l'analyse

**Applications potentielles** :
- Sécurité routière (détection de somnolence)
- Milieu professionnel (surveillance du bien-être)
- Santé (suivi de patients)
- Sport (détection de fatigue excessive)

## Objectifs et fonctionnalités

### Objectifs principaux
- **Collecter des données physiologiques** via capteurs Arduino embarqués
- **Mesurer les capacités de réaction** via tests interactifs (mobile et écran)
- **Analyser les données** avec intelligence artificielle pour détecter un état second
- **Visualiser en temps réel** l'état de l'utilisateur via dashboard web
- **Respecter une architecture distribuée** imposée (microservices, Docker)

### Architecture technique imposée

Le projet suit une architecture logicielle complexe en plusieurs couches :

```
Capteurs (Arduino)          Mobile (caméra, tests)
       ↓                              ↓
   µC1, µC2 ←→ Serveur TCP Java ←→ Serveur analyse média
       ↓                              ↓
       └──────────→ Python + API Node.js ←─────┘
                   (IA + accès BdD)
                          ↓
                      MongoDB
                          ↓
                  Frontend Vue.js
              (visualisation graphs/stats)
```

**Services dockerisés avec I/O** :
- Serveur TCP Java (centralisation données)
- Serveur d'analyse média (traitement images/vidéos)
- API Python + Node.js (intelligence artificielle)
- Base de données MongoDB
- Frontend Vue.js

## Fonctionnalités développées

### 1. Capteurs Arduino (µC1 & µC2)
**Responsable** : Équipe hardware

Deux microcontrôleurs collectant des données physiologiques :

**µC1 - Capteurs physiologiques** :
- Capteur 1 : Accéléromètre (détection de mouvements brusques)
- Capteur 2 : Capteur cardiaque (fréquence cardiaque)
- Capteur 3 : Gyroscope (orientation, équilibre)
- LED : Indicateur d'état

**µC2 - Interface utilisateur** :
- Bouton : Interaction manuelle
- Écran LCD : Affichage des instructions de test
- Capteur 3 : Thermomètre (température corporelle)

Communication avec le serveur TCP Java via protocole série/WiFi.

### 2. Application mobile (tests de réaction)
**Responsable** : Baptiste DULIEUX (mon rôle)

**Application web hybride** (accessible sur toutes plateformes) :

#### Tests de réaction développés
- **Test de temps de réaction simple** : Appuyer dès apparition d'un stimulus
- **Test de reconnaissance** : Identifier des formes/couleurs rapidement
- **Test de mémoire** : Mémoriser et reproduire des séquences
- **Capture photo/vidéo** : Analyse faciale pour détection de fatigue

#### Communication
- Envoi des résultats au serveur d'analyse média
- Réception de feedbacks en temps réel
- Synchronisation avec les données des capteurs Arduino

**Technologies** :
- Framework : Application web hybride (Vue.js 3 avec Capacitor/Cordova)
- Compatible : iOS, Android, navigateur web
- Communication : WebSocket pour temps réel

### 3. Frontend Vue.js (Dashboard & Visualisation)
**Responsable** : Baptiste DULIEUX (mon rôle principal)

**État actuel : 30% développé**

#### Fonctionnalités implémentées ✅
- **Templates de dashboards** : Structure complète des pages de visualisation
- **Squelettes de graphiques** : Composants prêts pour affichage de données
  - Graphique de fréquence cardiaque en temps réel
  - Historique des tests de réaction
  - Évolution de la température corporelle
  - Score global d'état (état second détecté ou non)
- **Système de layouts** : Organisation modulaire des vues
- **Composants réutilisables** : Cards, charts, tables pour affichage uniforme

#### À développer 🔄
- Connexion réelle à l'API Python/Node.js
- Affichage dynamique des données temps réel (WebSocket)
- Système d'alertes (notification si état second détecté)
- Historique et export des sessions (PDF, CSV)
- Paramétrage des seuils d'alerte

**Technologies** :
- **Vue.js 3** : Framework JavaScript progressif
- **Composition API** : Structure moderne et réactive
- **Chart.js** : Bibliothèque de graphiques interactifs
- **Axios** : Communication avec l'API backend
- **WebSocket** : Données en temps réel

### 4. Serveur TCP Java (centralisation)
**Responsable** : Équipe backend

- Réception des données des microcontrôleurs Arduino
- Transmission au système d'analyse Python
- Gestion des connexions multiples (plusieurs utilisateurs simultanés)

### 5. Serveur d'analyse média
**Responsable** : Équipe IA

- Réception des photos/vidéos de l'application mobile
- Analyse faciale : détection de signes de fatigue (clignements, bâillements)
- Transfert des résultats au serveur Python

### 6. API Python + Node.js (Intelligence Artificielle)
**Responsable** : Équipe IA/Backend

#### Traitement des données
- **Agrégation** : Fusion des données capteurs + tests + analyse faciale
- **Normalisation** : Standardisation des mesures
- **Modèle d'IA** : Classification binaire (état normal / état second)
  - Type : Machine Learning supervisé
  - Entraînement sur jeux de données médicales
  - Prédiction en temps réel

#### API REST
- Endpoints pour récupération des données (frontend)
- Endpoints pour envoi de données (capteurs, mobile)
- Authentification et gestion des sessions utilisateur

### 7. Base de données MongoDB
**Responsable** : Équipe backend

Stockage NoSQL pour flexibilité :
- Profils utilisateurs
- Historique des sessions de test
- Données brutes des capteurs (séries temporelles)
- Résultats d'analyse IA
- Logs système

## Mon rôle dans le projet

En tant que **développeur frontend et mobile**, je suis responsable de :

### Frontend Vue.js (Dashboard)
- ✅ Conception de l'architecture des composants
- ✅ Création des templates de dashboards
- ✅ Implémentation des squelettes de graphiques
- ✅ Mise en place du routing et de la navigation
- 🔄 Intégration avec l'API Python/Node.js (en cours)
- 🔄 Affichage des données temps réel via WebSocket
- 🔄 Système d'alertes et notifications

### Application mobile web hybride
- ✅ Conception de l'interface utilisateur
- ✅ Développement des tests de réaction de base
- 🔄 Intégration caméra pour analyse faciale
- 🔄 Communication avec le serveur d'analyse média
- 🔄 Synchronisation des données avec le backend

**Avancement global de mes tâches : ~30%**

## Technologies utilisées

### Mon stack (Frontend & Mobile)
- **Vue.js 3** : Framework JavaScript avec Composition API
- **Vite** : Build tool rapide et moderne
- **Chart.js / Recharts** : Visualisation de données
- **Axios** : Client HTTP pour l'API
- **Socket.io Client** : WebSocket pour temps réel
- **Capacitor/Cordova** : Transformation en app mobile hybride
- **Tailwind CSS / Vuetify** : Framework CSS pour le design

### Stack globale du projet
- **Arduino** : C/C++ pour les microcontrôleurs
- **Java** : Serveur TCP de centralisation
- **Python** : Intelligence artificielle et machine learning
  - Bibliothèques : TensorFlow/PyTorch, scikit-learn, pandas
- **Node.js** : API REST et gestion des accès BdD
- **MongoDB** : Base de données NoSQL
- **Docker** : Conteneurisation des services
- **Docker Compose** : Orchestration des conteneurs

## Défis rencontrés

### 1. Architecture distribuée complexe
**Défi** : Comprendre et respecter l'architecture imposée avec de nombreux services interconnectés.

**Approche** :
- Documentation approfondie de l'architecture
- Schémas de flux de données
- Communication étroite avec les équipes backend et hardware

### 2. Visualisation de données temps réel
**Défi** : Afficher des graphiques qui se mettent à jour en temps réel sans surcharger le navigateur.

**Solution prévue** :
- Utilisation de WebSocket pour push des données
- Limitation du nombre de points affichés (fenêtre glissante)
- Optimisation du rendering avec `requestAnimationFrame`

### 3. Application web hybride performante
**Défi** : Créer une application mobile fluide à partir d'une web app, notamment pour les tests de réaction qui nécessitent de la réactivité.

**Solution prévue** :
- Optimisation du code JavaScript
- Lazy loading des composants
- Utilisation de Service Workers pour mode hors ligne
- Tests sur plusieurs appareils physiques

### 4. Coordination d'équipe sur architecture imposée
**Défi** : Synchroniser le travail de 5 personnes sur des composants interdépendants avec une architecture rigide.

**Approche** :
- Définition claire des interfaces (API contracts)
- Mock data pour développer en parallèle
- Intégration progressive module par module
- Tests d'intégration réguliers

## État d'avancement global

### Par composant

| Composant | Avancement | Responsable |
|-----------|-----------|-------------|
| Arduino (µC1, µC2) | 40% | Équipe hardware |
| Serveur TCP Java | 35% | Équipe backend |
| Serveur analyse média | 25% | Équipe IA |
| API Python + IA | 30% | Équipe IA/Backend |
| MongoDB | 50% | Équipe backend |
| **Frontend Vue.js** | **30%** | **Baptiste (moi)** |
| **Application mobile** | **30%** | **Baptiste (moi)** |

**Avancement global du projet : ~32%**

## Prochaines étapes

### Court terme (avant février 2025)
- [ ] Finaliser les tests de réaction sur mobile
- [ ] Intégrer la caméra pour capture faciale
- [ ] Connecter le frontend à l'API (vraies données)
- [ ] Implémenter les WebSocket pour temps réel
- [ ] Compléter l'intégration Arduino ↔ Serveur TCP

### Moyen terme (mars-avril 2025)
- [ ] Tests d'intégration complets de bout en bout
- [ ] Entraînement du modèle d'IA sur données réelles
- [ ] Optimisation des performances (temps de réponse < 100ms)
- [ ] Tests utilisateurs avec volontaires
- [ ] Ajustement des seuils d'alerte

### Long terme (mai-juin 2025)
- [ ] Système d'alertes avancé (email, SMS)
- [ ] Export de rapports détaillés (PDF)
- [ ] Documentation technique complète
- [ ] Déploiement en environnement de production
- [ ] Préparation de la soutenance finale

## Compétences développées

### Compétences techniques (en cours d'acquisition)
- **Vue.js 3 avancé** : Composition API, composables, réactivité
- **Visualisation de données** : Graphiques temps réel, charts interactifs
- **Architecture microservices** : Compréhension des systèmes distribués
- **Communication temps réel** : WebSocket, événements asynchrones
- **Applications hybrides** : Web-to-mobile avec Capacitor
- **Travail avec API complexes** : Intégration multi-services

### Compétences professionnelles
- **Gestion de projet au long cours** : Organisation sur une année complète
- **Coordination d'équipe** : Synchronisation avec équipes backend et hardware
- **Adaptabilité** : Respect d'une architecture imposée et contraignante
- **Documentation** : Nécessité de documenter pour l'intégration future

## Évolutions possibles

### Fonctionnalités avancées
- [ ] **Multi-utilisateurs** : Suivi de plusieurs personnes simultanément
- [ ] **Profils personnalisés** : Calibration selon l'individu (âge, condition physique)
- [ ] **Historique long terme** : Analyse de l'évolution sur plusieurs mois
- [ ] **Prédiction** : Anticipation d'un état second avant qu'il survienne
- [ ] **Recommandations** : Suggestions d'actions (pause, repos, hydratation)

### Améliorations techniques
- [ ] **Tests automatisés** : Jest pour le frontend, Cypress end-to-end
- [ ] **CI/CD** : Pipeline automatisé avec GitHub Actions
- [ ] **Progressive Web App** : Installation sur mobile comme app native
- [ ] **Mode hors ligne** : Fonctionnement sans connexion avec sync ultérieure
- [ ] **Optimisation IA** : Modèle plus léger pour exécution sur mobile

## Conclusion

**SAMSOUL** est un projet ambitieux combinant **IoT, intelligence artificielle et développement web moderne**. La contrainte d'architecture distribuée rend le projet particulièrement formateur en termes de compréhension des systèmes complexes.

Mon rôle sur la partie **frontend et mobile** me permet de développer des compétences en **Vue.js 3, visualisation de données temps réel et applications hybrides**. C'est également une excellente opportunité de collaborer avec des équipes backend et hardware, reproduisant un environnement professionnel réaliste.

Bien que le projet soit encore en développement (30%), les bases sont solides et l'architecture claire. Les prochains mois seront consacrés à l'intégration des différents composants et aux tests utilisateurs.

---

**Projet en cours** : SAE BUT Informatique S5/S6  
**Établissement** : IUT Nord Franche-Comté  
**Équipe** : 5 étudiants  
**Fin prévue** : Juin 2025  
**Technologies** : Vue.js 3, Arduino, Python IA, Java, MongoDB, Docker