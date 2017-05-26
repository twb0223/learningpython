<template>
    <div class='Message' id="MsgContain">
          <br/>
          <br/>
        <div class="msgtip" v-for="item in sendMsgs" :key="item.time">
          <img :src="item.avater">
            <p class="msgname">{{item.sendid}} {{item.time}}</p>
            <div class="msginfo">
              <pre><code>{{item.Msg}}</code></pre>
            </div>
            <br/>
            <br/>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      selectid: "",
      sendMsgs: []
    };
  },
  methods: {
    htmlDecode(str) {
      var div = document.createElement("div");
      div.innerHTML = str;
      var result = div.innerText;
      //createElement 的节点必须添加到body 否则会引起内存泄漏
      document.body.appendChild(div); //将div追加到页面上
      document.body.removeChild(div); //将div从页面上删除
      return result;
    }
  },
  updated() {
    MsgContain.scrollTop = MsgContain.scrollHeight;
    
  },
  mounted() {
    var _this = this;
    eventBus.$on("selectid", function(val) {
      _this.selectid = val;
    });
    eventBus.$on("sendmsg", function(val) {
      val.Msg = _this.htmlDecode(val.Msg); //特殊标签重新转义回来
      _this.sendMsgs.push(val);
    });
  }
};
</script>

<style>
.Message {
  width: 99.9%;
  height: 552px;
  overflow-y: scroll;
  overflow-y: auto;
}
.Message::-webkit-scrollbar {
  /*滚动条整体样式*/
  width: 5px;
  /*高宽分别对应横竖滚动条的尺寸*/
  height: 5px;
}

.Message::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  border-radius: 5px;
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
  background: rgba(0, 0, 0, 0.2);
}

.Message::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
  border-radius: 0;
  background: rgba(0, 0, 0, 0.1);
}
.msgtip {
  display: inline;
  margin-left: 10px;
}
.msgtip img {
  width: 40px;
  height: 40px;
  border-radius: 30px;
  box-shadow: 0 0 10px #cee2ee;
}
.msgname {
  margin-top: -45px;
  margin-left: 55px;
  font-size: 13px;
  font-weight: bold;
  color: #3b73c0;
}
.msginfo {
  margin-top: 5px;
  height: auto;
  margin-left: 55px;
  line-height: 30px;
  font-size: 14px;
  width: 80%;
  background-color: #f5f5f5;
  border-radius: 5px;
  word-break: break-word;
  word-wrap: break-word;
  box-shadow: 0 0 10px rgba(0, 204, 204, 1);
}
.msginfo pre {
  margin-left: 5px;
}
</style>