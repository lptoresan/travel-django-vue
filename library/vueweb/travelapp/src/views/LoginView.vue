<template>
    <b-row class="vh-100 vw-100 row-login">
        <b-col sm="5" class="d-flex justify-content-center align-items-center left-login">
            <div class="col-8">
                <h2 class="mb-3 login-title">Login</h2>
                <b-form>
                    <b-form-group
                        label="Email"
                        label-for="email">
                    <b-form-input
                        id="email"
                        type="text"
                        placeholder="Insert your email"
                        autocomplete="off"
                        v-model.trim="$v.form.email.$model"
                        :state="getValidation('email')">
                    </b-form-input>
                    </b-form-group>

                    <b-form-group
                        label-for="password"
                    >
                    
                    <b-form-input
                        id="password"
                        type="password"
                        placeholder="Insert your password"
                        v-model.trim="$v.form.password.$model"
                        :state="getValidation('password')">
                    </b-form-input>
                    </b-form-group>

                    <b-button id="login-button" 
                        type="button"
                        variant="primary"
                        block
                        @click="loginUser">
                        <i class="fas fa-sign-in-alt"></i> Login
                    </b-button>

                    <b-button id="register-button"
                        type="button"
                        variant="outline-light"
                        block
                        @click="registerUser">
                        <i class="fas fa-user-plus"></i> Register
                    </b-button>
                </b-form>
            </div>
        </b-col>
        <b-col sm="7" class="d-flex justify-content-center align-items-center">
            <img src="../assets/images/login-travel.svg" style="max-width: 100%; height: auto;"/>
        </b-col>
    </b-row>
</template>

<script>
import axios from 'axios';
import { required, minLength, email } from "vuelidate/lib/validators";
import ToastMixin from '../mixins/toastMixin.js'

    export default {
        mixins: [ToastMixin],

        data(){
            return {
                form: {
                    email: "",
                    password: ""
                }
            }
        },

    validations: {
        form: {
            email: {
                required,
                email
            },

            password: {
                required, 
                minLength: minLength(6)
            },
        }
    },

    methods: {
            loginUser(){
            this.$v.$touch();
            if(this.$v.$error) {
                return;
            }

            axios.get('http://127.0.0.1:8000/user/', { timeout: 10000 })                
                .then((response) => {
                    const users = response.data;
                    console.log('Retrieved user:', users);
                    const user = users.find(user => user.email === this.form.email);
                    console.log('User:', user)
                    if (user) {
                        if (user.password === this.form.password){
                            console.log('Login sucessfull.')
                            localStorage.setItem('token', user.id_user);
                            this.$router.push({name: "list"});
                        } else {
                            console.error('Email or password is incorrect!');
                            this.showToast("danger", "Error!", "Email or password is incorrect!");
                            this.clearForm();
                        }
                    } else {
                        console.error('Email or password is incorrect!');
                        this.showToast("danger", "Error!", "Email or password is incorrect!");
                        this.clearForm();
                    }
                })
            .catch((error) => {
            console.error('Email or password is incorrect!', error);    
            this.showToast("danger", "Error!", "Email or password is incorrect!");
            this.clearForm();
            });
        },

        registerUser(){
            this.$router.push({name: 'register'})
        },

        clearForm() {
            this.form = {
                email: "",
                password: ""
            }
        },

        getValidation(field){
            if(this.$v.form.$dirty == false) {
                return null;
            }

            return !this.$v.form[field].$error;
        }
        }
    }
</script>

<style>

*,
*::after,
*::before{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    text-decoration: none;
}

.login-title{
    text-align: center;
    justify-items: center;
    font-size: 40px;
    font-weight: bolder;
    text-shadow: 2px 2px 2px #00aeff;
}

.row-login {
    margin-left: 0;
}

.left-login{
    background-image: linear-gradient(180deg, #604fbd, #170830);
    color: #ffffff;
}

a {
    color: #ffffff;
    text-decoration: none;
}

a:visited {
    color: #ffffff;
    text-decoration: none;
}

a:hover {
    color: #d0ccd6;
}

</style>