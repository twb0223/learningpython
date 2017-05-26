<template>
  <div class="Msginput">
      <div class="inputbar">
        <img src="../assets/img/Smile.png">
        <img src="../assets/img/set.png">
           <img src="../assets/img/skip.png">
        </div>
      <div class="inputdiv">
        <textarea class="inputfiled" placeholder="在此处输入消息(Ctrl+Enter发送)" @keydown='sendMsg'></textarea>
     </div>
  </div>
</template>

<script>
Date.prototype.Format = function(fmt) {
  var o = {
    "M+": this.getMonth() + 1, //月份
    "d+": this.getDate(), //日
    "h+": this.getHours(), //小时
    "m+": this.getMinutes(), //分
    "s+": this.getSeconds(), //秒
    "q+": Math.floor((this.getMonth() + 3) / 3), //季度
    S: this.getMilliseconds() //毫秒
  };
  if (/(y+)/.test(fmt))
    fmt = fmt.replace(
      RegExp.$1,
      (this.getFullYear() + "").substr(4 - RegExp.$1.length)
    );
  for (var k in o)
    if (new RegExp("(" + k + ")").test(fmt))
      fmt = fmt.replace(
        RegExp.$1,
        RegExp.$1.length == 1 ? o[k] : ("00" + o[k]).substr(("" + o[k]).length)
      );
  return fmt;
};

export default {
  data() {
    return {
      inputMsg: ""
    };
  },
  methods: {
    renderMsg() {},
    htmlEncode(str) {
      var div = document.createElement("div");
      div.appendChild(document.createTextNode(str));
      var result = div.innerHTML;
      //createElement 的节点必须添加到body 否则会引起内存泄漏
      document.body.appendChild(div); //将div追加到页面上
      document.body.removeChild(div); //将div从页面上删除
      return result;
    },
    sendMsg(oEvent) {
      if (oEvent.keyCode === 13 && oEvent.ctrlKey) {
        let _this = this,
          _msg = _this.htmlEncode(oEvent.currentTarget.value),
          _time = new Date().Format("yyyy-MM-dd hh:mm:ss");
        let sendobj = {
          sendid: "AAA",
          avater: require("../assets/img/face.jpg"),
          Msg: _msg,
          time: _time
        };
        if (sendobj.Msg) {
          eventBus.$emit("sendmsg", sendobj); //注册全局监听，将值传递到Message
          oEvent.currentTarget.value = "";
        }
      }
    }
  }
};
</script>

<style>
.Msginput {
  width: auto;
}
.inputbar {
  text-indent: 10px;
  height: 23px;
  line-height: 23px;
  background-color: #f5f5f5;
  border-top: 1px solid #f5f5f5;
  border-bottom: 1px solid #f5f5f5;
  vertical-align: middle;
}
.inputbar img {
  margin-top: 3px;
  width: 18px;
  height: 18px;
  margin-right: 10px;
}

.inputfiled {
  clear: both;
  text-indent: 10px;
  outline: none;
  resize: none;
  height: 150px;
  width: 99.6%;
  border: 0px solid #f5f5f5;
  overflow-y: scroll;
  overflow-y: auto;
  word-break: break-word;
  word-wrap: break-word;
  outline-style: none;
  border-bottom: 1px solid #f5f5f5;
}

.inputfiled::-webkit-scrollbar {
  /*滚动条整体样式*/
  width: 5px;
  /*高宽分别对应横竖滚动条的尺寸*/
  height: 5px;
}

.inputfiled::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  border-radius: 5px;
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
  background: rgba(0, 0, 0, 0.2);
}

.inputfiled::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
  border-radius: 0;
  background: rgba(0, 0, 0, 0.1);
}
</style>
