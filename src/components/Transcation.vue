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
            <tbody>
              <tr>
                <td class="text-white">markotto@gmail.com</td>
                <td class="text-white">Mark</td>
                <td class="text-white">200</td>
                <td class="text-white">qqqqqqqqqqqqqqqqqqqqqsssssssssssss</td>
              </tr>
              <tr>
                <td class="text-white">markotto@gmail.com</td>
                <td class="text-white">Mark</td>
                <td class="text-white">200</td>
                <td class="text-white">qqqqqqqqqqqqqqqqqqqqqsssssssssssss</td>
              </tr>
              <tr>
                <td class="text-white">markotto@gmail.com</td>
                <td class="text-white">Mark</td>
                <td class="text-white">200</td>
                <td class="text-white">qqqqqqqqqqqqqqqqqqqqqsssssssssssss</td>
              </tr>
              <tr>
                <td class="text-white">markotto@gmail.com</td>
                <td class="text-white">Mark</td>
                <td class="text-white">200</td>
                <td class="text-white">qqqqqqqqqqqqqqqqqqqqqsssssssssssss</td>
              </tr>
              <tr>
                <td class="text-white">markotto@gmail.com</td>
                <td class="text-white">Mark</td>
                <td class="text-white">200</td>
                <td class="text-white">qqqqqqqqqqqqqqqqqqqqqsssssssssssss</td>
              </tr>
            </tbody>
            <!-- Table body -->
          </table>
          <!-- Table -->
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: "Transcation",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
