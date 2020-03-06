<script>
  import active from 'svelte-spa-router/active';
</script>

<!-- Main Sidebar Container -->
<aside class="main-sidebar sidebar-dark-primary">
  <!-- Brand Logo -->
  <a href="/" class="brand-link">
    <img src="dist/img/logo.png" alt="logo" class="brand-image">
    <span class="brand-text">Noobcash</span>
  </a>
  <!-- Sidebar -->
  <div class="sidebar">
    <nav class="mt-2">
      <ul class="nav nav-pills nav-sidebar flex-column">
        <li class="nav-item">
          <a href="#/" use:active class="nav-link">
            <i class="nav-icon fas fa-home"></i>
            <p>Home</p>
          </a>
        </li>
        <li class="nav-item">
          <a href="#/status" use:active class="nav-link">
            <i class="nav-icon fas fa-tachometer-alt"></i>
            <p>Status</p>
          </a>
        </li>
        <li class="nav-item">
          <a href="#/wallet" use:active class="nav-link">
            <i class="nav-icon fas fa-wallet"></i>
            <p>Wallet</p>
          </a>
        </li>
        <li class="nav-item">
          <a href="#/network" use:active class="nav-link">
            <i class="nav-icon fas fa-network-wired"></i>
            <p>Network</p>
          </a>
        </li>
        <li class="nav-item">
          <a href="#/connect" use:active class="nav-link">
            <i class="nav-icon fas fa-plug"></i>
            <p>Connect</p>
          </a>
        </li>
        <li class="nav-item">
          <a href="#/example" use:active class="nav-link">
            <i class="nav-icon fas fa-th"></i>
            <p>
              Example
              <span class="right badge badge-danger">New</span>
            </p>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</aside>
