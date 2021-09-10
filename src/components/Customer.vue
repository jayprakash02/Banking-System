<template>
  <!-- Grid column -->

  <div class="col-xl-7 col-md-12 mr-0 pb-2">
    <!-- Card image -->
    <div class="card card-cascade narrower dark-card-admin text-white">
      <div
        class="view view-cascade gradient-card-header light-blue lighten-1 white black lighten-4"
      >
        <h2 class="h2-responsive mb-0 font-weight-500">
          Customer Available
        </h2>
      </div>

      <!-- Card content -->
      <div class="card-body card-body-cascade pb-0">
        <!-- Panel data -->
        <div class="row py-3 pl-4">
          <!-- First column -->
          <div class="col-md-6">
            <!-- Date select -->
            <button
              type="button"
              class="btn btn-primary"
              data-toggle="modal"
              data-target="#fluidModalRightSuccessDemo"
            >
              Search Customers
            </button>
            <div class="card-body card-body-cascade">
              <p v-if="user" class="card-text text-white">
                Selected Customer: {{ user.name }}
              </p>
            </div>

            <div
              class="modal fade right"
              id="fluidModalRightSuccessDemo"
              tabindex="-1"
              role="dialog"
              aria-labelledby="myModalLabel"
              aria-hidden="true"
              data-backdrop="false"
            >
              <div
                class="modal-dialog modal-full-height modal-right modal-notify modal-info"
                role="document"
              >
                <!-- Content -->
                <div class="modal-content">
                  <!-- Header -->
                  <div class="modal-header">
                    <p class="heading lead">Avilable Customers</p>

                    <button
                      type="button"
                      class="close"
                      data-dismiss="modal"
                      aria-label="Close"
                    >
                      <span aria-hidden="true" class="white-text">&times;</span>
                    </button>
                  </div>

                  <!-- Body -->

                  <div class="modal-body">
                    <fieldset
                      v-for="list in lists"
                      :key="list.cutomer_id"
                      class="form-check mb-4"
                    >
                      <input
                        class="form-check-input"
                        name="group1"
                        type="radio"
                        :id="list.cutomer_id"
                        :value="list"
                        v-model="user"
                      />
                      <label class="form-check-label" :for="list.cutomer_id">{{
                        list.name
                      }}</label>
                    </fieldset>
                  </div>

                  <!-- Footer -->
                  <div class="modal-footer justify-content-center">
                    <a type="button" class="btn btn-info" data-dismiss="modal"
                      >Select <i class="far fa-gem ml-1"></i
                    ></a>

                    <a
                      type="button"
                      class="btn btn-outline-danger waves-effect"
                      data-dismiss="modal"
                      v-on:click="user = ''"
                      >Cancel</a
                    >
                  </div>
                </div>
                <!-- Content -->
              </div>
            </div>
          </div>
          <!-- First column -->

          <!-- Second column -->
          <div class="col-md-6 text-center pl-xl-2 my-md-0 my-3">
            <!-- Summary -->
            <form action="" method="post"></form>
            <div class="md-form md-outline">
              <input
                type="text"
                id="amount"
                v-model="amount"
                class="form-control"
              />
              <label for="username12">Amount</label>

              <div class="md-form md-outline">
                <div class="card-foter text-right">
                  <button
                    type="button"
                    class="btn btn-outline-warning btn-sm waves-effect waves-light"
                    style="width: 140px;"
                    v-on:click="transfer(+amount, user.cutomer_id)"
                  >
                    Send Credits
                  </button>
                </div>
              </div>
            </div>
          </div>
          <!-- Second column -->
        </div>
        <!-- Panel data -->
      </div>
      <!-- Card content -->
    </div>
    <!-- Grid column -->

    <!-- Grid column -->
    <!-- Grid column -->
  </div>
</template>

<script>
import api from "../api.js";
export default {
  name: "Customer",
  data() {
    return {
      lists: [],
      user: {},
      amount: "",
    };
  },
  methods: {
    async listCustomer() {
      try {
        const response = await api.get("/users/");
        this.lists = response.data;
      } catch {
        console.log("error");
      }
    },
    isUUID(uuid) {
      let s = "" + uuid;

      s = s.match(
        "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
      );
      if (s === null) {
        return false;
      }
      return true;
    },
    transfer(amount, id) {
      if(amount!=NaN && this.isUUID(id)){
        api.post('/transfer/',{'FROM':'2d3bbc60-9f18-4f90-b150-d5e3489e2c34','TO':id,'AMOUNT':amount})
        .then(function(response){
          alert(response.data)
          this.user=''
          this.amount=''
        })
        .catch(error=>alert(response.data))
      }
      else{
        alert('if Not worked')
      }
    },
  },
  created() {
    this.listCustomer();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
