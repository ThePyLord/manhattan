const axios = require('axios')
const express = require('express')
const mongoose = require('mongoose')
const morgan = require('morgan')
const app = express()

const apiRoutes = require('./routes/portfolio')

app.use(morgan('dev'))
app.use(express.urlencoded({ extended: true}))
app.use(express.json())

mongoose.connect('mongodb://localhost:27017/manhattan', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
console.log('Successfully connected to the database. 😎')

app.use('/api', apiRoutes)

app.use((req, res, next) => {
    const error = new Error({messsage: 'There\s nothing at this resource'})
    error.status = 404
    next()
})

app.use((error, req, res, next) => {
    res.status(error.status || 500).json({
        error: {
            messsage: error.messsage
        }
    })
})

module.exports = app