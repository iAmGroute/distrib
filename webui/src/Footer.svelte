<script>
  export let state;
</script>

<!-- Main Footer -->
<footer class="main-footer">
  <!-- To the right -->
  <span class="float-right">
    <strong>Noobcash Web UI</strong>, based on <a href="https://github.com/ColorlibHQ/AdminLTE" target="_blank">AdminLTE.io</a>
  </span>
  <!-- Default to the left -->
  <h5 class="m-0">{state.isLive ? "Live" : "Offline"}</h5>
</footer>
