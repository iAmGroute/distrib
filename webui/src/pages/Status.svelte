<script>
  export let state;
</script>

<div class="col-sm-2">
  <div class="card card-primary card-outline">
    <div class="card-header">
      <h5 class="card-title">Listening on</h5>
    </div>
    <div class="card-body">
      [{state.content.status.host}]:{state.content.status.port}
    </div>
  </div>
</div>

<div class="col-sm-2">
  <div class="card card-primary card-outline">
    <div class="card-header">
      <h5 class="card-title">Blockchain length</h5>
    </div>
    <div class="card-body">
      {state.content.status.blockchain.length} Blocks
    </div>
  </div>
</div>

<div class="col-sm-2">
  <div class="card card-primary card-outline">
    <div class="card-header">
      <h5 class="card-title">Connected to</h5>
    </div>
    <div class="card-body">
      {state.content.status.neighbors.length} Neighbors
    </div>
  </div>
</div>
