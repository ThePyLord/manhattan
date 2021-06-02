const express = require('express');
const { Mongoose } = require('mongoose');
const router = express.Router();

const Portfolio = require('../models/portfolioModel')


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
	console.log("POST")
	// console.log(req.body)
	const pft = new Portfolio({
		_id: new mongoose.Types.ObjectId(),
		portfolio: req.body.portfolio,
		notifs: req.body.notifs
	})
	
	pft.save()
	.then(result => {
		console.log(result);
		res.status(201).json({
			message: 'Your submission was received👍',
			// result: Number(req.body.myRes)
		})
	}).catch(err => {
		console.log(err)
		res.status(500).json({error: err})
	})
	// res.status(201).json({"message": "You POSTed"})
})

// router.delete('/portfolios')

module.exports = router;