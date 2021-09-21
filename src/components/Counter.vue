<template>  
    <label for="price">Price</label><br>
    <input type="number" name="price" id="price" v-model="state.price"><br>
    <label for="qty">Qty</label><br>
    <input type="number" name="qty" id="qty" v-model="state.qty"><br>
    <label for="cost">Cost</label><br>
    <input type="number" name="cost" id="cost" v-model="state.cost"><br>
    <label for="apr">APR</label><br>
    <input type="number" name="apr" id="apr" v-model="state.apr"><br>
    <label for="yearly">Yearly income</label><br>
    <input type="number" name="yearly" id="yearly" v-model="state.yearly"><br>
    <label for="daily">Daily income</label><br>
    <input type="number" name="daily" id="daily" v-model="state.daily"><br>
    <button @click="inc()">Inc</button>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import counterStore from '../stores/counter'

export default defineComponent({
    setup(){
        const { state, getters, inc } = counterStore
        return { state, inc }
    }
})
</script>