<script>
  import { get } from '../api.js';

  export let state;

  function printHash(h) {
    return h.slice(0, 16);
  }
  function printDate(unixTime) {
    const d = new Date(unixTime * 1000);
    return d.toLocaleString(undefined, {
      dateStyle: "medium",
      timeStyle: "medium",
      hour12: false
    });
  }

  async function getBlocks() {
    const to     = state.content.status.blockchain.length;
    const from   = to - 10;
    const blocks = [];
    for (let i = from; i < to; i++) {
      blocks.push(await get('getBlock', {blockID: i}));
    }
    return blocks;
  }
</script>

<div class="col-lg-12">
  <div class="card card-primary card-outline">
    <div class="card-header">
      <h4 class="card-title">Showing last 10 of {state.content.status.blockchain.length} blocks</h4>
    </div>
    <div class="card-body table-responsive p-0">
      {#await getBlocks()}
        <div class="alert alert-info">
          <button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button>
          <h5><i class="icon fas fa-info"></i> Please wait !</h5>
          <p>Getting latest blocks ...</p>
        </div>
      {:then blocks}
        <table class="table table-striped table-valign-middle">
          <thead>
            <tr>
              <th>Block ID</th>
              <th>This Hash</th>
              <th>Previous Hash</th>
              <th>Timestamp</th>
              <th>Transactions</th>
            </tr>
          </thead>
          <tbody>
            {#each blocks as {myID, thisHash, prevHash, timestamp, txCount}, i}
              <tr>
                <td>{myID}</td>
                <td>{printHash(thisHash)}</td>
                <td>{printHash(prevHash)}</td>
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
