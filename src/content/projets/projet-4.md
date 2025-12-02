---
title: "LOL-COACH - Prédiction de winrate et coaching IA"
description: "Modèle de Machine Learning pour prédire le taux de victoire d'une composition de champions League of Legends avec IA générative pour le coaching stratégique"
technologies: ["Python", "Pandas", "NumPy", "Scikit-learn", "LightGBM", "Mistral API", "API Riot Games"]
date: 2024-12-02
image: "/images/neural.webp"
featured: false
ordre: 4
---

## 🚧 Projet en cours de développement (60%)

> **Note** : Ce projet est actuellement en développement dans le cadre d'un TP de S5. Rendu prévu fin décembre 2024.

## Contexte du projet

Projet réalisé dans le cadre d'un **TP de Machine Learning** du BUT Informatique S5.

**Équipe** : 2 étudiants (Baptiste DULIEUX, Timothée MEYER)  
**Durée** : Semestre 5  
**Date de rendu** : Fin décembre 2024  
**Contexte** : League of Legends - Jeu compétitif en équipe 5v5 avec plus de 160 champions

### Problématique

Dans League of Legends, la phase de **draft** (sélection des champions) est cruciale pour déterminer l'issue d'une partie. Cependant, l'analyse se limite souvent à :
- Des statistiques individuelles par champion (winrate isolé)
- Des recommandations empiriques de joueurs professionnels
- Des outils basiques de tier-list

**Manque** : Aucun outil ne quantifie précisément les **synergies** (combinaisons favorables d'alliés) et les **contres** (matchups défavorables) entre les 10 champions d'une partie.

**Objectif du projet** : Développer un système d'intelligence artificielle capable de :
1. Prédire le **winrate** d'une composition basée sur les interactions entre champions
2. Quantifier les **effets implicites** (synergie/contre) au-delà des stats individuelles
3. Générer des **recommandations stratégiques** pour la partie via IA générative

## Objectifs et fonctionnalités

### Objectifs principaux

#### 1. Modélisation du Winrate de Draft
Développer un modèle de Machine Learning capable de prédire la probabilité de victoire d'une équipe, basée uniquement sur :
- Les **10 champions** choisis (5 alliés, 5 ennemis)
- Leurs **rôles** respectifs (Top, Jungle, Mid, ADC, Support)

#### 2. Quantification des Interactions
Isoler et quantifier **trois scores clés** pour chaque composition :

**Score de Force Brute (β)** :
- Impact individuel du champion indépendamment de son contexte
- Mesure la puissance "pure" du champion dans son rôle
- Calculé via régression logistique (coefficients β interprétables)

**Score de Synergie** :
- Combinaisons positives de champions alliés
- Matchups avantageux face aux champions ennemis
- Exemples : Yasuo + Malphite (combo ultime), Yuumi + champions hypermobiles

**Score de Contre** :
- Combinaisons adverses défavorables
- Matchups désavantageux pour vos champions
- Exemples : Champions sans mobilité face à des assassins, tanks face à des %HP true damage

**Formule du Score d'Interaction** :
```
Score d'Interaction = WR_LightGBM - WR_RegressionLogistique
```

Si Score > 0 : Synergie dominante (composition favorable)  
Si Score < 0 : Contre dominant (composition défavorable)

#### 3. Coaching Stratégique par IA Générative
Intégration de l'**API Mistral** pour générer des recommandations personnalisées :
- **Recommandations de draft** : Quels champions choisir/bannir selon la composition adverse
- **Conseils stratégiques** : Plan de jeu optimal (early game, objectifs prioritaires, win conditions)
- **Analyse de matchup** : Points faibles à exploiter, menaces à éviter

## Architecture du projet

### Pipeline de données

```
API Riot Games (Matchs NA S13)
        ↓
Collecte & Stockage
(~X millions de matchs classés)
        ↓
Preprocessing & Vectorisation
(Champions encodés par rôle : +1/-1/0)
        ↓
    ┌───────────────┴───────────────┐
    ↓                               ↓
Régression Logistique          LightGBM
(Score de Force Brute)    (Prédiction finale)
    ↓                               ↓
    └───────────────┬───────────────┘
                    ↓
        Analyse des Résidus
    (Score Synergie/Contre)
                    ↓
            API Mistral
        (Coaching stratégique)
```

## Technologies utilisées

### Stack Data Science & Machine Learning

| Catégorie | Technologie | Rôle dans le projet |
|-----------|-------------|---------------------|
| **Collecte de données** | API Riot Games | Source des données brutes (champions, rôles, résultat) |
| **Manipulation des données** | Python (Pandas, NumPy) | Nettoyage, vectorisation positionnelle des champions |
| **Modèle baseline** | Scikit-learn (Régression Logistique) | Calcul du Score de Force Brute (β), interprétabilité |
| **Modèle avancé** | LightGBM (Gradient Boosting) | Prédiction finale capturant les interactions non-linéaires |
| **Analyse** | Analyse des résidus | Calcul du Score d'Interaction (Synergie - Contre) |
| **IA Générative** | Mistral API | Génération de recommandations stratégiques |
| **Notebooks** | Jupyter / Google Colab | Expérimentation et visualisation des résultats |
| **Visualisation** | Matplotlib, Seaborn | Graphiques d'analyse (feature importance, résidus) |

### Dataset

**Source** : API Riot Games  
**Région** : NA (North America)  
**Saison** : Saison 13 (2023)  
**Type de matchs** : Ranked (classés uniquement)  
**Rangs** : Tous (Iron à Challenger)  
**Taille** : Plusieurs millions de parties analysées

**Features extraites par match** :
- 10 champions (IDs)
- 10 rôles (Top, Jungle, Mid, ADC, Support)
- Résultat (victoire équipe bleue : 1/0)

**Preprocessing** :
- **Vectorisation positionnelle** : Chaque champion est encodé avec son rôle
  - Champion allié dans son rôle : `+1`
  - Champion ennemi dans ce rôle : `-1`
  - Absent : `0`
- Résultat : Matrice sparse de dimension `(n_matchs, n_champions × n_roles)`

## Mon rôle dans le projet

En tant que **data scientist et développeur IA**, je suis responsable de :

### 1. Preprocessing des données (ma partie principale)
- ✅ Collecte des données via API Riot Games
- ✅ Nettoyage et structuration du dataset (gestion des valeurs manquantes, outliers)
- ✅ **Vectorisation positionnelle** : Transformation champions → features encodées par rôle
- ✅ Séparation train/test/validation (stratification par rang si nécessaire)
- ✅ Feature engineering : Création de features dérivées (taux de ban, popularité du meta)

### 2. Modélisation Machine Learning (ma partie principale)
- ✅ Implémentation du **modèle baseline** (Régression Logistique)
  - Extraction des coefficients β (Score de Force Brute par champion/rôle)
  - Interprétation des features les plus impactantes
- ✅ Développement du **modèle avancé** (LightGBM)
  - Tuning des hyperparamètres (grid search / random search)
  - Validation croisée pour éviter l'overfitting
  - Optimisation des performances (learning rate, max depth, num leaves)
- ✅ **Analyse des résidus** : Calcul du Score d'Interaction
  - Identification des compositions avec forte synergie
  - Identification des compositions contrees

**Performance actuelle** : ~60% d'accuracy (modèle en cours d'optimisation)

