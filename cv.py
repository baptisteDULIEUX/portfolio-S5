#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

def create_cv():
    # Configuration
    filename = "CV_Baptiste_DULIEUX.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # Couleurs du portfolio
    primary_color = HexColor('#16a34a')  # primary-600
    primary_light = HexColor('#dcfce7')  # primary-100
    dark_color = HexColor('#111827')
    gray_color = HexColor('#6b7280')
    
    # Marges
    margin_left = 2*cm
    margin_right = width - 2*cm
    y_position = height - 2*cm
    
    # ========== EN-TÊTE ==========
    # Nom
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(dark_color)
    c.drawString(margin_left, y_position, "Baptiste DULIEUX")
    y_position -= 0.8*cm
    
    # Titre
    c.setFont("Helvetica", 14)
    c.setFillColor(primary_color)
    c.drawString(margin_left, y_position, "Étudiant Développeur Web - BUT Informatique 3ème année")
    y_position -= 1.2*cm
    
    # Informations de contact
    c.setFont("Helvetica", 9)
    c.setFillColor(gray_color)
    contact_info = [
        "7 rue des Capucins, 90000 Belfort",
        "06 15 28 09 66",
        "baptiste.dulieux@edu.univ-fcomte.fr",
        "github.com/baptisteDULIEUX"
    ]
    
    for info in contact_info:
        c.drawString(margin_left, y_position, info)
        y_position -= 0.5*cm
    
    y_position -= 0.5*cm
    
    # Ligne de séparation
    c.setStrokeColor(primary_light)
    c.setLineWidth(1)
    c.line(margin_left, y_position, margin_right, y_position)
    y_position -= 0.8*cm
    
    # ========== FORMATION ==========
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(primary_color)
    c.drawString(margin_left, y_position, "🎓 FORMATION")
    y_position -= 0.6*cm
    
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(dark_color)
    c.drawString(margin_left + 0.3*cm, y_position, "BUT Informatique - Parcours Réalisation d'applications")
    y_position -= 0.5*cm
    
    c.setFont("Helvetica", 9)
    c.setFillColor(gray_color)
    c.drawString(margin_left + 0.3*cm, y_position, "IUT Nord Franche-Comté, Belfort • 2023 - 2025")
    y_position -= 0.4*cm
    c.drawString(margin_left + 0.3*cm, y_position, "Spécialisation en développement web et conception d'applications")
    y_position -= 0.8*cm
    
    # ========== EXPÉRIENCE PROFESSIONNELLE ==========
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(primary_color)
    c.drawString(margin_left, y_position, "💼 EXPÉRIENCE PROFESSIONNELLE")
    y_position -= 0.6*cm
    
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(dark_color)
    c.drawString(margin_left + 0.3*cm, y_position, "Stage - SAS Financière The Box")
    y_position -= 0.5*cm
    
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(gray_color)
    c.drawString(margin_left + 0.3*cm, y_position, "2ème année BUT • Holding financière")
    y_position -= 0.5*cm
    
    c.setFont("Helvetica", 9)
    missions = [
        "• Conception et développement d'une application de gestion du personnel",
        "• Mise en place d'une interface web moderne et intuitive",
        "• Déploiement et mise en production de l'application"
    ]
    for mission in missions:
        c.drawString(margin_left + 0.3*cm, y_position, mission)
        y_position -= 0.4*cm
    
    y_position -= 0.4*cm
    
    # ========== COMPÉTENCES TECHNIQUES ==========
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(primary_color)
    c.drawString(margin_left, y_position, "🛠️ COMPÉTENCES TECHNIQUES")
    y_position -= 0.6*cm
    
    # Langages
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(dark_color)
    c.drawString(margin_left + 0.3*cm, y_position, "Langages de programmation")
    y_position -= 0.5*cm
    
    c.setFont("Helvetica", 9)
    c.setFillColor(gray_color)
    c.drawString(margin_left + 0.3*cm, y_position, "Java (avancé) • Python (avancé) • C/C++ (intermédiaire) • JavaScript • PHP")
    y_position -= 0.6*cm
    
    # Frontend
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(dark_color)
    c.drawString(margin_left + 0.3*cm, y_position, "Développement Frontend")
    y_position -= 0.5*cm
    
    c.setFont("Helvetica", 9)
    c.setFillColor(gray_color)
    c.drawString(margin_left + 0.3*cm, y_position, "HTML5, CSS3, Tailwind CSS • Vue.js, Astro • Responsive Design • Accessibilité (ARIA)")
    y_position -= 0.6*cm
    
    # Backend
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(dark_color)
    c.drawString(margin_left + 0.3*cm, y_position, "Développement Backend & Bases de données")
    y_position -= 0.5*cm
    
    c.setFont("Helvetica", 9)
    c.setFillColor(gray_color)
    c.drawString(margin_left + 0.3*cm, y_position, "Node.js, Express • Spring Boot, Hibernate • MySQL, PostgreSQL • API REST")
    y_position -= 0.6*cm
    
    # Outils
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(dark_color)
    c.drawString(margin_left + 0.3*cm, y_position, "Outils & Méthodologies")
    y_position -= 0.5*cm
    
    c.setFont("Helvetica", 9)
    c.setFillColor(gray_color)
    c.drawString(margin_left + 0.3*cm, y_position, "Git/GitHub • Docker • VS Code • Méthodes Agiles • Tests unitaires (JUnit, pytest)")
    y_position -= 0.8*cm
    
    # ========== PROJETS ACADÉMIQUES ==========
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(primary_color)
    c.drawString(margin_left, y_position, "🚀 PROJETS ACADÉMIQUES & PERSONNELS")
    y_position -= 0.6*cm
    
    projets = [
        {
            "titre": "Portfolio Personnel",
            "desc": "Site web moderne avec Astro et Vue.js, déployé sur Vercel • Design responsive avec Tailwind CSS",
            "tech": "Astro, Vue.js, Tailwind CSS"
        },
        {
            "titre": "Applications Web Full-Stack",
            "desc": "Développement d'applications complètes avec gestion utilisateurs et bases de données",
            "tech": "Java Spring Boot, Vue.js, PostgreSQL"
        },
        {
            "titre": "Projets Open Source",
            "desc": "Contributions sur GitHub et développement de projets personnels",
            "tech": "Python, JavaScript, Git"
        }
    ]
    
    for projet in projets:
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(dark_color)
        c.drawString(margin_left + 0.3*cm, y_position, projet["titre"])
        y_position -= 0.4*cm
        
        c.setFont("Helvetica", 9)
        c.setFillColor(gray_color)
        c.drawString(margin_left + 0.3*cm, y_position, projet["desc"])
        y_position -= 0.35*cm
        
        c.setFont("Helvetica-Oblique", 8)
        c.setFillColor(primary_color)
        c.drawString(margin_left + 0.3*cm, y_position, f"Technologies : {projet['tech']}")
        y_position -= 0.6*cm
    
    # ========== LANGUES & CENTRES D'INTÉRÊT ==========
    y_position -= 0.2*cm
    
    # Ligne de séparation
    c.setStrokeColor(primary_light)
    c.setLineWidth(1)
    c.line(margin_left, y_position, margin_right, y_position)
    y_position -= 0.6*cm
    
    # Langues
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(dark_color)
    c.drawString(margin_left, y_position, "🌍 Langues")
    
    # Centres d'intérêt
    c.drawString(margin_left + 7*cm, y_position, "⚡ Centres d'intérêt")
    y_position -= 0.5*cm
    
    c.setFont("Helvetica", 9)
    c.setFillColor(gray_color)
    c.drawString(margin_left, y_position, "Français : Langue maternelle")
    c.drawString(margin_left + 7*cm, y_position, "Sport : VTT, Escalade, Course à pied")
    y_position -= 0.4*cm
    c.drawString(margin_left, y_position, "Anglais : Niveau technique")
    c.drawString(margin_left + 7*cm, y_position, "Veille technologique active")
    
    # Footer
    y_position = 2*cm
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(gray_color)
    c.drawCentredString(width/2, y_position, "En recherche de stage de fin d'études • Disponible dès maintenant")
    y_position -= 0.4*cm
    c.drawCentredString(width/2, y_position, "Portfolio : portfolio-s5-two.vercel.app")
    
    # Sauvegarder
    c.save()
    print(f"✅ CV créé avec succès : {filename}")

if __name__ == "__main__":
    create_cv()