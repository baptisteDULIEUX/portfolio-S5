import { defineCollection, z } from 'astro:content';

const projetsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    technologies: z.array(z.string()),
    date: z.date(),
    image: z.string().optional(),
    githubUrl: z.string().optional(),
    liveUrl: z.string().optional(),
    featured: z.boolean().default(false),
    ordre: z.number().default(999),
  }),
});

const competencesCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    category: z.enum(['frontend', 'backend', 'tools', 'soft-skills','langages']),
    level: z.enum(['debutant', 'intermediaire', 'avance', 'expert']).optional(),
    icon: z.string().optional(),
    ordre: z.number().default(999),
  }),
});

export const collections = {
  projets: projetsCollection,
  competences: competencesCollection,
};