### 3. Intégration de l'IA Générative (ma partie principale)
- ✅ Intégration de l'**API Mistral** pour génération de texte
- ✅ **Recommandations de draft** :
  - Prompt engineering : "Étant donné cette composition et ce meta, quels champions bannir/choisir ?"
  - Génération de suggestions basées sur les scores calculés
- ✅ **Conseils stratégiques en partie** :
  - Analyse de la composition finale (après draft)
  - Génération de plan de jeu : early game, objectifs, win conditions
  - Identification des points faibles adverses à exploiter

**Exemple de prompt Mistral** :
```python
prompt = f"""
Tu es un coach professionnel League of Legends. Analyse cette composition :

Équipe Alliée : {ally_champions} (rôles : {ally_roles})
Équipe Ennemie : {enemy_champions} (rôles : {enemy_roles})

Scores calculés :
- Force Brute : {brute_force_score}
- Score d'Interaction : {interaction_score} (Synergie/Contre)
- Winrate prédit : {predicted_winrate}%

Fournis :
1. Analyse des forces/faiblesses de chaque équipe
2. Win conditions de ton équipe
3. Plan de jeu recommandé (early/mid/late game)
4. Points d'attention stratégiques
"""
```

### Répartition du travail avec Timothée MEYER
- **Baptiste (moi)** : Preprocessing, modélisation ML, IA générative
- **Timothée** : Collecte de données complémentaires, visualisations, analyse statistique

## Défis rencontrés et solutions

### 1. Volume massif de données
**Défi** : Plusieurs millions de parties à traiter, risque de saturation mémoire et temps de calcul prohibitif.

