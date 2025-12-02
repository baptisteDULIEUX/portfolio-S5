---
title: "TrifleConsole - Jeu Kamisado avec IA"
description: "Implémentation complète du jeu de plateau Kamisado en Java avec interface console/graphique et intelligence artificielle (Minimax + heuristique)"
technologies: ["Java", "JavaFX", "Boardifier", "Minimax", "JUnit", "Mockito", "MVC"]
date: 2024-06-15
image: "/src/assets/triffle.png"
githubUrl: "https://github.com/baptisteDULIEUX/trifle.git"
featured: false
ordre: 5
---

## ✅ Projet terminé et fonctionnel

> **Note** : Ce projet a été finalisé en juin 2024 dans le cadre d'une SAE de S2. Le jeu est entièrement jouable en mode console et graphique avec des IA performantes.

## Contexte du projet

Projet réalisé dans le cadre d'une **SAE (Situation d'Apprentissage et d'Évaluation)** du BUT Informatique S2.

**Équipe** : 5 étudiants
- Cédric Colin
- Marvyn Levin
- Hugues Estrade
- Timothée Meyer
- Baptiste Dulieux (moi)

**Durée** : Semestre 2  
**Date de rendu** : Juin 2024  
**Contraintes** : Architecture MVC imposée, tests unitaires obligatoires

### Le jeu Kamisado

**Kamisado** est un jeu de plateau stratégique abstrait pour 2 joueurs, créé par Peter Burley.

**Principe du jeu** :
- Plateau de 8×8 cases colorées (8 couleurs différentes)
- Chaque joueur possède 8 tours colorées
- La couleur de la case d'arrivée détermine quelle tour adverse doit bouger
- **Objectif** : Amener une de ses tours sur la ligne adverse

**Complexité** :
- Profondeur stratégique élevée (comparable aux échecs)
- Arbre de décision complexe avec contraintes de couleur
- Nécessite anticipation et tactique

### Pourquoi "Trifle" ?

> *Trifle is a layered dessert of English origin. The usual ingredients are a thin layer of sponge fingers or sponge cake soaked in sherry [...] The contents of a trifle are highly variable and many varieties exist.*

Le nom du projet fait référence aux **multiples couches** du dessert anglais, symbolisant :
- Les couches d'abstraction du code (MVC)
- Les variantes de règles implémentées (Oshi, Sumo)
- La richesse stratégique du jeu

## Objectifs et fonctionnalités

### Objectifs principaux

1. **Implémenter le jeu Kamisado complet** avec toutes ses règles
2. **Développer des IA compétitives** capables de battre des joueurs humains
3. **Créer une interface utilisateur** fluide (console et graphique)
4. **Respecter l'architecture MVC** avec séparation stricte des responsabilités
5. **Garantir la qualité du code** via tests unitaires exhaustifs

### Fonctionnalités développées

#### 1. Jeu de base (Console)
Interface en ligne de commande (TUI - Text User Interface) :

**Fonctionnalités** :
- Affichage du plateau avec couleurs ANSI
- Notation des cases (coordonnées)
- Saisie des coups par l'utilisateur
- Validation des mouvements légaux
- Historique des coups

**Configuration flexible** :
```bash
# Humain vs Humain
java -cp out trifleConsole.TrifleConsole 0

# Humain vs IA
java -cp out trifleConsole.TrifleConsole 1

# IA vs IA (benchmarking)
java -cp out trifleConsole.TrifleConsole 2
```

**Options avancées** :
- Export des parties : `--output-moves ./partie.in`
- Ralentissement de l'IA : `WAIT_BEFORE_END=5000` (5 secondes)
- Menu interactif pour configuration (noms joueurs, stratégies)

#### 2. Interface graphique (JavaFX)
Implémentation avec **Boardifier** (framework JavaFX pour jeux de plateau) :

