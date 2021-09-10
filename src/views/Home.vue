<template>
  <div class="home">
  <section class="mt-md-4 pt-md-2 mb-5 pb-4">
    <!-- Card -->

    <!-- Section: Chart -->
    <section>
      <!-- Grid row -->
      <div class="row">
        <!-- Grid column -->
        <personal />

        <customer />
      </div>
      <!-- Grid row -->
    </section>

    <!-- Card -->
  </section>
    <transcation />
  
  </div>
</template>

<script>
// @ is an alias to /src
import Customer from "@/components/Customer.vue";
import Transcation from "@/components/Transcation.vue";
import Personal from "@/components/Personal.vue";
export default {
  name: "Home",
  components: {
    Customer,Transcation,Personal
  },
};
</script>
