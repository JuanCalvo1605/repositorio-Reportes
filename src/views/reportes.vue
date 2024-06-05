<template>
    <sidebar />
    
    <div class="container">
        <h1 v-html="nombre"></h1>
        <div class="iframe-container">
            <div v-html="codigo" class="iframe-content"></div>
        </div>
    </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';
import axios from 'axios';
export default {
    name:'ReporteDetalle',
    components:{
        sidebar
    },
    data() {
        
        return {
            id: this.$route.params.id_reporte,
            codigo: '',
            nombre: ''
        };
    },
    mounted() {
        console.log(this.id_reporte)
        this.obtenerCodigoPBI();
    },
    methods: {
        async obtenerCodigoPBI() {
            try {
                console.log('ID que se está enviando:', this.id);
                const response = await axios.get('http://172.19.10.8:5000/informe',{
                    params:{id_reporte: this.id}
                });
                this.codigo = response.data.codigo; // Establecer el HTML del iframe
                this.nombre = response.data.nombre
                console.log(this.nombre)
                //this.codigoPBI = data.codigo_pwi;
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
.iframe-content {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transition: transform 0.3s; /* Añade una transición suave */
}


</style>
