<template>
     <div class="header">
        <div class="logo">
            <img src="../assets/img/face.jpg" alt="">
        </div>
<<<<<<< HEAD
        <div id="menu">
            
        </div>
        <router-view/>
=======
>>>>>>> ff7a14f2154a7dfc23e207e860672a94371d9191
    </div>
</template>

<script>
export default {
  data() {
    return {};
  }
};
</script>

<style scoped>
.header {
  width: 100%;
  clear: both;
  min-height: 50px;
  background: #f9fafc;
  top: 0;
  position: fixed;
  text-align: center;
  box-shadow: 0 0 10px rgba(0, 204, 204, 0.5);
}
.logo {
  margin-top: 5px;
  margin-left: 10px;
  float: left;
  text-align: left;
  vertical-align: middle;
}
.logo img {
  width: 40px;
  height: 40px;
  border-radius: 100px;
}
#menu {
  height: 50px;
  width: 300px;
  float: right;
}
#menu ul {
  vertical-align: middle;
  margin-top: 15px;
  margin-right: 50px;
}
#menu li {
  list-style: none;
  padding: 0;
  margin: 0;
  float: right;
}

#menu li a {
  color: black;
  display: block;
  margin-left: 10px;
  text-decoration-line: none;
  font-size: 20px;
}

#menu li a:hover {
  color: #8492a6;
  text-decoration: none;
}
</style>