**Solutions appliquées** :
- Échantillonnage stratifié (garder représentativité des rangs)
- Traitement par batch pour l'entraînement LightGBM
- Utilisation de types de données optimisés (`int8`, `float32` au lieu de `float64`)
- Cache des données préprocessées (pickle/parquet)

### 2. Déséquilibre de classes
**Défi** : Winrate global proche de 50/50, mais certains matchups extrêmes sous-représentés.

**Solutions appliquées** :
- Pondération des classes dans la loss function
- Sur-échantillonnage des configurations rares (SMOTE)
- Validation croisée stratifiée pour conserver la distribution

### 3. Complexité des interactions
**Défi** : 160+ champions × 5 rôles = espace de features énorme, risque de malédiction de la dimensionnalité.

**Solutions appliquées** :
- Feature selection : élimination des champions très rarement joués
- Régularisation L2 dans la régression logistique
- Early stopping dans LightGBM pour éviter l'overfitting

### 4. Interprétabilité vs Performance
**Défi** : Régression Logistique interprétable mais limitée ; LightGBM performant mais "boîte noire".

**Solution adoptée** :
- **Approche hybride** : Régression Logistique pour l'interprétabilité (β scores)
- LightGBM pour la précision maximale
- Analyse des résidus pour isoler les effets d'interaction
- SHAP values pour expliquer les prédictions LightGBM localement

### 5. Qualité des recommandations IA générative
**Défi** : Mistral peut générer des conseils génériques ou incohérents si mal prompté.

**Solutions appliquées** :
- **Prompt engineering rigoureux** : Contexte détaillé + scores numériques
- Few-shot prompting : Exemples de bonnes analyses dans le prompt
- Validation manuelle des sorties (vérification cohérence stratégique)
- Post-processing : Extraction des points clés structurés (bullet points)

## État d'avancement

### Par composant

| Composant | Avancement | Responsable |
|-----------|-----------|-------------|
| Collecte de données (API Riot) | 100% | Timothée |
| Preprocessing & Vectorisation | 100% | Baptiste (moi) |
| Régression Logistique (baseline) | 100% | Baptiste (moi) |
| LightGBM (modèle avancé) | 80% | Baptiste (moi) |
| Analyse des résidus | 70% | Baptiste (moi) |
| Intégration Mistral API | 60% | Baptiste (moi) |
| Visualisations & Graphiques | 50% | Timothée |
| Interface de test | 0% | À développer |

**Avancement global du projet : ~60%**

### Métriques actuelles

**Modèle Régression Logistique** :
- Accuracy : ~55%
- Sert de baseline pour comparaison

**Modèle LightGBM** :
- Accuracy : **~60%**
- En cours d'optimisation (hyperparameter tuning)
- Objectif : Atteindre 63-65% (état de l'art pour ce type de prédiction)

**IA Générative (Mistral)** :
- Qualité des recommandations : Variable (dépend du prompt)
- Pertinence stratégique : Bonne (validation manuelle positive)

## Prochaines étapes

### Avant le rendu (fin décembre 2024)

#### Court terme (décembre)
- [ ] Finaliser le tuning des hyperparamètres LightGBM
- [ ] Améliorer l'accuracy à 63%+ (target)
- [ ] Compléter l'analyse des résidus (toutes les compositions)
- [ ] Raffiner les prompts Mistral pour recommandations plus précises
- [ ] Créer un notebook de démonstration interactif
- [ ] Rédiger le rapport technique complet

#### Optimisations finales
- [ ] Feature engineering avancé (méta-features : taux de ban, popularité)
- [ ] Ensemble de modèles (voting classifier : LR + LGBM + XGBoost)
- [ ] Validation sur données saison 14 (nouveaux patchs)
- [ ] SHAP analysis pour interprétabilité du LightGBM

### Évolutions possibles (post-rendu)

#### Interface utilisateur
- [ ] **Web app interactive** (Streamlit/Gradio) :
  - Sélection des 10 champions via dropdown
  - Affichage du winrate prédit en temps réel
  - Visualisation des scores (Force/Synergie/Contre)
  - Recommandations Mistral générées à la demande

#### Fonctionnalités avancées
- [ ] **Mode draft simulator** : Simulation de phase de pick/ban complète
- [ ] **Analyse de meta** : Identification des compositions OP du patch actuel
- [ ] **Historique personnel** : Import de l'historique d'un joueur pour recommandations personnalisées
- [ ] **Mode coaching live** : Suggestions en temps réel pendant le draft (overlay)

#### Améliorations ML
- [ ] Prise en compte du **patch** (équilibrage champions évolue)
- [ ] Modèle **multi-classe** : Prédire le score final (pas juste victoire/défaite)
- [ ] Analyse des **bans** : Intégrer les 10 champions bannis dans la prédiction
- [ ] Modèle de **recommandation de pick** : "Quel champion choisir étant donné les 9 autres ?"

## Compétences développées

### Compétences techniques (acquises)
- **Data Science** : Manipulation de gros datasets (Pandas, NumPy)
- **Feature Engineering** : Vectorisation positionnelle, création de features dérivées
- **Machine Learning** :
  - Régression Logistique : Interprétabilité des coefficients
  - LightGBM : Gradient Boosting avancé, hyperparameter tuning
  - Validation croisée, métriques de classification
- **IA Générative** : Intégration d'API (Mistral), prompt engineering
- **Analyse statistique** : Analyse des résidus, SHAP values
- **Python avancé** : Scripts robustes, gestion mémoire, optimisations

### Compétences méthodologiques
- **Approche scientifique** : Hypothèses → Expérimentations → Validation
- **Interprétabilité** : Ne pas se contenter de la précision, comprendre le "pourquoi"
- **Travail en binôme** : Répartition efficace des tâches, synchronisation
- **Documentation** : Code commenté, notebooks structurés, rapport technique

### Compétences transverses
- **Connaissance du domaine** : Compréhension approfondie de League of Legends (méta, stratégies)
- **Créativité** : Innovation dans l'analyse (Score d'Interaction, IA générative pour coaching)
- **Esprit critique** : Remise en question des résultats (accuracy 60% = peut mieux faire)

