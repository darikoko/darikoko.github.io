import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'PrunePy',
			favicon: '/favicon.png',
			logo: {
				src: './src/assets/prune.png',
			  },
			customCss: [
				// Relative path to your custom CSS file
				'./src/styles/styles.css',
			],
			social: {
				github: 'https://github.com/darikoko/prunepy',
			},
			sidebar: [
				{
					label: 'Get Started',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'What is PrunePy', slug: 'get-started/what-is-prune' },
						{ label: 'First Project', slug: 'get-started/first-project' },
					],
				},
				{
					label: 'Templating',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'p-text', slug: 'templating/p-text' },
						{ label: 'p-html', slug: 'templating/p-html' },
						{ label: 'p-show', slug: 'templating/p-show' },
						{ label: 'p-if', slug: 'templating/p-if' },
						{ label: 'p-for', slug: 'templating/p-for' },
						{ label: 'p-bind (or :)', slug: 'templating/p-bind' },
						{ label: 'p-on (or @)', slug: 'templating/p-on' },
						{ label: 'p-ref', slug: 'templating/p-ref' },
					]
				},
				{
					label: 'Reactivity',
					items: [
						{ label: '@notify', slug: 'reactivity/notify' },
						{ label: '@notify_async', slug: 'reactivity/notify-async' },
					]
				},
			],
		}),
	],
});
