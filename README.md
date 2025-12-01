# Portfolio Baptiste Dulieux

Portfolio professionnel développé avec Astro, Vue.js et Tailwind CSS.

## 🚀 Technologies utilisées

- **Astro** - Framework moderne pour sites ultra-rapides
- **Vue.js 3** - Framework JavaScript progressif
- **Tailwind CSS** - Framework CSS utility-first
- **TypeScript** - JavaScript typé
- **MDX** - Markdown avec JSX pour le contenu

## 📋 Prérequis

- Node.js 18+ 
- npm ou yarn

## 🛠️ Installation

### 1. Créer le projet

```bash
npm create astro@latest portfolio-baptiste
cd portfolio-baptiste
```

### 2. Installer les intégrations

```bash
# Vue.js
npx astro add vue

# Tailwind CSS
npx astro add tailwind

# MDX (pour le contenu Markdown)
npx astro add mdx
```

### 3. Structure du projet

Créez la structure de fichiers suivante :

```
portfolio-baptiste/
├── src/
│   ├── components/
│   │   ├── Header.vue
│   │   ├── Footer.vue
│   │   ├── ContactForm.vue
│   │   ├── ProjectCard.vue
│   │   └── SkillCard.vue
│   ├── layouts/
│   │   └── Layout.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── projets/
│   │   │   ├── index.astro
│   │   │   └── [slug].astro
│   │   ├── competences.astro
│   │   └── contact.astro
│   ├── content/
│   │   ├── config.ts
│   │   ├── projets/
│   │   │   ├── projet-1.md
│   │   │   ├── projet-2.md
│   │   │   └── projet-3.md
│   │   └── competences/
│   │       ├── competence-frontend-1.md
│   │       ├── competence-backend-1.md
│   │       └── competence-soft-1.md
│   └── styles/
│       └── global.css
├── public/
│   ├── images/
│   │   └── projets/
│   └── cv/
│       └── CV_Baptiste_Dulieux.pdf
├── astro.config.mjs
├── tailwind.config.cjs
└── package.json
```

### 4. Copier les fichiers

Copiez tous les fichiers que je vous ai fournis dans leur emplacement respectif.

### 5. Personnaliser les informations

Remplacez les informations suivantes par les vôtres :

#### Dans `Footer.vue` et `contact.astro`
- `votre.email@edu.univ-fcomte.fr` → votre email universitaire
- `06 00 00 00 00` → votre numéro de téléphone
- `https://github.com/votre-username` → votre profil GitHub
- `https://linkedin.com/in/votre-profil` → votre profil LinkedIn

#### Dans `astro.config.mjs`
- `https://votre-portfolio.vercel.app` → votre future URL Vercel

### 6. Ajouter vos projets

Créez des fichiers Markdown dans `src/content/projets/` en utilisant les templates fournis.

**Exemple : `src/content/projets/mon-projet-stage.md`**

```markdown
---
title: "Stage S4 - Développement application web"
description: "Application de gestion développée durant mon stage"
technologies: ["Vue.js", "Node.js", "PostgreSQL"]
date: 2024-06-15
image: "/images/projets/stage-s4.jpg"
githubUrl: "https://github.com/username/projet"
featured: true
ordre: 1
---

## Contexte du projet
...
```

### 7. Ajouter vos compétences

Créez des fichiers Markdown dans `src/content/competences/`.

**Exemple : `src/content/competences/javascript.md`**

```markdown
---
title: "JavaScript / TypeScript"
category: "frontend"
level: "avance"
icon: "⚡"
ordre: 2
---

Développement JavaScript moderne avec ES6+ et TypeScript.

- Async/await et Promises
- Manipulation du DOM
- API Fetch
```

### 8. Ajouter vos images

Placez vos images dans `public/images/` :
- Photos de profil
- Captures d'écran de projets
- Autres visuels

### 9. Ajouter votre CV

Placez votre CV PDF dans `public/cv/CV_Baptiste_Dulieux.pdf`

## 🎨 Personnalisation des couleurs

Les couleurs vertes sont définies dans `tailwind.config.cjs`. Vous pouvez les modifier :

```javascript
colors: {
  primary: {
    50: '#f0fdf4',   // Plus clair
    500: '#22c55e',  // Couleur principale
    700: '#15803d',  // Plus foncé
  },
}
```

## 🚀 Commandes

```bash
# Développement
npm run dev

# Build pour production
npm run build

# Prévisualiser le build
npm run preview

# Vérifier les erreurs
npm run astro check
```

Le site sera disponible sur `http://localhost:4321`

## 📦 Déploiement sur Vercel

### Option 1 : Via GitHub (Recommandé)

1. Créez un repository GitHub :
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/votre-username/portfolio.git
git push -u origin main
```

2. Connectez-vous sur [Vercel](https://vercel.com)
3. Cliquez sur "New Project"
4. Importez votre repository GitHub
5. Vercel détectera automatiquement Astro
6. Cliquez sur "Deploy"

### Option 2 : Via Vercel CLI

```bash
# Installer Vercel CLI
npm i -g vercel

# Se connecter
vercel login

# Déployer
vercel

# Déployer en production
vercel --prod
```

## ✅ Checklist avant le rendu

- [ ] Toutes les informations personnelles sont à jour
- [ ] Au moins 3 projets sont documentés (dont le stage S4/S6)
- [ ] Les compétences techniques et soft skills sont listées
- [ ] Le CV est téléchargeable
- [ ] Les liens GitHub/LinkedIn fonctionnent
- [ ] Le site est responsive (testé sur mobile)
- [ ] Aucun lien cassé
- [ ] Les images sont optimisées
- [ ] Le site se charge rapidement (< 3s)
- [ ] Le formulaire de contact fonctionne
- [ ] Le site est déployé sur Vercel
- [ ] Le lien du portfolio est dans votre CV

## 🎯 Fonctionnalités

- ✅ Design moderne et responsive
- ✅ Navigation fluide
- ✅ Projets avec système de templates Markdown
- ✅ Compétences organisées par catégories
- ✅ Formulaire de contact avec validation
- ✅ CV téléchargeable
- ✅ Optimisé pour les performances
- ✅ SEO-friendly
- ✅ Accessibilité web

## 📝 Notes

- Les projets sont gérés via Markdown pour faciliter les mises à jour
- Les compétences peuvent être ajoutées simplement en créant de nouveaux fichiers .md
- Le design utilise une palette de couleurs vertes modernes
- Le site est optimisé pour le référencement

## 🆘 Besoin d'aide ?

- [Documentation Astro](https://docs.astro.build)
- [Documentation Vue.js](https://vuejs.org)
- [Documentation Tailwind CSS](https://tailwindcss.com)
- [Documentation Vercel](https://vercel.com/docs)

## 📧 Contact

Baptiste Dulieux - votre.email@edu.univ-fcomte.fr

---

Bon courage pour votre portfolio ! 🚀