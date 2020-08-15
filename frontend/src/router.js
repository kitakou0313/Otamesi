import Vue from 'vue'
import Router from 'vue-router'

import articlePage from './page/article'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
        path: '/article',
        name: 'articleList',
        component: articlePage
    }]
})