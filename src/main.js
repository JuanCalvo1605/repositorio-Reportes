import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import Login from './views/login.vue';
import home from './views/Home.vue';
import vistaReportes from './views/vista_informes.vue';
import ReporteDetalle from './views/reportes.vue';

//import { BootstrapVue } from 'bootstrap-vue'; // Solo importa BootstrapVue, no IconsPlugin
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

// Importa BootstrapVue sin IconsPlugin
//createApp.use(BootstrapVue);

// Configura Vue Router
const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: Login
        },
        {
            path: '/home',
            component: home
        },
        {
            path: '/vistaReportes',
            component: vistaReportes
        },
        {
            path: '/reportes-detalle/:id_reporte',
            name: 'ReporteDetalle',
            component: ReporteDetalle
        },
    ]
});

// Crea la instancia de la aplicación Vue y utiliza el componente App como componente raíz
const app = createApp(App);

// Utiliza Vue Router en la aplicación
app.use(router);

// Monta la aplicación en el elemento con el ID #app
app.mount('#app');

export default router;
