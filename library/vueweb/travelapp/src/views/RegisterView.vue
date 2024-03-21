<template>
    <b-row class="vh-100 vw-100 row-login">
        <b-col sm="7" class="d-flex justify-content-center align-items-center">
            <img src="../assets/images/register-travel.svg" style="max-width: 100%; height: auto;"/>
        </b-col>
        <b-col sm="5" class="d-flex justify-content-center align-items-center right-register">
            <div class="col-8">
                <h2 class="mb-3 login-title">Register</h2>
                <b-form>
                    <b-form-group
                        label="Name"
                        label-for="name">
                    <b-form-input
                        id="name"
                        type="text"
                        placeholder="Insert your name"
                        autocomplete="off"
                        v-model.trim="$v.form.name.$model"
                        :state="getValidation('name')">
                    </b-form-input>
                    </b-form-group>

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
                        label="Password"
                        label-for="password">
                    <b-form-input
                        id="password"
                        type="password"
                        placeholder="Insert your password"
                        v-model.trim="$v.form.password.$model"
                        :state="getValidation('password')">
                    </b-form-input>
                    </b-form-group>

                    <b-form-group
                        label="Re-tipe your passaword"
                        label-for="confirmepassword">
                    <b-form-input
                        id="confirmpassword"
                        type="password"
                        placeholder="Re-tipe your password"
                        v-model.trim="$v.form.confirmpassword.$model"
                        :state="getValidation('confirmpassword')">
                    </b-form-input>
                    </b-form-group>

                    <b-button id="register-button"
                        type="button"
                        variant="primary"
                        block
                        @click="registerUser">
                        <i class="fas fa-user-plus"></i> Register
                    </b-button>

                    <b-button
                        type="button"
                        variant="outline-light"
                        block
                        @click="goToLogin"
                        ><i class="fas fa-arrow-left"></i> Go back
                    </b-button>
                </b-form>
            </div>
        </b-col>
    </b-row>
</template>

<script>
import axios from 'axios';
import { required, minLength, email, sameAs } from "vuelidate/lib/validators";
import ToastMixin from '../mixins/toastMixin.js'

    export default {
        mixins: [ToastMixin],

        data(){
            return {
                form: {
                    name: "",
                    email: "",
                    password: "",
                    confirmpassword: ""
                }
            }
        },

    validations: {
        form: {
            name: {
                required,
                minLength: minLength(3)
            },
            email: {
                required,
                email
            },

            password: {
                required, 
                minLength: minLength(6)
            },
            confirmpassword:{
                required,
                sameAsPassword: sameAs('password')
            }
        }
    },

    methods: {
        registerUser(){
            this.$v.$touch();
            if(this.$v.$error) {
                return;
            }

            const formData = {
                name: this.form.name,
                email: this.form.email,
                password: this.form.password
            };

            axios.post('http://127.0.0.1:8000/user/', formData, { timeout: 10000 })
                .then((response) => {
                    console.log('User saved successfully:', response);
                    this.showToast("success", "Success!", "User registered sucessfully.");
                    this.goToLogin();
                })
            .catch((error) => {
                this.showToast("danger", "Error!", "Error saving user. Check the fields and submit again.");
                console.error('Error saving user:', error);
            });
        },

        getValidation(field){
            if(this.$v.form.$dirty == false) {
                return null;
            }

            return !this.$v.form[field].$error;
        },

        goToLogin() {
            this.$router.push({name: 'login'})
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

.right-register{
    background-image: linear-gradient(180deg, #170830, #604fbd);
    color: #ffffff;
}


</style>