<template>
    <div class="container mt-4">
        <b-form>
            <b-form-group label="Name" label-for="name">
               <b-form-input
                  id="name"
                  v-model="form.name"
                  type="text"
                  placeholder="Insert the name"
                  required
                  autocomplete="off"
                  maxlength="20"
               ></b-form-input> 
            </b-form-group>

            <b-form-group label="Price Comfort" label-for="price_confort">
                <b-form-input
                    id="price_confort"
                    v-model="form.price_confort"
                    type="number"
                    step="0.01"
                    placeholder="Insert the price for comfort"
                    required
                    autocomplete="off"
                ></b-form-input>
            </b-form-group>

            <b-form-group label="Price Econ" label-for="price_econ">
                <b-form-input
                    id="price_econ"
                    v-model="form.price_econ"
                    type="number"
                    step="0.01"
                    placeholder="Insert the price for econ"
                    required
                    autocomplete="off"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                label="City"
                label-for="city">
               <b-form-textarea
                  id="city"
                  v-model="form.city"
                  type="text"
                  placeholder="Insert the city"
                  required
                  autocomplete="off"
                  maxlength="40">
               </b-form-textarea> 
            </b-form-group>

            <b-form-group
                label="Duration"
                label-for="duration">
                <b-form-input
                    id="duration"
                    v-model="form.duration"
                    type="number"
                    step="0.01"
                    placeholder="Insert the duration"
                    required
                    autocomplete="off">
                </b-form-input>
            </b-form-group>

            <b-form-group
                label="Seat"
                label-for="seat">
               <b-form-textarea
                  id="seat"
                  v-model="form.seat"
                  type="text"
                  placeholder="Insert the seat"
                  required
                  autocomplete="off"
                  maxlength="3">
               </b-form-textarea> 
            </b-form-group>

            <b-form-group
                label="Bed"
                label-for="bed">
               <b-form-textarea
                  id="bed"
                  v-model="form.bed"
                  type="text"
                  placeholder="Insert the bed"
                  required
                  autocomplete="off"
                  maxlength="3">
               </b-form-textarea> 
            </b-form-group>
            <b-button-group>
                <b-button type="submit" class="mr-2" variant="outline-primary" @click="saveTravel">Save</b-button>
                <b-button v-if="this.$route.params.rowData" type="submit" class="mr-2" variant="outline-danger" @click="deleteTravel">Delete</b-button>
                <b-button type="submit" class="mr-2" variant="outline-secondary" @click="backToList">Return</b-button>
            </b-button-group>
        </b-form>
    </div>
</template>

<script>
import axios from 'axios';
import ToastMixin from '../mixins/toastMixin.js'

export default {
    mixins: [ToastMixin],
    name: "FormView",

    data() {
        return {
            form: {
                name: "",
                price_confort: "",
                price_econ: "",
                city: "",
                duration: "",
                seat: "",
                bed: "",
                timeout: null,
                waitTime: 1000
            }
        }
    },

    created() {
        // Get the row data from route params when acessed via list
        const rowData = this.$route.params.rowData;

        this.id_travel = rowData.id_travel;

        this.form.name = rowData.name;
        this.form.price_confort = rowData.price_confort;
        this.form.price_econ = rowData.price_econ;
        this.form.city = rowData.city;
        this.form.duration = rowData.duration;
        this.form.seat = rowData.seat;
        this.form.bed = rowData.bed;
    },

    methods: {
        saveTravel() {
        // Check if rowData is provided via route params from list
        if (this.$route.params.rowData) {
            // If rowData exists, it means we are updating an existing entry
            const url = `http://127.0.0.1:8000/travels/${this.id_travel}/`;
            axios.put(url, this.form, { timeout: 10000 })
                .then((response) => {
                console.log('Travel updated successfully:', response);
                this.showToast("success", "Success!", "Travel updated sucessfully!");
            })
            .catch((error) => {
                console.error('Error updating travel:', error);
            });
        } else {
            // If rowData doesn't exist, it means we are creating a new entry
            axios.post('http://127.0.0.1:8000/travels/', this.form, { timeout: 10000 })
                .then((response) => {
                    console.log('Travel saved successfully:', response);
                    this.resetForm();
                    this.showToast("success", "Success!", "Travel registered sucessfully!");
                })
            .catch((error) => {
                console.error('Error saving travel:', error);
            });
        }
        },
        deleteTravel(){
            const url = `http://127.0.0.1:8000/travels/${this.id_travel}/`;
            axios.delete(url, this.form, {timeout: 10000})
                .then((response) => {
                    console.log('Travel deleted sucessfully:', response);
                    this.resetForm();
                })
            .catch((error) => {
                console.error('Error deleting travel:', error);
            })
        },
        resetForm() {
            this.form = {
                name: "",
                price_confort: "",
                price_econ: "",
                city: "",
                duration: "",
                seat: "",
                bed: ""
            };
        },
        backToList(){
            this.$router.push({ name: 'list'})
        }
    }
}
</script>
