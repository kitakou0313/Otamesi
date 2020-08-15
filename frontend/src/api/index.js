import axios from 'axios'

const backendAPI = axios.create({
    baseURL: 'http://localhost:5000',
    headers: {
        Accept: 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
    }
})

export default backendAPI