**Fonctionnalités** :
- Plateau graphique avec cases colorées
- Tours stylisées avec textures
- Animations des déplacements
- Drag & drop pour déplacer les pièces
- Indications visuelles des coups possibles
- Score et historique affichés

**Architecture MVC** :
- **Model** : Logique du jeu (règles, état)
- **View** : Affichage graphique (JavaFX)
- **Controller** : Gestion des interactions utilisateur

#### 3. Intelligence Artificielle

##### Algorithme Minimax
**Principe** : Exploration de l'arbre de jeu pour trouver le meilleur coup.

- **Évaluation** : Fonction heuristique inspirée des échecs
- **Optimisation** : Élagage Alpha-Beta (supposé, standard pour Minimax)
- **Performance** : Taux de victoire de **60%** contre joueurs humains

##### Stratégie heuristique
**Principes appliqués** (inspirés des échecs) :

1. **Contrôle du centre** : Favoriser les tours centrales (plus de mobilité)
2. **Avancée progressive** : Prioriser les tours proches de la ligne adverse
3. **Blocage adverse** : Limiter les options de l'adversaire
4. **Sécurité** : Éviter les positions vulnérables
5. **Tempo** : Forcer l'adversaire à jouer avec des tours défavorables

**Fonction d'évaluation** :
```
Score = α × Position + β × Mobilité + γ × Contrôle + δ × Avancée
```

Où :
- **Position** : Valeur intrinsèque de la case (centre > bord)
- **Mobilité** : Nombre de coups légaux disponibles
- **Contrôle** : Influence sur le jeu adverse
- **Avancée** : Distance à la ligne de victoire

##### Configuration des bots
Le TUI permet de choisir parmi plusieurs stratégies :
- **Aléatoire** : Coups au hasard (baseline)
- **Heuristique** : Stratégie basée sur l'évaluation
- **Minimax** : Exploration d'arbre avec heuristique

#### 4. Règles avancées

**Règle Oshi** :
- Mode de jeu alternatif
- Permet de pousser les tours adverses
- Complexité accrue de l'arbre de décision

**Règle Sumo** :
- Variante avec élimination de tours
- Tour poussée hors du plateau = éliminée
- Condition de victoire alternative

#### 5. Système de tests

**Tests unitaires** (JUnit + Mockito) :
- Couverture extensive du code
- Tests du Model (logique de jeu)
- Tests des Controllers (interactions)
- Tests de non-régression

**Benchmarking** :
- Script bash `run_game.sh` pour lancer N parties
- Analyse statistique des performances IA
- Profiling mémoire/CPU (IDEA Profiler)

## Mon rôle dans le projet

En tant que **développeur et testeur**, j'ai contribué à plusieurs aspects du projet :

### 1. Tests unitaires (90% de mon temps)
**Responsabilité principale** du projet.

**Réalisations** :
- ✅ Tests complets du **Model** (logique de jeu)
  - Validation des règles de déplacement
  - Vérification des conditions de victoire
  - Tests des cas limites (bords du plateau, contraintes de couleur)
- ✅ Tests des **Controllers** (gestion des événements)
  - Interactions utilisateur (clics, saisie)
  - Communication Model ↔ View
- ✅ Utilisation de **Mockito** pour mocker les dépendances
- ✅ Tests de non-régression après modifications

**Difficulté rencontrée** :
- Problème avec **Mockito sur la View** (JavaFX)
  - Les composants JavaFX sont difficiles à mocker (threads, contexte graphique)
  - Solution : Tests d'intégration au lieu de tests unitaires purs pour la View

**Impact** :
- Code robuste et fiable
- Détection précoce des bugs
- Facilitation du refactoring

### 2. Règles élémentaires du jeu (10% de mon temps)
Participation au développement de la **logique de base** :

- Implémentation de règles de mouvement simples
- Détection et correction de bugs dans le code de mes coéquipiers
- Revue de code et suggestions d'amélioration

### 3. Règles complexes (15% de mon temps)
Collaboration avec **Marvyn Levin** et **Cédric Colin** :

