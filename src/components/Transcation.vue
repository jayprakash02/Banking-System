<template>
    <section>

            <!-- Top Table UI -->
            <div class="table-ui p-2 mb-3 mx-4 mb-5">

              <!-- Grid row -->
              <div class="row">

                <!-- Grid column -->
                <div class="col-xl-3 col-md-6">

                  <!-- Name -->
                  <select class="mdb-select colorful-select dropdown-info mx-2 md-form mt-3 md-dropdown">
                    <option value="" disabled="" selected="">Bulk actions</option>
                    <option value="1">Delate</option>
                    <option value="2">Export</option>
                    <option value="3">Change segment</option>
                  </select>

                </div>
                <!-- Grid column -->

                <!-- Grid column -->
                <div class="col-xl-3 col-md-6">

                  <!-- Blue select -->
                  <select class="mdb-select colorful-select dropdown-info mx-2 md-form mt-3 md-dropdown">
                    <option value="" disabled="" selected="">Show only</option>
                    <option value="1">All  (2000)</option>
                    <option value="2">Never opened  (200)</option>
                    <option value="3">Opened but unanswered  (1800)</option>
                    <option value="4">Answered  (200)</option>
                    <option value="5">Unsunscribed  (50)</option>
                  </select>

                </div>
                <!-- Grid column -->

                <!-- Grid column -->
                <div class="col-xl-3 col-md-6">

                  <!-- Blue select -->
                  <select class="mdb-select colorful-select dropdown-info mx-2 md-form mt-3 md-dropdown">
                    <option value="" disabled="" selected="">Filter segments</option>
                    <option value="1">Contacts in no segments  (100)</option>
                    <option value="1">Segment 1  (2000)</option>
                    <option value="2">Segment 2  (1000)</option>
                    <option value="3">Segment 3  (4000)</option>
                  </select>

                </div>
                <!-- Grid column -->

                <!-- Grid column -->
                <div class="col-xl-3 col-md-6">

                  <form class="form-inline mt-2 ml-2">
                    <div class="form-group md-form mt-2">
                      <input class="form-control w-100 text-white" type="text" placeholder="Search">
                    </div>
                    <button class="btn btn-sm btn-primary ml-2 mr-0 mb-md-0 mb-4 px-2 waves-effect waves-light dark-grey-text text-white"><i class="fas fa-search text-white"></i></button>
                  </form>

                </div>
                <!-- Grid column -->

              </div>
              <!-- Grid row -->

            </div>
            <!-- Top Table UI -->

            <div class="card card-cascade narrower z-depth-0 dark-card-admin text-white">

              <div class="view view-cascade gradient-card-header blue-gradient narrower py-2 mx-4 mb-3 d-flex justify-content-between align-items-center white black lighten-4">

                <div>
                  <button type="button" class="btn btn-outline-white btn-rounded btn-sm px-2 waves-effect waves-light dark-grey-text text-white"><i class="fas fa-th-large mt-0 text-white"></i></button>
                  <button type="button" class="btn btn-outline-white btn-rounded btn-sm px-2 waves-effect waves-light dark-grey-text text-white"><i class="fas fa-columns mt-0 text-white"></i></button>
                </div>

                <a href="" class="white-text mx-3">Table name</a>

                <div>
                  <button type="button" class="btn btn-outline-white btn-rounded btn-sm px-2 waves-effect waves-light dark-grey-text text-white"><i class="fas fa-pencil-alt mt-0 text-white"></i></button>
                  <button type="button" class="btn btn-outline-white btn-rounded btn-sm px-2 waves-effect waves-light dark-grey-text text-white"><i class="fas fa-eraser mt-0 text-white"></i></button>
                  <button type="button" class="btn btn-outline-white btn-rounded btn-sm px-2 waves-effect waves-light dark-grey-text text-white"><i class="fas fa-info-circle mt-0 text-white"></i></button>
                </div>

              </div>

              <div class="px-4">

                <div class="table-responsive">

                  <!--Table-->
                  <table class="table table-hover mb-0">

                    <!-- Table head -->
                    <thead>
                      <tr>
                        <th class="text-white">
                          <input class="form-check-input text-white" type="checkbox" id="checkbox">
                          <label for="checkbox" class="form-check-label mr-2 label-table text-white"></label>
                        </th>
                        <th class="th-lg text-white"><a>First Name <i class="fas fa-sort ml-1 text-white"></i></a></th>
                        <th class="th-lg text-white"><a>Last Name<i class="fas fa-sort ml-1 text-white"></i></a></th>
                        <th class="th-lg text-white"><a>Username<i class="fas fa-sort ml-1 text-white"></i></a></th>
                        <th class="th-lg text-white"><a>Email<i class="fas fa-sort ml-1 text-white"></i></a></th>
                        <th class="th-lg text-white"><a>Country<i class="fas fa-sort ml-1 text-white"></i></a></th>
                        <th class="th-lg text-white"><a>City<i class="fas fa-sort ml-1 text-white"></i></a></th>
                      </tr>
                    </thead>
                    <!-- Table head -->

                    <!-- Table body -->
                    <tbody>
                      <tr>
                        <th scope="row" class="text-white">
                          <input class="form-check-input text-white" type="checkbox" id="checkbox1">
                          <label for="checkbox1" class="label-table text-white"></label>
                        </th>
                        <td class="text-white">Mark</td>
                        <td class="text-white">Otto</td>
                        <td class="text-white">@mdo</td>
                        <td class="text-white">markotto@gmail.com</td>
                        <td class="text-white">USA</td>
                        <td class="text-white">San Francisco</td>
                      </tr>
                      <tr>
                        <th scope="row" class="text-white">
                          <input class="form-check-input text-white" type="checkbox" id="checkbox2">
                          <label for="checkbox2" class="label-table text-white"></label>
                        </th>
                        <td class="text-white">Jacob</td>
                        <td class="text-white">Thornton</td>
                        <td class="text-white">@fat</td>
                        <td class="text-white">jacobt@gmail.com</td>
                        <td class="text-white">France</td>
                        <td class="text-white">Paris</td>
                      </tr>
                      <tr>
                        <th scope="row" class="text-white">
                          <input class="form-check-input text-white" type="checkbox" id="checkbox3">
                          <label for="checkbox3" class="label-table text-white"></label>
                        </th>
                        <td class="text-white">Larry</td>
                        <td class="text-white">the Bird</td>
                        <td class="text-white">@twitter</td>
                        <td class="text-white">larrybird@gmail.com</td>
                        <td class="text-white">Germany</td>
                        <td class="text-white">Berlin</td>
                      </tr>
                      <tr>
                        <th scope="row" class="text-white">
                          <input class="form-check-input text-white" type="checkbox" id="checkbox4">
                          <label for="checkbox4" class="label-table text-white"></label>
                        </th>
                        <td class="text-white">Paul</td>
                        <td class="text-white">Topolski</td>
                        <td class="text-white">@P_Topolski</td>
                        <td class="text-white">ptopolski@gmail.com</td>
                        <td class="text-white">Poland</td>
                        <td class="text-white">Warsaw</td>
                      </tr>
                      <tr>
                        <th scope="row" class="text-white">
                          <input class="form-check-input text-white" type="checkbox" id="checkbox5">
                          <label for="checkbox5" class="label-table text-white"></label>
                        </th>
                        <td class="text-white">Anna</td>
                        <td class="text-white">Doe</td>
                        <td class="text-white">@andy</td>
                        <td class="text-white">annadoe@gmail.com</td>
                        <td class="text-white">Spain</td>
                        <td class="text-white">Madrid</td>
                      </tr>
                    </tbody>
                    <!-- Table body -->

                  </table>
                  <!-- Table -->

                </div>

                <hr class="my-0">

                <!-- Bottom Table UI -->
                <div class="d-flex justify-content-between">

                  <!-- Name -->
                  <select class="mdb-select colorful-select dropdown-primary md-form hidden-md-down">
                    <option value="" disabled="">Rows number</option>
                    <option value="1" selected="">5 rows</option>
                    <option value="2">25 rows</option>
                    <option value="3">50 rows</option>
                    <option value="4">100 rows</option>
                  </select>

                  <!-- Pagination -->
                  <nav class="my-4">
                    <ul class="pagination pagination-circle pg-blue mb-0">

                      <!--First-->
                      <li class="page-item disabled clearfix d-none d-md-block"><a class="page-link waves-effect waves-effect text-white">First</a></li>

                      <!-- Arrow left -->
                      <li class="page-item disabled">
                        <a class="page-link waves-effect waves-effect text-white" aria-label="Previous">
                          <span aria-hidden="true">«</span>
                          <span class="sr-only">Previous</span>
                        </a>
                      </li>

                      <!-- Numbers -->
                      <li class="page-item active"><a class="page-link waves-effect waves-effect text-white">1</a></li>
                      <li class="page-item"><a class="page-link waves-effect waves-effect text-white">2</a></li>
                      <li class="page-item"><a class="page-link waves-effect waves-effect text-white">3</a></li>
                      <li class="page-item"><a class="page-link waves-effect waves-effect text-white">4</a></li>
                      <li class="page-item"><a class="page-link waves-effect waves-effect text-white">5</a></li>

                      <!-- Arrow right -->
                      <li class="page-item">
                        <a class="page-link waves-effect waves-effect text-white" aria-label="Next">
                          <span aria-hidden="true">»</span>
                          <span class="sr-only">Next</span>
                        </a>
                      </li>

                      <!-- First -->
                      <li class="page-item clearfix d-none d-md-block"><a class="page-link waves-effect waves-effect text-white">Last</a></li>

                    </ul>
                  </nav>
                  <!-- Pagination -->

                </div>
                <!-- Bottom Table UI -->

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
