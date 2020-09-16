import axios from 'axios'

const backendAPI = axios.create({
    baseURL: 'http://localhost/api',
    headers: {
        Accept: 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
    }
})

export default backendAPI