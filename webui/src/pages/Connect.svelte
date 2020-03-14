<script>
  import { get } from '../api.js';

  let lines    = '';
  let canClick = true;
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

  const knownHosts = [
    ['10.0.0.1', 5000],
    ['10.0.1.0', 5000],
    ['10.0.1.1', 5000],
    ['10.0.1.2', 5000],
    ['10.0.1.3', 5000]
  ];
  let qcStates = knownHosts.map(([host, port]) => ({
    host,
    port,
    canClick: true,
    btnText:  'Connect',
    btnClass: 'btn-primary'
  }));

  console.log(qcStates);

  async function handleClickQC(i) {
    const s = qcStates[i];
    if (!s.canClick) return;
    s.canClick = false;
    try {
      s.btnText  = 'Connecting';
      s.btnClass = 'btn-warning';
      await get('connectToNeighbor', {host: s.host, port: s.port});
      s.btnText  = 'Will connect';
      s.btnClass = 'btn-success';
    }
    catch (error) {
      s.btnText  = 'Connect failed';
      s.btnClass = 'btn-danger';
      s.canClick = true;
    }
    qcStates[i] = s;
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

<div class="col-lg-6">
  <div class="card card-primary card-outline">
    <div class="card-header">
      <h5 class="card-title">Quick connect</h5>
    </div>
    <div class="card-body">
      <!-- <ul class="list-group-flush"> -->
      {#each qcStates as {host, port, canClick, btnText, btnClass}, i}
        <!-- <li class="list-group-item text-center"> -->
        <p>
          <span class="mx-3">{host}:{port}</span>
          <button on:click={() => handleClickQC(i)} class="btn {btnClass}">{btnText}</button>
        </p>
        <!-- </li> -->
      {/each}
      <!-- </ul> -->
    </div>
  </div>
</div>
