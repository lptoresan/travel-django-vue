<template>
    <div class="container">
        <img alt="Agency logo" id="list-logo" src="../assets/images/list-logo.svg">
        <b-alert v-model="showDismissibleAlert" variant="danger" dismissible>
            Registry not found!
        </b-alert>
        <section id="panel-search">
            <div>
                Search for any travel
            </div>
            <div class="mb-3"> 
                <input type="text" placeholder="City" class="mr-3" v-model="list.name">
                <input type="number" placeholder="Price econ" class="mr-3" v-model="list.price_econ">
                <input type="number" placeholder="Price confort" class="mr-3" v-model="list.price_confort">
            </div>
            <div class="mb-3">
                <b-button-group>
                    <b-button type="submit" class="panel-btns mr-2" variant="outline-secondary" @click="searchTravel">Search</b-button>
                    <b-button class="panel-btns mr-2" variant="outline-secondary" @click="refreshList">Refresh</b-button>
                </b-button-group>    
            </div>
        </section>
        <b-table striped hover :items="list" class="list-style" @row-clicked="handleRowClick"></b-table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "TravelList", 
    data() {
        return {
            list: [],
            showDismissibleAlert: false
        };
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/travel-urls/')
            .then((resp) => {
                this.list = resp.data;
                console.warn(resp);
            })
            .catch((error) => {
                console.error('Error fetching data:', error);
            });
    },

    methods: {
        searchTravel(){
            const params = {
                city: this.list.name,
                price_econ: this.list.price_econ,
                price_confort: this.list.price_confort
            };

            axios.get('http://127.0.0.1:8000/travel-urls/search/', { params})
                .then((resp) => {
                        this.list = resp.data;
                        console.warn(resp);
                })
                .catch((error) => {
                    this.showDismissibleAlert = true;
                    console.error('Error searching data:', error);
                })  
        },

        refreshList(){
            axios.get('http://127.0.0.1:8000/travel-urls/')
            .then((resp) => {
                this.list = resp.data;
                console.warn(resp);
            })
            .catch((error) => {
                if (error.response && error.response.status === 404) {
                    this.errorMessage = 'No entries found.';
                } else {
                    console.error('Error searching data:', error);
                }
            });
        },

        handleRowClick(item) {
            this.$router.push({ name: 'form', params: { rowData: item } });
        }
    }
};
</script>

<style>
#list-logo{
  display: block;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: auto;
  margin-right: auto;
  width: 400px;
}

#panel-search{
    background-image: linear-gradient(45deg, #170830, rgb(96, 79, 189));
    color: white;
    padding: 10px;
    padding-bottom: 2px;
    border-radius: 10px;
    margin-bottom: 10px;
}

.panel-btns {
    text-align: center;
    color:  rgb(43, 103, 131);
    background-color: white;
}

html {
    background-image: linear-gradient(45deg, white, #ececec);
    width: 100%;
    margin-right: 0;
    margin-left: 0;
}
</style>