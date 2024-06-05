<template>
    <sidebar />
    <div class="container">
        <h1 class="title">Reportes</h1>
        <ul class="report-list">  
            <li v-for="reporte in reportes" :key="reporte.id_reporte"> 
                <router-link :to="{name:'ReporteDetalle', params:{id_reporte: reporte.id_reporte}}">
                    <a>{{ reporte.nombre }}</a>
                </router-link>
            </li>
        </ul>
    </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';
import axios from 'axios';
export default {
    components:{
        sidebar
    },data() {
        return {
            reportes: []
        };
    },
    created(){
        this.obtenerReportes();
    },
    methods: {
        async obtenerReportes() {
            try {
                const response = await axios.get('http://172.19.10.8:5000/');
                this.reportes  = response.data;
                this.id_reporte = response.data
                console.log(this.reportes)
            } catch (error) {
                console.error('Error al obtener el código de Power BI:', error);
            }
        }
        
    }
}
</script>

<style>
.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

.report-list {
    list-style-type: none;
    padding: 0;
}
.report-item {
    margin-bottom: 10px;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 5px;
}
</style>