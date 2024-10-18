
import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'

const app = createApp(App)
axios.defaults.baseURL = 'http://localhost:8000/'
app.config.globalProperties.$http = axios // injecting axios to all components
app.use(router)
createApp(App).mount('#app')
