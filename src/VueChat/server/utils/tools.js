module.exports = {
    guidGenerator: function () {
        var S4 = function () {
            return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
        };
        return (S4() + S4() + S4() + S4() + S4() + S4() + S4() + S4());
    },

    jsonwrite: function (res, ret) {
        if (typeof ret === 'undefined') {
            res.json({
                code: '1',
                msg: '操作失败'
            });

        } else {
            res.json({
                ret
            });
        }
    }
}