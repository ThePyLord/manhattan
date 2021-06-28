const express = require('express');
const { mongoose } = require('mongoose');
const router = express.Router();

const Portfolio = require('../models/portfolioModel')
let postCount = 0

router.get('/portfolios', (req, res) => {
	Portfolio.find()
	.exec()
	.then(docs => {
		res.status(200).json(docs)
	})
	.catch(err => {
		console.log(err)
		res.status(500).json({
			error: err
		})
	})
	// console.log(req.body.portfolio)
	res.json({message: 'You are at the /portfolios route on the JS version'})
})

router.get('/portfolios/:id', (req, res) => {
	const id = req.params.id
	Portfolio.findById(id)
	.exec()
	.then(doc => {
		console.log("From database:", doc)
		if (doc) {
			res.status(200).json(doc)
		} else {
			res.status(404).json({
				message: "No valid entry for provided ID"
			})
		}
	})
	.catch(err => {
		console.log(err)
		res.status(500).json({
			error: err
		})
	})
	res.json({message: 'You are at the /portfolios route on the JS version'})
})

router.post('/portfolios', (req, res) => {
	const postedTime = new Date(Date.now())
	const pft = new Portfolio({
		// _id: new mongoose.Types.ObjectId(),
		portfolio: req.body.portfolio,
		notifs: req.body.notifs
	})

	pft.save()
	.then(result => {
		res.status(201).json({
			message: `Your submission was received on ${postedTime.toDateString()} 👍`
		})
	}).catch(err => {
		console.log(err)
		res.status(500).json({error: err})
	})
})

router.delete('/portfolios/:id', (req, res) => {
	const id = req.params.id

	Portfolio.remove({_id: id}).exec()
	.then(res => {
		res.status(200).json({
			message: `${id} was deleted`
		})
	})
})

module.exports = router;