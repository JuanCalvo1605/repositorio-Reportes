import { createRouter, createWebHistory } from 'vue-router'
import login from '../views/login.vue'
import reportes from '../views/reportes.vue'
const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			path: '/',
			component: login
		},
		{
			path: '/about',
			component: () => import('../views/about.vue')
		},
        {
            path: '/Prueba',
            component: reportes
        },
	],
})

export default router