<template>
    <div class="tabpanle">
        <div class="search">
              <input type="text"  v-model="key" placeholder="查询你的朋友" >
           <img src="../assets/img/search.png" alt="login">
        </div>
        <div class="linkgroup" v-for="item in filterList" :key="item.Gname">
            <div class="groupName" @click.self='item.Open=!item.Open'><img src='../assets/img/friends.png'>{{item.Gname}}({{item.AccountList.length}})</div>
            <ul class='grouplist' v-for="item2 in item.AccountList" v-show="item.Open" :key="item2.AccountID">
                <li v-bind:data-account="item2.AccountID" @click='selectfriend'>
                    <img v-bind:src="item2.AccountLogo" v-bind:alt="item2.AccountID">
                    <span>{{item2.AccountName}}</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
var initdata = {
  AccountID: 10000,
  AccountName: "Sam",
  Logo: "../assets/img/face.jpg",
  Grouplist: [
    {
      Gname: "Work",
      Open: true,
      AccountList: [
        {
          AccountID: "1302102",
          AccountName: "AName4",
          AccountLogo: "https://cn.vuejs.org/images/logo.png"
        },
        {
          AccountID: "140022",
          AccountName: "AName5",
          AccountLogo: "https://cn.vuejs.org/images/logo.png"
        },
        {
          AccountID: "1240202",
          AccountName: "AName2",
          AccountLogo: "https://cn.vuejs.org/images/logo.png"
        }
      ]
    },
    {
      Gname: "Study",
      Open: true,
      AccountList: [
        {
          AccountID: "10006",
          AccountName: "CCCCC",
          AccountLogo: "https://cn.vuejs.org/images/logo.png"
        },
        {
          AccountID: "10007",
          AccountName: "77777",
          AccountLogo: "https://cn.vuejs.org/images/logo.png"
        },
        {
          AccountID: "10008",
          AccountName: "88888",
          AccountLogo: "https://cn.vuejs.org/images/logo.png"
        }
      ]
    }
  ]
};

export default {
  data() {
    return {
      sendmsg: "",
      UserInfo: "",
      key: "",
      selectedPerson: {
        AccountID: "",
        AccountLogo: "",
        AccountName: ""
      },
      msgcache: {
        sendId: "",
        recvId: "",
        msglist: [
          {
            msg: "",
            time: "",
            flag: "" //s=发送数据，r=接收数据
          }
        ]
      },
      storagekey: "",
      socket: ""
    };
  },
  computed: {
    filterList() {
      return this.searchlist();
    }
  },
  mounted() {
    this.getgrouplist();
  },
  methods: {
    searchlist() {
      let key = this.key;
      let orglist = this.UserInfo.Grouplist;
      if (key) {
        let gplist = [];
        for (let i = 0; i < orglist.length; i++) {
          let gp = {};
          gp.Open = true;
          gp.Gname = orglist[i].Gname;
          gp.AccountList = [];
          for (let j = 0; j < orglist[i].AccountList.length; j++) {
            if (
              orglist[i].AccountList[j].AccountName
                .toLowerCase()
                .indexOf(key.toLowerCase()) !== -1
            ) {
              gp.AccountList.push(orglist[i].AccountList[j]);
            }
          }
          if (gp.AccountList.length > 0) {
            gplist.push(gp);
          }
        }
        return gplist;
      }
      return this.UserInfo.Grouplist;
    },
    getgrouplist() {
      let _this = this;
      _this.UserInfo = initdata;
    },
    selectfriend(e) {
      let curaccountid = e.currentTarget.dataset.account;
      if (curaccountid != this.selectedPerson.AccountID) {
        this.selectedPerson.AccountID = curaccountid;
        this.storagekey =
          this.UserInfo.AccountID + "_" + this.selectedPerson.AccountID;
        let curacc_lastMsginfo = localStorage.getItem(this.storagekey);
        this.msgcache.sendId = this.UserInfo.AccountID;
        this.msgcache.recvId = curaccountid;
        this.msgcache.msglist =
          JSON.parse(curacc_lastMsginfo) === null
            ? []
            : JSON.parse(curacc_lastMsginfo);
        this.selectedPerson.AccountLogo = e.currentTarget.querySelector(
          "img"
        ).src;
        let lis = document.querySelectorAll(".linkgroup li");
        for (var index = 0; index < lis.length; index++) {
          lis[index].classList.remove("libgcolor");
        }
        e.currentTarget.classList.add("libgcolor");
        //this.rendermsg();
        eventBus.$emit("selectid", curaccountid);
      }
    }
  }
};
</script>

<style>
/*联系人列表*/

.tabpanle {
  width: 200px;
  height: 740px;
  overflow-x: hidden;
  overflow-y: auto;
  float: left;
  background-color: #f5f5f5;
  border-right: 1px solid #f5f5f5;
  border-bottom: 1px solid #f5f5f5;
  /* box-shadow: 0 0 10px rgba(0, 204, 204, 0.5); */
}
.linkgroup {
  padding-top: 20px;
  text-indent: 20px;
}
.search {
  margin-top: 10px;
  margin-left: 10px;
  /*position: relative;*/
  width: 100%;
}

.search img {
  line-height: 20px;
  vertical-align: middle;
  height: 20px;
}

.search input {
  vertical-align: middle;
  width: 80%;
  height: 20px;
  line-height: 20px;
  border: none;
  outline: none;
  background-color: #f5f5f5;
  border-bottom: 1px solid #ddd;
}

.groupName {
  vertical-align: middle;
  font-size: 14px;
  cursor: pointer;
  line-height: 20px;
}
.groupName img {
  vertical-align: bottom;
  margin-right: 8px;
  width: 20px;
  height: 20px;
}
.grouplist {
  padding-top: 5px;
  font-size: 12px;
  text-indent: 30px;
}

.grouplist li {
  line-height: 50px;
  height: 50px;
  cursor: pointer;
}

.grouplist li:hover {
  box-shadow: 0 0 10px rgba(0, 204, 204, 0.5);
}

.libgcolor {
  background-color: #cee2ee;
}

.grouplist img {
  vertical-align: middle;
  width: 40px;
  height: 40px;
  border-radius: 30px;
  box-shadow: 0 0 10px #cee2ee;
}

/*滚动条样式*/

.tabpanle::-webkit-scrollbar {
  /*滚动条整体样式*/
  width: 4px;
  /*高宽分别对应横竖滚动条的尺寸*/
  height: 4px;
}

.tabpanle::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  border-radius: 5px;
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
  background: rgba(0, 0, 0, 0.2);
}

.tabpanle::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
  border-radius: 0;
  background: rgba(0, 0, 0, 0.1);
}
</style>
