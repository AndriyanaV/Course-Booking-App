import './assets/main.css'
import {createApp} from "vue";
import App from './App.vue'
import Vue3Toastify from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import axios from 'axios'





axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("access_token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);


const isTokenExpired = () => {
  const expirationTime = localStorage.getItem("token_expiration");
  return !expirationTime || Date.now() > parseInt(expirationTime, 10); // Poređenje sa trenutnim vremenom
};


const exemptRoutes = ["/api/login", "api/current-courses/get-courses"];


axios.interceptors.request.use(
  (config) => {
    // Proveri da li je ruta izuzeta
    const isExemptRoute = exemptRoutes.some((route) =>
      config.url.includes(route)
    );

    if (!isExemptRoute && isTokenExpired()) {
      // Obriši token i preusmeri na login
      localStorage.clear();
      router.push("/login"); // Preusmeravanje na login
      throw new axios.Cancel("Token is expired. Redirecting to login.");
    }

    return config;
  },
  (error) => Promise.reject(error)
);





const app = createApp(App)


app.use(Vue3Toastify, {
  autoClose: 3000,
})

app.use(router)

app.mount('#app')
