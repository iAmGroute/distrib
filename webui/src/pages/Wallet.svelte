<script>
  import { get } from '../api.js';

  export let state;

  let canClick      = true;
  let sendToAddress = '';
  let sendAmount    = 0;
  let btnText       = 'Send coins';
  let btnClass      = 'btn-primary';

  function resetFields() {
    canClick      = true;
    sendToAddress = '';
    sendAmount    = 0;
    btnText       = 'Send coins';
    btnClass      = 'btn-primary';
  }

  async function handleClick(event) {
    if (!canClick) return;
    canClick = false;
    try {
      if (sendToAddress.length !== 512)                                       throw 'Bad address';
      if (sendAmount < 0 || sendAmount > state.content.status.wallet.balance) throw 'Insufficient coins';
      btnText  = 'Creating transaction';
      btnClass = 'btn-warning';
      await get('sendCoins', {address: sendToAddress, amount: sendAmount});
      btnText  = 'Transaction submitted';
      btnClass = 'btn-success';
    }
    catch (error) {
      console.log(error);
      btnText  = 'Can\'t submit transaction';
      btnClass = 'btn-danger';
      canClick = true;
    }
  }
</script>

<div class="col-sm-2">
  <div class="card card-primary card-outline">
    <div class="card-header">
      <h5 class="m-0">My balance</h5>
    </div>
    <div class="card-body">
      <h6 class="card-title">{state.content.status.wallet.balance} NBC</h6>
    </div>
  </div>
</div>

<div class="col-sm-4">
  <div class="card card-primary card-outline">
    <div class="card-header">
      <h5 class="m-0">My address</h5>
    </div>
    <div class="card-body">
      {state.content.status.wallet.address}
    </div>
  </div>
</div>

<div class="col-lg-6">
  <div class="card card-primary card-outline">
    <div class="card-header">
      <h5 class="card-title">New transaction</h5>
    </div>
    <div class="card-body">
      <div class="form-group">
        <label>Recipient</label>
        <input bind:value={sendToAddress} type="text" class="form-control" placeholder="Enter recipient's address" />
      </div>
      <div class="form-group">
        <label>Amount </label>
        <div class="input-group">
          <input bind:value={sendAmount} type="number" min="0" max={state.content.status.wallet.balance} step="1" class="form-control" placeholder="0" />
          <div class="input-group-append">
            <span class="input-group-text">NBC</span>
          </div>
        </div>
      </div>
    </div>
    <div class="card-footer">
      <button on:click={handleClick} class="btn {btnClass}">{btnText}</button>
      <button on:click={resetFields} class="btn btn-danger float-right">Reset</button>
    </div>
  </div>
</div>

<div class="col-12">
  <div class="card card-primary">
    <div class="card-header">
      <h5 class="m-0">Unspent transaction outputs</h5>
    </div>
    <div class="card-body table-responsive p-0">
      <table class="table table-striped table-hover">
        <thead>
          <tr>
            <th>#</th>
            <th>Transaction</th>
            <th>Amount (NBC)</th>
          </tr>
        </thead>
        <tbody>
          {#each state.content.status.wallet.utxos as [[blockID, indexInBlock], amount], i}
            <tr>
              <td>{i}</td>
              <td><a href="#/tx?{blockID}:{indexInBlock}">{blockID + ':' + indexInBlock}</a></td>
              <td>{amount}</td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </div>
</div>
