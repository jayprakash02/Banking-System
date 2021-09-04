<template>
  <div class="home">
    <customer />
    <transcation />
  
  </div>
</template>

<script>
// @ is an alias to /src
import Customer from "@/components/Customer.vue";
import Transcation from "@/components/Transcation.vue";
export default {
  name: "Home",
  components: {
    Customer,Transcation
  },
};
</script>
