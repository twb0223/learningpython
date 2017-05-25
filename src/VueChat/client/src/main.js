import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import {
  
  Input,
  InputNumber,
  Form,
  FormItem,
  Button
  
} from 'element-ui'


import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false
Vue.prototype.$axios = axios;

Vue.use(Button)
Vue.use(Input)
Vue.use(InputNumber)
Vue.use(Form)
Vue.use(FormItem)


window.eventBus = new Vue();
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {
    App
  }
})
