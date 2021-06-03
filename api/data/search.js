const axios = require('axios')
const cheerio = require('cheerio')

async function getPriceData() {
    try {
        const { data } = await axios.get('https://coinmarketcap.com/')
        
        const $ = await cheerio.load(data)
        console.log($('tr').text())
    } catch (error) {
        
    }
}

getPriceData()