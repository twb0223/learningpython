<template>
<div class="main">
    <vHead/>   
    <div class="content">
        <vLeft/>
        <vCenter/>
    </div>
</div>
</template>

<script>
import vHead from "./Head";
import vLeft from "./Left";
import vCenter from "./Center";
import vFoot from "./Foot";
export default {
  data() {
    return {};
  },
  components: {
    vHead,
    vLeft,
    vCenter
  }
};
</script>

<style scoped>
.main {
  overflow: hidden;
}
.content {
  padding-top: 50px;
  height: 730px;
  overflow: hidden;
}
</style>
