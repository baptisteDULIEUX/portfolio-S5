<template>
  <form @submit.prevent="handleSubmit" class="space-y-6">
    <!-- Nom -->
    <div>
      <label for="name" class="block text-sm font-semibold text-gray-700 mb-2">
        Nom complet *
      </label>
      <input
        id="name"
        v-model="formData.name"
        type="text"
        required
        class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 outline-none transition"
        :class="{ 'border-red-500': errors.name }"
        placeholder="Votre nom"
      />
      <p v-if="errors.name" class="mt-1 text-sm text-red-600">{{ errors.name }}</p>
    </div>

    <!-- Email -->
    <div>
      <label for="email" class="block text-sm font-semibold text-gray-700 mb-2">
        Email *
      </label>
      <input
        id="email"
        v-model="formData.email"
        type="email"
        required
        class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 outline-none transition"
        :class="{ 'border-red-500': errors.email }"
        placeholder="votre.email@exemple.com"
      />
      <p v-if="errors.email" class="mt-1 text-sm text-red-600">{{ errors.email }}</p>
    </div>

    <!-- Sujet -->
    <div>
      <label for="subject" class="block text-sm font-semibold text-gray-700 mb-2">
        Sujet *
      </label>
      <input
        id="subject"
        v-model="formData.subject"
        type="text"
        required
        class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 outline-none transition"
        :class="{ 'border-red-500': errors.subject }"
        placeholder="L'objet de votre message"
      />
      <p v-if="errors.subject" class="mt-1 text-sm text-red-600">{{ errors.subject }}</p>
    </div>

    <!-- Message -->
    <div>
      <label for="message" class="block text-sm font-semibold text-gray-700 mb-2">
        Message *
      </label>
      <textarea
        id="message"
        v-model="formData.message"
        required
        rows="6"
        class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 outline-none transition resize-none"
        :class="{ 'border-red-500': errors.message }"
        placeholder="Votre message..."
      ></textarea>
      <p v-if="errors.message" class="mt-1 text-sm text-red-600">{{ errors.message }}</p>
    </div>

    <!-- Message de succès -->
    <div v-if="submitStatus === 'success'" class="bg-green-50 border border-green-200 rounded-lg p-4">
      <p class="text-green-800 flex items-center">
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
        </svg>
        Message envoyé avec succès ! Je vous répondrai dans les plus brefs délais.
      </p>
    </div>

    <!-- Message d'erreur -->
    <div v-if="submitStatus === 'error'" class="bg-red-50 border border-red-200 rounded-lg p-4">
      <p class="text-red-800 flex items-center">
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
        Une erreur est survenue. Veuillez réessayer ou me contacter directement par email.
      </p>
    </div>

    <!-- Bouton submit -->
    <button
      type="submit"
      :disabled="isSubmitting"
      class="w-full bg-primary-600 text-white py-3 px-6 rounded-lg hover:bg-primary-700 transition font-semibold disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center justify-center"
    >
      <svg
        v-if="isSubmitting"
        class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
        fill="none"
        viewBox="0 0 24 24"
      >
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
      </svg>
      {{ isSubmitting ? 'Envoi en cours...' : 'Envoyer le message' }}
    </button>

    <p class="text-sm text-gray-600 text-center">
      * Champs obligatoires
    </p>
  </form>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';

interface FormData {
  name: string;
  email: string;
  subject: string;
  message: string;
}

interface FormErrors {
  name?: string;
  email?: string;
  subject?: string;
  message?: string;
}

const formData = reactive<FormData>({
  name: '',
  email: '',
  subject: '',
  message: '',
});

const errors = reactive<FormErrors>({});
const isSubmitting = ref(false);
const submitStatus = ref<'idle' | 'success' | 'error'>('idle');

const validateForm = (): boolean => {
  // Réinitialiser les erreurs
  Object.keys(errors).forEach(key => delete errors[key as keyof FormErrors]);

  let isValid = true;

  // Validation du nom
  if (!formData.name.trim()) {
    errors.name = 'Le nom est requis';
    isValid = false;
  } else if (formData.name.trim().length < 2) {
    errors.name = 'Le nom doit contenir au moins 2 caractères';
    isValid = false;
  }

  // Validation de l'email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!formData.email.trim()) {
    errors.email = 'L\'email est requis';
    isValid = false;
  } else if (!emailRegex.test(formData.email)) {
    errors.email = 'L\'email n\'est pas valide';
    isValid = false;
  }

  // Validation du sujet
  if (!formData.subject.trim()) {
    errors.subject = 'Le sujet est requis';
    isValid = false;
  } else if (formData.subject.trim().length < 3) {
    errors.subject = 'Le sujet doit contenir au moins 3 caractères';
    isValid = false;
  }

  // Validation du message
  if (!formData.message.trim()) {
    errors.message = 'Le message est requis';
    isValid = false;
  } else if (formData.message.trim().length < 10) {
    errors.message = 'Le message doit contenir au moins 10 caractères';
    isValid = false;
  }

  return isValid;
};

const handleSubmit = async () => {
  if (!validateForm()) {
    return;
  }

  isSubmitting.value = true;
  submitStatus.value = 'idle';

  try {
    // Simulation d'envoi (à remplacer par votre logique d'envoi réelle)
    // Vous pouvez utiliser un service comme Formspree, EmailJS, ou votre propre API
    
    // Exemple avec mailto (simple mais ouvre le client mail)
    const mailtoLink = `mailto:votre.email@edu.univ-fcomte.fr?subject=${encodeURIComponent(formData.subject)}&body=${encodeURIComponent(`De: ${formData.name} (${formData.email})\n\n${formData.message}`)}`;
    
    // Simuler un délai
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    // Ouvrir le client mail
    window.location.href = mailtoLink;
    
    submitStatus.value = 'success';
    
    // Réinitialiser le formulaire
    formData.name = '';
    formData.email = '';
    formData.subject = '';
    formData.message = '';
    
    // Masquer le message de succès après 5 secondes
    setTimeout(() => {
      submitStatus.value = 'idle';
    }, 5000);
    
  } catch (error) {
    console.error('Erreur lors de l\'envoi:', error);
    submitStatus.value = 'error';
  } finally {
    isSubmitting.value = false;
  }
};
</script>