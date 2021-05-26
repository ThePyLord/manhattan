const express = require('express');
const router = express.Router();


router.get('/portfolios', (req, res) => {
    res.json({message: 'You are at the /portfolios route on the JS version'})
})

router.post('/portfolios/', (req, res) => {
    res.status(201).json({
        message: 'Your submission was received👍'
    })
})

module.exports = router;