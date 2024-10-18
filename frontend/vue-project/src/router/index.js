import { createRouter,createWebHistory } from "vue-router"; //两个方法分别用于创建路由实例和创建WebHistory实例

import register from "../components/register.vue"; //导入注册组件

const routes = [
    {
        path: '/',
        component:login
    },
    {
        path: '/register',
        name:'register',
        component: register   //注册页面的路由,component属性指定了渲染的组件
    },
    {
        path: '/login',
        component:login
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL), //作用是创建WebHistory实例，用于管理路由历史记录，process.env.BASE_URL是当前项目的根路径
    routes
})

export default router