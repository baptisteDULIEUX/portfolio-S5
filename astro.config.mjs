// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
import vue from "@astrojs/vue";
import mdx from "@astrojs/mdx";

// https://astro.build/config
export default defineConfig({
  // Les trois intégrations doivent être ici
  integrations: [tailwind(), vue(), mdx()], 
});