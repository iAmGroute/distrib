<script>
  export let state;
</script>

<div class="col">
  <div class="card card-primary">
    <div class="card-header">
      <h3 class="card-title">Neighbors</h3>
      <span class='badge badge-light badge-pill float-right'>
        {state.content.status.neighbors.length}
      </span>
    </div>
    <div class="card-body table-responsive p-0">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>#</th>
            <th>Host</th>
            <th>Port</th>
            <th>Blocks</th>
            <th>Connected</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {#each state.content.status.neighbors as {peerName, lastBlockID, connected, isSyncing}, i}
            <tr>
              <td>{i}</td>
              <td>{peerName[0]}</td>
              <td>{peerName[1]}</td>
              <td>{lastBlockID + 1}</td>
              <td>
                <span class={connected ? 'badge badge-success' : 'badge badge-danger'}>
                  {connected ? 'OK' : 'DISC'}
                </span>
              </td>
              <td>
                <span class={!isSyncing ? 'badge badge-success' : 'badge badge-warning'}>
                  {!isSyncing ? 'OK' : 'Syncing'}
                </span>
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </div>
</div>