## Résultats et apprentissages

### Points forts du projet
✅ **Approche innovante** : Quantification rigoureuse des synergies/contres (rarement fait)  
✅ **Hybridation ML + IA générative** : Modèle prédictif + coaching stratégique  
✅ **Dataset massif** : Millions de parties pour entraînement robuste  
✅ **Interprétabilité** : Ne pas se limiter à une "boîte noire", comprendre les mécanismes  
✅ **Application concrète** : Utilité réelle pour joueurs LoL compétitifs  

### Difficultés persistantes
⚠️ **Accuracy limitée** : 60% est correct mais perfectible (complexité intrinsèque du jeu)  
⚠️ **Absence d'interface** : Pas de démo visuelle pour l'instant (focus sur le ML)  
⚠️ **Données statiques** : Patch 13.X uniquement, modèle deviendra obsolète avec les MAJ  

### Enseignements clés
- **Preprocessing = 80% du travail** : La qualité des features détermine la performance
- **Simplicité d'abord** : Régression Logistique indispensable avant modèles complexes
- **Domain knowledge crucial** : Comprendre LoL permet de créer de meilleures features
- **IA générative complémentaire** : Mistral enrichit l'expérience mais ne remplace pas le ML

## Conclusion

**LOL-COACH** est un projet ambitieux combinant **Data Science, Machine Learning et IA Générative** appliqués au jeu vidéo compétitif. Au-delà de la simple prédiction de victoire, il apporte une **quantification rigoureuse des interactions entre champions** (synergies/contres) et des **recommandations stratégiques intelligentes** via Mistral.

Mon rôle central sur le **preprocessing, la modélisation ML et l'intégration de l'IA générative** m'a permis de développer des compétences solides en Data Science et de comprendre les défis d'un projet ML de bout en bout : de la collecte de données à l'analyse des résultats.

Avec une accuracy actuelle de **60%** et un projet avancé à **60%**, les semaines à venir seront consacrées à l'optimisation du modèle et à la finalisation des recommandations IA pour le rendu de fin décembre.

Ce projet démontre qu'il est possible de combiner **passion pour le gaming** et **compétences techniques** pour créer des outils d'analyse avancés et utiles.

---

**Projet universitaire** : TP Machine Learning BUT Informatique S5  
**Établissement** : IUT Nord Franche-Comté  
**Équipe** : 2 étudiants (Baptiste DULIEUX, Timothée MEYER)  
**Date de rendu** : Fin décembre 2024  
**Technologies** : Python, Scikit-learn, LightGBM, Mistral API, Pandas, NumPy

**Note** : League of Legends est une marque déposée de Riot Games. Ce projet est réalisé dans un cadre éducatif et utilise l'API publique Riot Games.