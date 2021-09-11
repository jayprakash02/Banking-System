<template>
  <header>
    <nav
      class="navbar fixed-top navbar-expand-lg scrolling-navbar double-nav white-skin navy-blue-skin"
    >
      <!-- SideNav slide-out button -->
      <div class="float-left">
        <a href="#" data-activates="slide-out" class="button-collapse"
          ><i class="fas fa-bars text-white"></i
        ></a>
      </div>

      <!-- Breadcrumb -->
      <div class="breadcrumb-dn mr-auto">
        <p class="text-white">BANK OF SBS</p>
      </div>
    </nav>
  </header>
  <main>
    <div class="home">
      <section class="mt-md-4 pt-md-2 mb-5 pb-4">
        <!-- Card -->

        <!-- Section: Chart -->
        <section>
          <!-- Grid row -->
          <div class="row">
            <!-- Grid column -->
            <div class="col-xl-5 col-lg-12 mr-0 pb-2">
              <div class="row py-3 pl-4">
                <div class="col-md-12">
                  <div
                    class="card card-cascade cascading-admin-card dark-card-admin text-white"
                  >
                    <!-- Card Data -->
                    <div class="admin-up">
                      <div class="data">
                        <p class="text-uppercase text-white">
                          Personal Details
                        </p>
                        <h4 v-if="name" class="font-weight-bold">{{ name }}</h4>
                        <h4 v-else class="font-weight-bold">
                          <input
                            type="text"
                            placeholder="Enter your name"
                            v-model="temp_name"
                          />
                        </h4>
                      </div>
                    </div>

                    <!-- Card content -->
                    <div class="card-body card-body-cascade">
                      <p class="card-text text-white">
                        Email:
                      </p>
                      <p v-if="email" class="font-weight-bold">{{ email }}</p>
                      <p v-else class="font-weight-bold">
                        <input
                          type="text"
                          placeholder="Enter your email"
                          v-model="temp_email"
                        />
                      </p>
                      <div v-if="id">
                        <p class="card-text text-white">Credit Available:</p>
                        <h4 class="font-weight-bold">{{ credit }}</h4>

                        <div class="progress mb-3">
                          <div
                            class="progress-bar bg-primary"
                            role="progressbar"
                            style="width: 20%"
                            aria-valuenow="800"
                            aria-valuemin="0"
                            aria-valuemax="1000"
                          ></div>
                        </div>
                      </div>
                      <div v-else>
                        <button
                          type="button"
                          class="btn btn-primary success"
                          v-on:click="login(temp_name, temp_email)"
                        >
                          Give me Credits
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-xl-7 col-md-12 mr-0 pb-2">
              <!-- Card image -->
              <div
                class="card card-cascade narrower dark-card-admin text-white"
              >
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
                                <span aria-hidden="true" class="white-text"
                                  >&times;</span
                                >
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
                                <label
                                  class="form-check-label"
                                  :for="list.cutomer_id"
                                  >{{ list.name }}</label
                                >
                              </fieldset>
                            </div>

                            <!-- Footer -->
                            <div class="modal-footer justify-content-center">
                              <a
                                type="button"
                                class="btn btn-info"
                                data-dismiss="modal"
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
          </div>
          <!-- Grid row -->
        </section>

        <!-- Card -->
      </section>
      <section>
        <div
          class="card card-cascade narrower z-depth-0 dark-card-admin text-white"
        >
          <div
            class="view view-cascade gradient-card-header blue-gradient narrower py-2 mx-4 mb-3 d-flex justify-content-between align-items-center white black lighten-4"
          >
            <div></div>

            <a href="" class="white-text mx-3">Received History</a>

            <div></div>
          </div>

          <div class="px-4">
            <div class="table-responsive">
              <!--Table-->
              <table class="table table-hover mb-0">
                <!-- Table head -->
                <thead>
                  <tr>
                    <th class="th-lg text-white">
                      <a>Email <i class="fas fa-sort ml-1 text-white"></i></a>
                    </th>
                    <th class="th-lg text-white">
                      <a>Name<i class="fas fa-sort ml-1 text-white"></i></a>
                    </th>
                    <th class="th-lg text-white">
                      <a>Amount<i class="fas fa-sort ml-1 text-white"></i></a>
                    </th>
                    <th class="th-lg text-white">
                      <a
                        >Transcation ID<i
                          class="fas fa-sort ml-1 text-white"
                        ></i
                      ></a>
                    </th>
                  </tr>
                </thead>
                <!-- Table head -->

                <!-- Table body -->
                <tbody class="success">
                  <tr
                    v-for="transaction in transactions_credit"
                    :key="transaction.transcation_id"
                  >
                    <td class="text-white">{{ transaction.email }}</td>
                    <td class="text-white">{{ transaction.date }}</td>
                    <td class="text-white">{{ transaction.amount }}</td>
                    <td class="text-white">{{ transaction.transcation_id }}</td>
                  </tr>
                </tbody>

                <!-- Table body -->
              </table>
              <!-- Table -->
            </div>
          </div>
        </div>
        <div
          class="card card-cascade narrower z-depth-0 dark-card-admin text-white"
        >
          <div
            class="view view-cascade gradient-card-header blue-gradient narrower py-2 mx-4 mb-3 d-flex justify-content-between align-items-center white black lighten-4"
          >
            <div></div>

            <a href="" class="white-text mx-3">Transfer History</a>

            <div></div>
          </div>

          <div class="px-4">
            <div class="table-responsive">
              <!--Table-->
              <table class="table table-hover mb-0">
                <thead>
                  <tr>
                    <th class="th-lg text-white">
                      <a>Email <i class="fas fa-sort ml-1 text-white"></i></a>
                    </th>
                    <th class="th-lg text-white">
                      <a>Name<i class="fas fa-sort ml-1 text-white"></i></a>
                    </th>
                    <th class="th-lg text-white">
                      <a>Amount<i class="fas fa-sort ml-1 text-white"></i></a>
                    </th>
                    <th class="th-lg text-white">
                      <a
                        >Transcation ID<i
                          class="fas fa-sort ml-1 text-white"
                        ></i
                      ></a>
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="transaction in transactions_transfer"
                    :key="transaction.transcation_id"
                  >
                    <td class="text-white">{{ transaction.email }}</td>
                    <td class="text-white">{{ transaction.date }}</td>
                    <td class="text-white">{{ transaction.amount }}</td>
                    <td class="text-white">{{ transaction.transcation_id }}</td>
                  </tr>
                </tbody>
                <!-- Table body -->
              </table>
            </div>
          </div>
        </div>
      </section>
    </div>
  </main>
  <!-- Footer -->
  <!-- Footer -->
  <footer class="page-footer font-small unique-color-dark pt-4">
    <!-- Footer Elements -->
    <div class="container">
      <!-- Call to action -->

      <!-- Call to action -->
    </div>
    <!-- Footer Elements -->

    <!-- Copyright -->
    <div class="footer-copyright text-center py-3">
      © 2020 Copyright:
      <a href="https://github.com/jayprakash02/"> Jayprakash</a>
    </div>
    <!-- Copyright -->
  </footer>
  <!-- Footer -->
  <!-- Footer -->
