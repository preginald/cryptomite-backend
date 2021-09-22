import { reactive } from 'vue'

const state = reactive({
    price: 2.50,
    apr: 1050,
    cost: 0,
    profit: 0,
    yearly: 0,
    daily: 0,
    qty: 300,
})

const actions = {
    inc() {
        state.cost = state.price * state.qty
        state.yearly= state.cost * (state.apr/100) 
        state.daily = state.yearly / 365
    }
}

export default { state, ...actions }