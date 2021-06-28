const express = require('express');
const cryptos = require('../cryptos');
const router = express.Router();


router.get('/prices', (req, res) => {
    const error = new Error('No resource exists at this location')
    error.status = 400
    error.redirMsg = 'Please use /prices/:assetId instead ⏭'
    res.status(error.status).send(error.message + '. ' + error.redirMsg)
})

router.get('/prices/:assetId', (req, res) => {
    const assetId = req.params.assetId
    cryptos(assetId)?.then(data => {
        console.log(data)
        res.status(200).json({
            message: "Successfully retrieved the assetId info",
            data: data
        })
    }).catch(err => {
        res.status(404).json({
            message: 'Failed to retrieve the assetId info',
            Error: err.data
        })
    })
})


module.exports = router;