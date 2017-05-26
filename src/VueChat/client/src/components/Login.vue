<template>
  <div class="login_main">
    <div class="login_form">
      <div class="loginlogo">
        <img :src="loginLogo" alt="">
      </div>
      <el-form ref="form" :model="form">
        <el-form-item >
          <el-input v-model="userName" placeholder="输入账号"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input v-model="pwd" placeholder="输入密码"></el-input>
        </el-form-item>
     <el-form-item>
         <el-button @click='login' type="primary">Sign In</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      userName: "",
      pwd: "",
      loginLogo: "",
      form: {}
    };
  },
  mounted: function() {
    this.loginLogo = require("../assets/img/face.jpg");
  },
  methods: {
    login() {
      const _this = this;
      this.$axios.get(process.env.API_HOST + "/user").then(function(response) {
        _this.$router.push({
          name: "Main"
        });
      });
    }
  }
};
</script>
<style scoped>
.login_main {
  position: fixed;
  top: 50%;
  bottom: 50%;
  left: 50%;
  right: 50%;
  width: 0;
  height: 0;
}

.login_form {
  width: 450px;
  height: 300px;
  /*margin: 50px auto;*/
  margin-left: -225px;
  margin-top: -150px;
  box-shadow: 0px 0px 10px rgba(0, 204, 204, 0.5);
  border-radius: 10px;
}
.el-form {
  margin-top: 20px;
  text-align: center;
}
.el-input {
  width: 300px;
}
.el-button {
  width: 300px;
}
.loginlogo {
  padding-top: 30px;
  margin-left: 200px;
  width: 50px;
}

.loginlogo img {
  width: 50px;
  height: 50px;
  border-radius: 50px;
}
</style>
