import { createRouter,createWebHistory } from "vue-router"; //两个方法分别用于创建路由实例和创建WebHistory实例

import register from "../components/register.vue"; //导入注册组件

const routes = [
    {
        path: '/',
        component:login
    },
    {
        path: '/register',
        component:register
    },
    {
        path: '/login',
        component:login
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router