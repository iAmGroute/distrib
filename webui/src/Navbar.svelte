<script>
  import active from 'svelte-spa-router/active';
  export let state;
</script>

<!-- Navbar -->
<nav class="main-header navbar navbar-expand navbar-white navbar-light">
  <!-- Left navbar links -->
  <ul class="navbar-nav">
    <li class="nav-item d-none d-sm-inline-block">
      <a href="#/" use:active class="nav-link">Home</a>
    </li>
  </ul>
  <!-- Right navbar links -->
  <ul class="navbar-nav ml-auto">
    <li class="nav-item">
      <h5 class="nav-link m-0">{state.isLive ? "Live" : "Offline"}</h5>
    </li>
  </ul>
</nav>
