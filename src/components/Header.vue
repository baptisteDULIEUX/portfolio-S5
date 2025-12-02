<template>
  <header class="fixed top-0 left-0 right-0 bg-white/80 backdrop-blur-md shadow-sm z-50">
    <nav class="container mx-auto px-4 py-4">
      <div class="flex items-center justify-between">
        <a href="/" class="text-2xl font-bold text-primary-600 hover:text-primary-700 transition">
          BD
        </a>

        <!-- Menu desktop -->
        <ul class="hidden md:flex items-center space-x-8">
          <li v-for="link in navLinks" :key="link.href">
            <a 
              :href="link.href" 
              class="text-gray-700 hover:text-primary-600 transition font-medium"
              :class="{ 'text-primary-600': isActive(link.href) }"
            >
              {{ link.label }}
            </a>
          </li>
          <li>
            <a 
              href="/cv/CV_Baptiste_DULIEUX.pdf" 
              download
              class="bg-primary-600 text-white px-4 py-2 rounded-lg hover:bg-primary-700 transition font-medium"
            >
              Télécharger CV
            </a>
          </li>
        </ul>

        <!-- Burger menu mobile -->
        <button 
          @click="toggleMenu" 
          class="md:hidden text-gray-700 focus:outline-none"
          aria-label="Toggle menu"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path 
              v-if="!menuOpen" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M4 6h16M4 12h16M4 18h16"
            />
            <path 
              v-else 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      <!-- Menu mobile -->
      <div 
        v-if="menuOpen" 
        class="md:hidden mt-4 pb-4 border-t border-gray-200"
      >
        <ul class="space-y-4 pt-4">
          <li v-for="link in navLinks" :key="link.href">
            <a 
              :href="link.href" 
              @click="closeMenu"
              class="block text-gray-700 hover:text-primary-600 transition font-medium"
              :class="{ 'text-primary-600': isActive(link.href) }"
            >
              {{ link.label }}
            </a>
          </li>
          <li>
            <a 
              href="/cv/CV_Baptiste_Dulieux.pdf" 
              download
              class="block bg-primary-600 text-white px-4 py-2 rounded-lg hover:bg-primary-700 transition font-medium text-center"
            >
              Télécharger CV
            </a>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const menuOpen = ref(false);

const navLinks = [
  { href: '/', label: 'Accueil' },
  { href: '/projets', label: 'Projets' },
  { href: '/competences', label: 'Compétences' },
  { href: '/contact', label: 'Contact' },
];

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value;
};

const closeMenu = () => {
  menuOpen.value = false;
};

const isActive = (href: string) => {
  if (typeof window !== 'undefined') {
    const path = window.location.pathname;
    return path === href || (href !== '/' && path.startsWith(href));
  }
  return false;
};
</script>