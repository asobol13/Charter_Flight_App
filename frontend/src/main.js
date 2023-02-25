// import { createApp } from 'vue'
// import App from './App.vue'

// createApp(App).mount('#app')
import Vue from 'vue';
import App from './App.vue';
import VueComp from '@vue/composition-api';

Vue.useAttrs(VueComp);

new Vue({

    render: h => h(App),
}).$mount('#app');