- Co-développement de la **règle Oshi**
- Co-développement de la **règle Sumo**
- Tests et validation de ces variantes

### 4. Rapports et documentation (30% de mon temps)
Support à l'équipe sur la **partie rédactionnelle** :

- ✅ Rédaction de sections du rapport technique (37 pages)
- ✅ Création de diaporamas de présentation
- ✅ Documentation des stratégies IA
- ✅ Réalisation de la **vidéo de démonstration** du jeu

### Répartition visuelle de mon implication
D'après l'analyse Git :
- **Tests** : 90%
- **Rapports/Documentation** : 30%
- **Règles complexes** : 15%
- **Règles de base** : 10%

*Note* : Les pourcentages dépassent 100% car certaines tâches se chevauchent.

## Technologies utilisées

### Stack technique

| Catégorie | Technologie | Rôle |
|-----------|-------------|------|
| **Langage** | Java 17 | Langage principal du projet |
| **Interface graphique** | JavaFX | Framework pour l'interface utilisateur |
| **Framework jeu** | Boardifier | Surcouche JavaFX pour jeux de plateau |
| **Architecture** | MVC | Séparation Model-View-Controller |
| **Tests** | JUnit 5 | Framework de tests unitaires |
| **Mocking** | Mockito | Simulation de dépendances pour tests |
| **Build** | Javac (manuel) | Compilation Java classique |
| **Versioning** | Git + GitLab | Gestion de versions (IUT) |
| **Benchmarking** | Bash scripts | Automatisation des tests de performance |
| **Profiling** | IntelliJ IDEA Profiler | Analyse mémoire et CPU |

### Outils de développement
- **IDE** : IntelliJ IDEA (recommandé pour JUnit)
- **Terminal** : TTY avec support couleurs ANSI
- **OS** : Linux (Debian 12), Windows 10/11, macOS (testés)

## Défis rencontrés et solutions

### 1. Tests unitaires sur JavaFX (Mockito)
**Défi** : Impossible de mocker correctement la **View** avec Mockito.

**Problème technique** :
- JavaFX nécessite un thread d'application dédié
- Les composants graphiques (Scene, Stage) ne sont pas facilement mockables
- Erreur : `IllegalStateException: Not on FX application thread`

**Solution appliquée** :
- Abandon des tests unitaires purs pour la View
- Passage à des **tests d'intégration** pour les parties graphiques
- Focus sur les tests du Model et Controller (logique métier)

**Apprentissage** :
- Comprendre les limites du mocking
- Savoir quand privilégier tests d'intégration vs unitaires

### 2. Complexité de l'arbre de décision Minimax
**Défi** : Explosion combinatoire du nombre de coups possibles.

**Problème** :
- 8 tours par joueur × mouvements possibles = arbre très large
- Temps de calcul prohibitif au-delà de 3-4 niveaux de profondeur

**Solutions probables** (standard pour Minimax) :
- Élagage Alpha-Beta pour réduire l'exploration
- Limitation de la profondeur de recherche
- Optimisation de la fonction d'évaluation (calcul rapide)

### 3. Coordination d'équipe
**Défi** : 5 développeurs travaillant sur des modules différents.

**Approche** :
- Répartition claire des tâches dès le début
- Revue de code croisée (code review)
- Tests continus pour détecter les régressions
- Communication via GitLab (issues, merge requests)

**Impact sur moi** :
- Rôle de **support transversal** (aide sur la plupart des tâches)
- Renforcement des liens d'équipe
- Compréhension des différentes approches de résolution

## Résultats et performances

### Métriques du projet

**Code** :
- ~5000+ lignes de code Java
- Architecture MVC respectée
- Tests unitaires : Couverture élevée (Model + Controller)

**IA** :
- Taux de victoire : **60%** contre joueurs humains
- Temps de réflexion moyen : ~2-5 secondes par coup (Minimax)
- Stratégies : 3 niveaux (Aléatoire, Heuristique, Minimax)

