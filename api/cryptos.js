const path = require('path')
const axios = require('axios')
const pyCon = require('node-python-communication').Process;
let proc = new pyCon();

let paths = `${path.join(__dirname, '../module')}`

proc.configure(`${paths}\\search.py`, [])

proc.start();

async function cryptos() {
    proc.listen.on('data', data => {
        let cryptoObj = data.toString();
        // console.log(cryptoObj);
        return cryptoObj
    })

    proc.listen.on('error', err => {
        console.log(err)
    })
}


async function getPriceData(assetName) {
    return new Promise((resolve, reject) => {
        axios.get(`https://api.coincap.io/v2/assets`, {
            headers: {
                'Accept-Encoding': 'gzip'
            }
        }).then(res => {
            let { data } = res.data
            const symbol = data.some(ticker => {
                const formatted = {
                    name: ticker['id'],
                    rank: ticker['rank'],
                    ticker: ticker['symbol'],
                    supply: trimNums(ticker['supply']),
                    maxSupply: (ticker['maxSupply']*1).toLocaleString('en-US'),
                    marketCap: trimNums(ticker['marketCapUsd']),
                    volume24h: trimNums(ticker['volumeUsd24Hr']),
                    price: trimNums(ticker['priceUsd']),
                    priceChange24h: trimNums(ticker['changePercent24Hr'])
                }
                if(ticker.symbol === assetName || ticker.id === assetName) {
                    const tickerRes = Object.filter(formatted, res => res !== '0')
                    resolve(tickerRes)
                }
            })
        }).catch(err => {
            reject(err)
            // const error = JSON.parse(err)
            if (err.response.status === 404) {
            //     // console.log(error['request']['data']['error'])
                console.log(err.toJSON().message)
            }
        })
    })
}

function trimNums(num) {
    let trimmedNum = (((num *1).toFixed(2)) *1)
    .toLocaleString('en-US', {currency: 'USD', style: 'currency'})
    
    return trimmedNum
}


// Helper to filter the object returned from the api
Object.prototype.filter = (mainObject, filterFunction) => 
        Object.keys(mainObject)
        .filter((ObjectKey) => filterFunction(mainObject[ObjectKey]))
        .reduce((result, ObjectKey) => {
            result[ObjectKey] = mainObject[ObjectKey];
            return result;
        }, {})


// getPriceData('ethereum')?.then(data => {
//     let desiredRes = Object.filter(data, res => res !== '0')
//     console.log( desiredRes )
//     console.log("Printing data\n =============================")
//     console.table(desiredRes)
//     console.log("\n ====================================")
// })

module.exports = getPriceData