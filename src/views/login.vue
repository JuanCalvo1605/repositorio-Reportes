<template>
    <div class="sidenav">
        <div class="login-main-text">
            <h2>Repositorio Reportes<br> Inicio de Sesion</h2>
            <p>Consulte sus reportes </p>
        </div>
    </div>
    <div class="main">
        <div class="col-md-6 col-sm-12">
            <div class="login-form">
            <form @submit.prevent="enviarCredenciales">
                <h2>Ingreso</h2>
                <div class="form-group">
                    <label>Usuario</label>
                    <input type="text" class="form-control" placeholder="Por favor ingrese su usuario" v-model="correo">
                </div>
                <div class="form-group2">
                    <label>Contraseña</label>
                    <input type="password" class="form-control" placeholder="Por favor ingrese su contraseña" v-model="contra">
                </div>
                <button type="submit" class="btn btn-black">Login</button>
                <button type="submit" class="btn btn-secondary">Olvido su contraseña</button>
            </form>
            </div>
        </div>
        <div v-if="error" class="alert alert-danger"><h1> error{{ error }}</h1></div> <!-- Mostrar mensaje de error -->
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return{
            correo: '',
            contra: '',
            error:''

        };
    },
    methods:{
        async enviarCredenciales() {
            try {
                const response = await axios.get('http://172.19.10.8:5000/login', {
                params: {
                correo: this.correo,
                contra: this.contra
            }
        });
        
        const { valido, error } = response.data;

        if (error) {
            this.error = error;  // Mostrar mensaje de error si existe
        } else if (valido) {
            this.$router.push('/home');
        }
        } catch (error) {
            console.error('Error en enviarCredenciales:', error);
            this.error = 'Error de conexión';
        }
        }
    }

}
</script>

<style>
body {
    font-family: "Lato", sans-serif;
}

.main-head{
    height: 150px;
    background: #FFF;
}

.sidenav {
    height: 100%;
    background-color: #000;
    overflow-x: hidden;
    padding-top: 20px;
}
.main {
    padding: 0px 10px;
}

@media screen and (max-height: 450px) {
    .sidenav {padding-top: 15px;}
}

@media screen and (max-width: 450px) {
    .login-form{
        margin-top: 10%;
    }

    .register-form{
        margin-top: 10%;
    }
}

@media screen and (min-width: 768px){
    .main{
        margin-left: 40%; 
    }

    .sidenav{
        width: 40%;
        position: fixed;
        z-index: 1;
        top: 0;
        left: 0;
    }

    .login-form{
        margin-top: 80%;
    }

    .register-form{
        margin-top: 20%;
    }
}

.login-main-text{
    margin-top: 20%;
    padding: 60px;
    color: #fff;
}

.login-main-text h2{
    font-weight: 300;
}

form{
    padding-left: 35px;
    text-align: left;
    width: 500px;
}
.form-control:hover{
    background-color: #adb8b9;
    transition: 2s ;
}
form .btn-secondary{
    margin-top: 15px;
    width: 220px;
}
form .btn-black{
    margin-top: 15px;
    background-color: #000;
    color: #FFF;
    width: 225px;
    margin-right: 20px;
}
.form-group2 {
    margin-top: 25px;
}
form .btn-black:hover{
    transition: 2s;
    background-color: #adb8b9;
    color: #000;
}
form .btn-secondary:hover{
    transition: 2s;
    background-color: #adb8b9;
    color: #000;
}
</style>