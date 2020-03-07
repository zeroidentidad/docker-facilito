
const express = require('express')
const app = express()

app.get('/',(req, res)=>res.send('Holas mundos'))
app.listen(3000,()=>console.log("Watahea"))