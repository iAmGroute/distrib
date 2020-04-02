<script>
  import { querystring }              from 'svelte-spa-router'
  import { printHash, printDateLong } from '../lib.js';
  import { get }                      from '../api.js';

  let blockID      = 0;
  let indexInBlock = 0;

  querystring.subscribe(v => {
    const txRef  = v.split(':');
    blockID      = parseInt(txRef[0]);
    indexInBlock = parseInt(txRef[1]);
  });

  async function getTransaction(blockID, indexInBlock) {
    return await get('getTransaction', {blockID, indexInBlock});
  }
</script>

{#await getTransaction(blockID, indexInBlock)}
  <div class="alert alert-info">
    <h5><i class="icon fas fa-info"></i> Please wait !</h5>
    <p>Getting transaction info ...</p>
  </div>
{:then tx}
  <div class="col-sm-2">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h5 class="card-title">ID</h5>
      </div>
      <div class="card-body">{blockID}:{indexInBlock}</div>
    </div>
  </div>
  <div class="col-sm-2">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h5 class="card-title">Total coins</h5>
      </div>
      <div class="card-body">{tx.coins}</div>
    </div>
  </div>
  <div class="col-sm-4">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h5 class="card-title">Signature</h5>
      </div>
      <div class="card-body">{tx.signature}</div>
    </div>
  </div>
  <div class="col-sm-4">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h5 class="card-title">Sender's address</h5>
      </div>
      <div class="card-body">{tx.senderAddress}</div>
    </div>
  </div>
  <hr />
  <div class="col-lg-6">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h4 class="card-title">Inputs: {tx.inputs.length}</h4>
      </div>
      <div class="card-body table-responsive p-0">
        <table class="table table-striped table-hover table-valign-middle">
          <thead>
            <tr>
              <th>Index</th>
              <th>Transaction</th>
              <th>Coins</th>
            </tr>
          </thead>
          <tbody>
            {#each tx.inputs as {inTxBlockID, inTxIndex, amount}, i}
              <tr>
                <td>{i}</td>
                <td><a href="#/tx?{inTxBlockID}:{inTxIndex}">{inTxBlockID}:{inTxIndex}</a></td>
                <td>{amount} NBC</td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="col-lg-6">
    <div class="card card-primary card-outline">
      <div class="card-header">
        <h4 class="card-title">Outputs: {tx.outputs.length}</h4>
      </div>
      <div class="card-body table-responsive p-0">
        <table class="table table-striped table-hover table-valign-middle">
          <thead>
            <tr>
              <th>Index</th>
              <th>Recipient</th>
              <th>Coins</th>
            </tr>
          </thead>
          <tbody>
            {#each tx.outputs as {address, amount}, i}
              <tr>
                <td>{i}</td>
                <td>{printHash(address)}...</td>
                <td>{amount} NBC</td>
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