**Interfaces** :
- Console : Fonctionnelle, couleurs ANSI
- Graphique : Fluide, animations, drag & drop

**Benchmarking** :
- Script automatisé pour lancer 100+ parties
- Analyse statistique des performances bots
- Profiling mémoire : Pas de fuite détectée

## Compétences développées

### Compétences techniques (acquises)
- **Java avancé** : Manipulation d'objets complexes, héritage, polymorphisme
- **JavaFX** : Création d'interfaces graphiques modernes
- **Architecture MVC** : Séparation claire des responsabilités
- **Tests unitaires** : JUnit, Mockito, couverture de code
- **Intelligence Artificielle** : Algorithme Minimax, fonctions heuristiques
- **Profiling & Optimisation** : Analyse mémoire/CPU, détection de goulots

### Compétences méthodologiques
- **Rigueur de test** : Importance des tests pour garantir la qualité
- **Travail collaboratif** : Support multi-tâches, aide aux coéquipiers
- **Documentation** : Rédaction technique, clarté et précision
- **Gestion de projet** : Priorisation, respect des délais

### Compétences transverses
- **Communication** : Rédaction de rapports, création de vidéos
- **Pédagogie** : Expliquer des concepts complexes aux coéquipiers
- **Adaptabilité** : Passer rapidement d'une tâche à une autre
- **Esprit d'équipe** : Renforcement des liens, entraide

## Évolutions possibles

### Améliorations techniques
- [ ] **Optimisation Minimax** : Transposition table (memoization des positions)
- [ ] **Apprentissage automatique** : Remplacer l'heuristique par un réseau de neurones
- [ ] **Interface web** : Version jouable dans le navigateur (JavaFX → JavaScript)
- [ ] **Multijoueur en ligne** : Jouer contre d'autres joueurs via réseau

### Fonctionnalités additionnelles
- [ ] **Replay de parties** : Revoir une partie jouée coup par coup
- [ ] **Classement ELO** : Système de notation des joueurs
- [ ] **Analyse post-partie** : Suggestions d'amélioration par l'IA
- [ ] **Mode tournoi** : Organisation de compétitions automatiques

### Expérience utilisateur
- [ ] **Tutoriel interactif** : Apprendre les règles en jouant
- [ ] **Niveaux de difficulté** : Facile, Moyen, Difficile, Expert
- [ ] **Statistiques joueur** : Historique, taux de victoire, coups préférés
- [ ] **Thèmes graphiques** : Personnalisation du plateau et des tours

## Conclusion

**TrifleConsole** est un projet complet et abouti qui combine **logique de jeu, intelligence artificielle et interfaces utilisateur**. Ce projet de S2 m'a permis de développer des compétences solides en **tests unitaires, architecture MVC et JavaFX**.

Mon rôle transversal m'a offert une **vue d'ensemble du projet**, de la logique métier aux interfaces, en passant par l'IA et la documentation. La réalisation de **90% des tests unitaires** a été un défi formateur, notamment sur les limites du mocking avec JavaFX.

Le travail en équipe de 5 personnes a renforcé mes compétences en **collaboration et communication**, avec un impact positif sur la cohésion du groupe. Participer à la plupart des tâches m'a permis de comprendre les différentes approches de mes coéquipiers.

Avec un **taux de victoire de 60%** pour les IA et une application entièrement fonctionnelle (console + graphique), ce projet démontre notre capacité à **livrer un produit de qualité** dans les délais impartis.

---

**Projet universitaire** : SAE BUT Informatique S2  
**Établissement** : IUT Nord Franche-Comté  
**Équipe** : 5 étudiants  
**Date de rendu** : Juin 2024  
**Technologies** : Java 17, JavaFX, Boardifier, JUnit, Mockito  
**Repository** : github

**Note** : Le jeu Kamisado est une création de Peter Burley. Ce projet est réalisé dans un cadre éducatif.