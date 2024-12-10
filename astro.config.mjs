import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'PrunePy',
			customCss: [
				// Relative path to your custom CSS file
				'./src/styles/styles.css',
			  ],
			social: {
				github: 'https://github.com/darikoko/prunepy',
			},
			sidebar: [
				{
					label: 'Guides',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Example Guide', slug: 'guides/example' },
					],
				},
				{
					label: 'Templating',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'p-text', slug: 'templating/p-text' },
						{ label: 'p-show', slug: 'templating/p-show' },
						{ label: 'p-if', slug: 'templating/p-if' },
						{ label: 'p-on (or @)', slug: 'templating/p-on' },
						{ label: 'p-for', slug: 'templating/p-for' },
						{ label: 'p-html', slug: 'templating/p-html' },
						{ label: 'p-ref', slug: 'templating/p-ref' },
						{ label: 'Example Guide', slug: 'guides/example' },
					]
				},
			],
		}),
	],
});
