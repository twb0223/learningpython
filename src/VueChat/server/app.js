const index = require('./routes/index');
const path = require('path');
const bodyParser = require('body-parser');
const express = require('express');
const cors=require('cors');
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static(path.join(__dirname, 'dist')))
// 后端api路由
app.use('/', index);

//跨域设置
app.use(cors({
    origin:['http://localhost:8080'],
    methods:['GET','POST'],
    alloweHeaders:['Conten-Type', 'Authorization']
}));

// app.use(cors());

// app.all('*', function(req, res, next) {  
//     res.header("Access-Control-Allow-Origin", "*");  
//     res.header("Access-Control-Allow-Headers", "X-Requested-With");  
//     res.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");  
//     res.header("X-Powered-By",' 3.2.1')  
//     res.header("Content-Type", "application/json;charset=utf-8");  
//     next();  
// });


// 监听端口
app.listen(3000);
console.log('success listen at port:3000......');