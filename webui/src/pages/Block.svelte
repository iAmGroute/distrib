<script>
  import { querystring }              from 'svelte-spa-router'
  import { printHash, printDateLong } from '../lib.js';
  import { get }                      from '../api.js';

  const blockID = parseInt($querystring);

  async function getBlock(i) {
    return await get('getBlock', {blockID: i, detailed: true});
  }
</script>

{#await getBlock(blockID)}
  <div class="alert alert-info">
    <h5><i class="icon fas fa-info"></i> Please wait !</h5>
    <p>Getting block info ...</p>
  </div>
{:then block}
  <div class="col-sm-2">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h5 class="card-title">ID</h5>
      </div>
      <div class="card-body">{block.myID}</div>
    </div>
  </div>
  <div class="col-sm-2">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h5 class="card-title">PoW hash</h5>
      </div>
      <div class="card-body">{block.powHash}</div>
    </div>
  </div>
  <div class="col-sm-2">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h5 class="card-title">Nonce</h5>
      </div>
      <div class="card-body">{block.nonce}</div>
    </div>
  </div>
  <div class="col-sm-2">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h5 class="card-title">Own hash</h5>
      </div>
      <div class="card-body">{block.thisHash}</div>
    </div>
  </div>
  <div class="col-sm-2">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h5 class="card-title">Previous block's hash</h5>
      </div>
      <div class="card-body">{block.prevHash}</div>
    </div>
  </div>
  <div class="col-sm-2">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h5 class="card-title">Timestamp</h5>
      </div>
      <div class="card-body">{printDateLong(block.timestamp)}</div>
    </div>
  </div>
  <div class="col-lg-12">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h4 class="card-title">Transactions: {block.txCount}</h4>
      </div>
      <div class="card-body table-responsive p-0">
        <table class="table table-striped table-hover table-valign-middle">
          <thead>
            <tr>
              <th>Index</th>
              <th>Signature</th>
              <th>Sender</th>
              <th>Inputs</th>
              <th>Outputs</th>
              <th>Coins</th>
            </tr>
          </thead>
          <tbody>
            {#each block.txs as {signature, senderAddress, inputCount, outputCount, coins}, i}
              <tr>
                <td><a href="#/tx?{blockID}:{i}">{i}</a></td>
                <td>{printHash(signature)}...</td>
                <td>{printHash(senderAddress)}...</td>
                <td>{inputCount}</td>
                <td>{outputCount}</td>
                <td>{coins} NBC</td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    </div>
  </div>
{:catch error}
  <div class="alert alert-danger">
    <h5><i class="icon fas fa-ban"></i> Couldn't fetch block !</h5>
    <p>{error}</p>
  </div>
{/await}
