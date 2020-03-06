<script>
  export let state;
</script>

<div class="col-lg-3">
  <div class="card card-primary card-outline">
    <div class="card-header">
      <h5 class="m-0">Balance</h5>
    </div>
    <div class="card-body">
      <h6 class="card-title">{state.content.status.balance} NBC</h6>
    </div>
  </div>
</div>

<div class="col-lg-9">
  <div class="card card-primary">
    <div class="card-header">
      <h5 class="m-0">Unspent transaction outputs</h5>
    </div>
    <div class="card-body p-0">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>#</th>
            <th>Transaction hash</th>
            <th>Amount (NBC)</th>
          </tr>
        </thead>
        <tbody>
          {#each state.content.status.utxos as [txHash, amount], i}
            <tr>
              <td>{i}</td>
              <td><a href="#/tx/{txHash}">{txHash}</a></td>
              <td>{amount}</td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </div>
</div>