</template>

<script>
const $ = window.jQuery;
import api from "./api.js";
export default {
  data() {
    return {
      name: "",
      temp_name: "",
      id: "",
      email: "",
      temp_email: "",
      credit: 0,
      lists: [],
      user: {},
      amount: "",
      transactions_credit: [],
      transactions_transfer: [],
    };
  },
  methods: {
    // Personal
    setCookies() {
      $.cookie("name", this.name);
      $.cookie("email", this.email);
      $.cookie("ID", this.id);
      $.cookie("credit", this.credit);
    },
    async intialise() {
      if ($.cookie("ID")) {
        const params = new URLSearchParams([["ID", $.cookie("ID")]]);
        const response = await api.get("/details/", { params });
        this.name = response.data.name;
        this.email = response.data.email;
        this.id = response.data.ID;
        this.credit = response.data.wallet;
        this.setCookies();
      }
    },
    async login(name, email) {
      if (name.length > 0 && email.length > 0) {
        const response = await api.post("/details/", {
          name: name,
          email: email,
        });
        this.name = response.data.name;
        this.email = response.data.email;
        this.id = response.data.ID;
        this.credit = response.data.wallet;
        this.setCookies();
      }
      this.getTable();
    },
    // Customer
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
      if (amount != NaN && this.isUUID(id)) {
        api
          .post("/transfer/", { FROM: $.cookie("ID"), TO: id, AMOUNT: amount })
          .then(function(response) {
            alert(response.data);
            this.user = "";
            this.amount = "";
          })
          .catch((error) => alert(response.data));
      } else {
        alert("if Not worked");
      }
      this.intialise();
      this.getTable();
    },
    // Table
    async getTable() {
      const params = new URLSearchParams([["ID", $.cookie("ID")]]);
      try {
        const response = await api.get("/transfer/", { params });
        this.transactions_credit = response.data.credit;
        this.transactions_transfer = response.data.transfer;
      } catch {
        console.log(error);
      }
    },
  },
  created() {
    this.intialise();
    this.listCustomer();
    this.getTable();
  },
};
</script>
