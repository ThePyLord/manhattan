const axios = require('axios')
const express = require('express')
const mongoose = require('mongoose')
const app = express()

app.use(express.urlencoded({ extended: false}))
app.use(express.json())

mongoose.connect('mongodb://localhost:27017/manhattan', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
console.log('Successfully connected to the database. 😎')

app.get('/', (req, res) => {
    res.json({ message: 'Hello'})
})

app.get('/portfolios', (req, res) => {
    res.json({message: 'You are at the /portfolios route on the JS version'})
})

app.post('/portfolios/', (req, res) => {
    
})

module.exports = app