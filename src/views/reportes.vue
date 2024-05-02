<template>
    <sidebar />
    
    <div class="container">
        <h1 v-html="nombre"></h1>
        <div class="iframe-container">
            <div v-html="codigoPBI" class="iframe-content"></div>
        </div>
    </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';
import axios from 'axios';
export default {
    components:{
        sidebar
    },
    data() {
        return {
            codigoPBI: ''
        };
    },
    mounted() {
        this.obtenerCodigoPBI();
    },
    methods: {
        async obtenerCodigoPBI() {
            try {
                const response = await axios.get('http://172.19.10.8:5000/informe');
                this.codigoPBI = response.data.codigo_pwi; // Establecer el HTML del iframe
                this.nombre = response.data.nombre
            } catch (error) {
                console.error('Error al obtener el código de Power BI:', error);
            }
        }
    }
}

</script>

<style>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    h1{
        padding-bottom: 25px;
        padding-top: 25px;
    }
}

/*
.iframe-container {
    position: relative;
    width: 100%;
    padding-top: 56.25%; /* Proporción 16:9 para un iframe responsive */
    margin-bottom: 20px; /* Espacio entre el iframe y el título */
    overflow: hidden; /* Evita que el iframe se desborde 
}
*/
.iframe-content {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transition: transform 0.3s; /* Añade una transición suave */
}


</style>
