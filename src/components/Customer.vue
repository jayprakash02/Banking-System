<template>
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
                    <p class="text-uppercase text-white">Personal Details</p>
                    <h4 class="font-weight-bold">Jay Prakash</h4>
                  </div>
                </div>

                <!-- Card content -->
                <div class="card-body card-body-cascade">
                  <p class="card-text text-white">
                    Email:
                  </p>
                  <p class="font-weight-bold">unijay12@gmail.com</p>

                  <p class="card-text text-white">Credit Available:</p>
                  <h4 class="font-weight-bold">2000</h4>

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
              </div>
            </div>
          </div>
        </div>

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
                          <p class="heading lead">Modal Info</p>

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
                          <fieldset class="form-check mb-4">
                            <input
                              class="form-check-input"
                              name="group1"
                              type="radio"
                              id="radio1"
                              checked="checked"
                            />
                            <label class="form-check-label" for="radio1"
                              >Option 1</label
                            >
                          </fieldset>

                          <fieldset class="form-check mb-4">
                            <input
                              class="form-check-input"
                              name="group1"
                              type="radio"
                              id="radio2"
                            />
                            <label class="form-check-label" for="radio2"
                              >Option 2</label
                            >
                          </fieldset>

                          <fieldset class="form-check mb-4">
                            <input
                              class="form-check-input"
                              name="group1"
                              type="radio"
                              id="radio3"
                            />
                            <label class="form-check-label" for="radio3"
                              >Option 3</label
                            >
                          </fieldset>
                        </div>

                        <!-- Footer -->
                        <div class="modal-footer justify-content-center">
                          <a type="button" class="btn btn-info"
                            >Get it now <i class="far fa-gem ml-1"></i
                          ></a>
                          <a
                            type="button"
                            class="btn btn-outline-success waves-effect"
                            data-dismiss="modal"
                            >No, thanks</a
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
                    <input type="text" id="username12" class="form-control" />
                    <label for="username12">Amount</label>
                    <div class="md-form md-outline">
                      <div class="card-foter text-right">
                        <button
                          type="button"
                          class="btn btn-outline-warning btn-sm waves-effect waves-light"
                          style="width: 140px;"
                        >
                          Send message
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
</template>

<script>
export default {
  name: "Customer",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
