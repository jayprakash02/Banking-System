<template>
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
                    <h4 class="font-weight-bold">{{name}}</h4>
                  </div>
                </div>

                <!-- Card content -->
                <div class="card-body card-body-cascade">
                  <p class="card-text text-white">
                    Email:
                  </p>
                  <p class="font-weight-bold">{{email}}</p>

                  <p class="card-text text-white">Credit Available:</p>
                  <h4 class="font-weight-bold">{{credit}}</h4>

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
</template>
<script>
const $ = window.jQuery;

export default {
    name: "Personal",
    data(){
        return {
            name:'',
            id:'',
            email:'',
            credit:0,
        }
    },
    created(){
        
    }
}
</script>