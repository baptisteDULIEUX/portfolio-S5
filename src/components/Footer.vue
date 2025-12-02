<template>
  <footer class="bg-gray-900 text-gray-300 py-12 mt-20">
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
        <!-- À propos -->
        <div>
          <h3 class="text-white text-lg font-semibold mb-4">Baptiste Dulieux</h3>
          <p class="text-sm leading-relaxed">
            Étudiant en 3ème année de BUT Informatique à l'IUT Nord Franche-Comté, 
            passionné par le développement web.
          </p>
        </div>

        <!-- Navigation rapide -->
        <div>
          <h3 class="text-white text-lg font-semibold mb-4">Navigation</h3>
          <ul class="space-y-2">
            <li v-for="link in navLinks" :key="link.href">
              <a 
                :href="link.href" 
                class="text-sm hover:text-primary-400 transition"
              >
                {{ link.label }}
              </a>
            </li>
          </ul>
        </div>

        <!-- Contact -->
        <div>
          <h3 class="text-white text-lg font-semibold mb-4">Contact</h3>
          <ul class="space-y-2 text-sm">
            <li>
              <a 
                href="mailto:votre.email@edu.univ-fcomte.fr" 
                class="hover:text-primary-400 transition"
              >
                baptiste.dulieux@edu.univ-fcomte.fr
              </a>
            </li>
            <li>
              <a 
                href="tel:+33600000000" 
                class="hover:text-primary-400 transition"
              >
                06 15 28 09 66
              </a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Séparateur -->
      <div class="border-t border-gray-800 pt-8">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <p class="text-sm mb-4 md:mb-0">
            © {{ currentYear }} Baptiste Dulieux. Tous droits réservés.
          </p>
          
          <!-- Réseaux sociaux -->
          <div class="flex space-x-4">
            <a 
              href="https://github.com/baptisteDULIEUX" 
              target="_blank"
              rel="noopener noreferrer"
              class="hover:text-primary-400 transition"
              aria-label="GitHub"
            >
              <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const currentYear = computed(() => new Date().getFullYear());

const navLinks = [
  { href: '/', label: 'Accueil' },
  { href: '/projets', label: 'Projets' },
  { href: '/competences', label: 'Compétences' },
  { href: '/contact', label: 'Contact' },
];
</script>