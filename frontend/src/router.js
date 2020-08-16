import Vue from 'vue'
import Router from 'vue-router'

import articleList from './page/articleList'
import articlePage from './page/article'
import articleForm from './page/articleForm'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
            path: '/article',
            name: 'articleList',
            component: articleList,
        },
        {
            path: '/article/:id',
            name: 'articlePage',
            component: articlePage,
            props: true
        },
        {
            path: '/article/new',
            name: 'articleForm',
            component: articleForm,
        }
    ]
})