const mongoose = require('mongoose')
const { Schema } = require('mongoose')

const dbSchema = new Schema({
    portfolio: {
        tick_name: { required: true, type: String},
        entry: {required: true, type: Number},
        target: {required: true, type: Number}
        // required: true,
        // type: Schema.Types.Mixed
    },
    notifs: [{type: Number, max: 10}],
    
})

const dbModel = mongoose.model('Portfolio', dbSchema)

module.exports = dbModel