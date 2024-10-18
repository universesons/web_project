<template>
    <h1>注册页面</h1><br><br>
    用户名：<input type="text" v-model="username"> <br>
    密码：<input type="password" v-model="password"> <br>
    <button @click="submit">注册</button> <br>
    <router-link to="/login">登录</router-link>
    </template>
    
    <script>
    export default{
        data() {
            return {
                username: "",
                password: ""
            }
        },
        methods: {
            submit() {
                this.$http.post('/api/register/', {"username": this.username, "password": this.password})
                .then((response) => {
                    alert(response.data.msg)
                })
            }
        }
    }
    </script>
