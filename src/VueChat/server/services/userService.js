var mysql = require('mysql');
var $conf = require('../conf/dbconf');
var $tool = require('../utils/tools');
var $sql = require('./sqlmap');

var pool = mysql.createPool($conf.aliyunmysql);

module.exports = {
    getToken: function (req, res, next) {
        var param = req.query || req.params;
        var token = $tool.guidGenerator() + $tool.guidGenerator();
        var time = 3000;

        $tool.jsonwrite(res, { 'token': token, 'time': time });
    },
    add(req, res, next) {
        pool.getConnection((err, connetion) => {
            var param = req.query || req.params;
            connetion.query($sql.insert, [param.user_name, param.password, param.email], () => {
                if (result) {
                    result = { code: 200, msg: '添加成功' }
                }
                $tool.jsonwrite(res, result);
                connetion.release();
            })
        })
    },
    update: function (req, res, next) {
        var param = req.body;
        if (param.user_name == null || param.email == null || param.id == null) {
            $tool.jsonwrite(res, undefined);
            return;
        }
        pool.getConnection(function (err, connection) {
            connection.query($sql.update, [param.name, param.age, +param.id], function (err, result) {
                // 使用页面进行跳转提示
                if (result.affectedRows > 0) {
                    res.render('suc', {
                        result: result
                    }); // 第二个参数可以直接在jade中使用
                } else {
                    res.render('fail', {
                        result: result
                    });
                }
                connection.release();
            });
        });
    },
    delete: function (req, res, next) {
        pool.getConnection(function (err, connection) {
            connection.query($sql.delete, id, function (err, result) {
                if (result.affectedRows > 0) {
                    result = {
                        code: 200,
                        msg: '删除成功'
                    };
                } else {
                    result = void 0;
                }
                $tool.jsonwrite(res, result);
               
            });
        });
    },
    deleteGirlById(req, res, next) {
        var id = +req.params.id;
        pool.getConnection((err, connection) => {
            connection.query($sql.deleteGirlById, id, (err, result) => {
                if (result.affectedRows > 0) {
                    result = {
                        code: 200,
                        msg: '删除成功'
                    };
                } else {
                    result = void 0;
                }
                $tool.jsonwrite(res, result);
            })
        })
    },
    queryById: function (req, res, next) {
        var id = +req.query.id; // 为了拼凑正确的sql语句，这里要转下整数
        pool.getConnection(function (err, connection) {
            connection.query($sql.queryById, id, function (err, result) {
                $tool.jsonwrite(res, result);
                connection.release();
            });
        });
    },
    queryAll: function (req, res, next) {
        pool.getConnection(function (err, connection) {
            connection.query($sql.queryAll, function (err, result) {
                $tool.jsonwrite(res, result);
                connection.release();
            });
        });
    },
    queryAllGril(req, res, next) {
        pool.getConnection(function (err, connection) {
            connection.query($sql.queryAllGrils, function (err, result) {
                $tool.jsonwrite(res, result);
                connection.release();
            });
        });
    },
    queryAllFund(req, res, next) {
        pool.getConnection(function (err, connection) {
            connection.query($sql.queryAllFund, function (err, result) {
                $tool.jsonwrite(res, result);
                connection.release();
            });
        });
    }
}
