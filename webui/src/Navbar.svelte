<script>
  import active from 'svelte-spa-router/active';
  export let state;
</script>

<!-- Navbar -->
<nav class="main-header navbar navbar-expand navbar-white navbar-light">
  <!-- Left navbar links -->
  <ul class="navbar-nav">
    <li class="nav-item d-none d-sm-inline-block">
      <a href="#/blockchain" use:active class="nav-link">{state.content.status.blockchain.length} Blocks</a>
    </li>
    <li class="nav-item d-none d-sm-inline-block">
      <a href="#/wallet" use:active class="nav-link">{state.content.status.balance} NBC</a>
    </li>
    <li class="nav-item d-none d-sm-inline-block">
      <a href="#/network" use:active class="nav-link">{state.content.status.neighbors.length} Neighbors</a>
    </li>
  </ul>
  <!-- Right navbar links -->
  <ul class="navbar-nav ml-auto">
    <li class="nav-item">
      <h5 class="nav-link m-0">{state.isLive ? "Live" : "Offline"}</h5>
    </li>
  </ul>
</nav>
