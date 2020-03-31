<script>
  import { printHash, printDate } from '../lib.js';

  export let title, promise;
</script>

<div class="col-lg-12">
  <div class="card card-primary card-outline">
    <div class="card-header">
      <h4 class="card-title">{title}</h4>
    </div>
    <div class="card-body table-responsive p-0">
      {#await promise}
        <div class="alert alert-info">
          <h5><i class="icon fas fa-info"></i> Please wait !</h5>
          <p>Getting blocks ...</p>
        </div>
      {:then blocks}
        <table class="table table-striped table-hover table-valign-middle">
          <thead>
            <tr>
              <th>Block ID</th>
              <th>PoW</th>
              <th>Nonce</th>
              <th>Hash</th>
              <th>Previous</th>
              <th>Timestamp</th>
              <th>Transactions</th>
            </tr>
          </thead>
          <tbody>
            {#each blocks as {myID, powHash, nonce, thisHash, prevHash, timestamp, txCount}, i}
              <tr>
                <td><a href="#/block?{myID}">{myID}</a></td>
                <td>{printHash(powHash)}...</td>
                <td>{nonce}</td>
                <td>{printHash(thisHash)}...</td>
                <td>{printHash(prevHash)}...</td>
                <td>{printDate(timestamp)}</td>
                <td>{txCount}</td>
              </tr>
            {/each}
          </tbody>
        </table>
      {:catch error}
        <div class="alert alert-danger">
          <h5><i class="icon fas fa-ban"></i> Couldn't fetch a block !</h5>
          <p>{error}</p>
        </div>
      {/await}
    </div>
  </div>
</div>
