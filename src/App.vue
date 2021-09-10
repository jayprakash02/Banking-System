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

      <div class="d-flex change-mode">
               <!-- Navbar links -->
        <ul class="nav navbar-nav nav-flex-icons ml-auto">
          <!-- Dropdown -->
          <li class="nav-item dropdown notifications-nav">
            <a
              class="nav-link dropdown-toggle waves-effect text-white"
              id="navbarDropdownMenuLink"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              <span class="badge red">3</span>
              <i class="fas fa-bell text-white"></i>
              <span class="d-none d-md-inline-block">Notifications</span>
            </a>
            <div
              class="dropdown-menu dropdown-primary"
              aria-labelledby="navbarDropdownMenuLink"
            >
              <a class="dropdown-item waves-effect waves-light" href="#">
                <i class="far fa-money-bill-alt mr-2" aria-hidden="true"></i>
                <span>New order received</span>
                <span class="float-right"
                  ><i class="far fa-clock" aria-hidden="true"></i> 13 min</span
                >
              </a>
              <a class="dropdown-item waves-effect waves-light" href="#">
                <i class="far fa-money-bill-alt mr-2" aria-hidden="true"></i>
                <span>New order received</span>
                <span class="float-right"
                  ><i class="far fa-clock" aria-hidden="true"></i> 33 min</span
                >
              </a>
              <a class="dropdown-item waves-effect waves-light" href="#">
                <i class="fas fa-chart-line mr-2" aria-hidden="true"></i>
                <span>Your campaign is about to end</span>
                <span class="float-right"
                  ><i class="far fa-clock" aria-hidden="true"></i> 53 min</span
                >
              </a>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link waves-effect text-white"
              ><i class="fas fa-envelope text-white"></i>
              <span class="clearfix d-none d-sm-inline-block">Contact</span></a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link waves-effect text-white"
              ><i class="far fa-comments text-white"></i>
              <span class="clearfix d-none d-sm-inline-block">Support</span></a
            >
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle waves-effect text-white"
              href="#"
              id="userDropdown"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              <i class="fas fa-user text-white"></i>
              <span class="clearfix d-none d-sm-inline-block">Profile</span>
            </a>
            <div
              class="dropdown-menu dropdown-menu-right"
              aria-labelledby="userDropdown"
            >
              <a class="dropdown-item waves-effect waves-light" href="#"
                >Log Out</a
              >
              <a class="dropdown-item waves-effect waves-light" href="#"
                >My account</a
              >
            </div>
          </li>
        </ul>
        <!-- Navbar links -->
      </div>
    </nav>
  </header>

  <router-link to="/">Home</router-link> |

  <main>
    <router-view />
  </main>
</template>

<style></style>
