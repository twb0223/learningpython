<template>
  <div class="center">
      <vMessage/>
      <vInput/>
       <router-view/>
  </div>
  
</template>

<script>
import vMessage from "./Message";
import vInput from "./Input";
export default {
  data() {
    return {};
  }, 
  components: {
    vMessage,
    vInput
  }
};
</script>

<style>
.center {
  overflow-x: hidden;
  overflow-y: auto;
  height: 740px;
}
</style>