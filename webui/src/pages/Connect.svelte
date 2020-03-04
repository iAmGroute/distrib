<script>
  import { get } from '../api.js';

  let canClick = true;
  let lines    = '';
  let btnText  = 'Connect';
  let btnClass = 'btn-primary';

  async function handleClick(event) {
    if (!canClick) return;
    canClick = false;
    try {
      btnText  = 'Connecting';
      btnClass = 'btn-warning';
      let count = 0;
      for (const line of lines.split('\n')) {
        const pos = line.lastIndexOf(':');
        if (pos < 0) continue;
        const host = line.slice(0, pos);
        const port = line.slice(pos + 1);
        count += 1;
        await get('connectToNeighbor', {host, port});
      }
      if (count) {
        btnText  = `Will connect to ${count} neighbors`;
        btnClass = 'btn-success';
      }
      else {
        btnText  = 'Connect';
        btnClass = 'btn-primary';
      }
    }
    catch (error) {
      btnText  = 'Connect failed';
      btnClass = 'btn-danger';
      canClick = true;
    }
  }
</script>

<div class="col-lg-6">
  <div class="card card-primary card-outline">
    <div class="card-header">
      <h5 class="card-title">Enter hosts to connect to (one per line)</h5>
    </div>
    <div class="card-body">
      <textarea bind:value={lines} class="form-control" rows="10" placeholder="10.0.0.1:5000"></textarea>
    </div>
    <div class="card-footer">
      <button on:click={handleClick} class="btn {btnClass}">{btnText}</button>
    </div>
  </div>
</div>
