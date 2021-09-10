<template>
  <section>
    <div
      class="card card-cascade narrower z-depth-0 dark-card-admin text-white"
    >
      <div
        class="view view-cascade gradient-card-header blue-gradient narrower py-2 mx-4 mb-3 d-flex justify-content-between align-items-center white black lighten-4"
      >
        <div></div>

        <a href="" class="white-text mx-3">Transaction History</a>

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
                    >Transcation ID<i class="fas fa-sort ml-1 text-white"></i
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

        <a href="" class="white-text mx-3">Transaction History</a>

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
                    >Transcation ID<i class="fas fa-sort ml-1 text-white"></i
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
</template>
<script>
import api from "../api.js";
export default {
  name: "Transcation",
  data() {
    return {
      transactions_credit: [],
      transactions_transfer: [],
    };
  },
  methods: {
    async getTable() {
      const params = new URLSearchParams([
        ["ID", "2d3bbc60-9f18-4f90-b150-d5e3489e2c34"],
      ]);
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
    this.getTable();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
