<script>
  import { printHash } from '../lib.js';
  import { get }       from '../api.js';

  export let state;

  async function disconnect(guid) {
    await get('disconnectNeighbor', {guid});
  }
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
      <table class="table table-striped table-hover">
        <thead>
          <tr>
            <th>Host</th>
            <th>Port</th>
            <th>Address</th>
            <th>Blocks</th>
            <th>Connected</th>
            <th>Status</th>
            <th>Disconnect</th>
          </tr>
        </thead>
        <tbody>
          {#each state.content.status.neighbors as {peerName, guid, lastBlockID, connected, isSyncing}}
            <tr>
              <td>{peerName[0]}</td>
              <td>{peerName[1]}</td>
              <td>{printHash(guid)}...</td>
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
              <td>
                <button on:click|once={() => disconnect(guid)} class="btn btn-danger badge-btn">&times;</button>
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </div>
</div>
