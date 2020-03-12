<script>
  export let state;
</script>

<style>
  .small-box .icon>i {
    transition: none;
  }
  .small-box:hover .icon>i {
    font-size: 70px;
  }
  .small-box-footer {
    padding: 5px 0;
  }
</style>

<div class="col-lg-3 col-6">
  <a href="#/status">
    <div class="small-box bg-primary">
      <div class="inner">
        <h3>Status</h3>
        <p>Blockchain has {state.content.status.blockchain.length} blocks</p>
      </div>
      <div class="icon">
        <i class="fas fa-tachometer-alt"></i>
      </div>
    </div>
  </a>
</div>

<div class="col-lg-3 col-6">
  <a href="#/wallet">
    <div class="small-box bg-primary">
      <div class="inner">
        <h3>Wallet</h3>
        <p>Balance is {state.content.status.balance} NBC</p>
      </div>
      <div class="icon">
        <i class="fas fa-wallet"></i>
      </div>
    </div>
  </a>
</div>

<div class="col-lg-3 col-6">
  <a href="#/network">
    <div class="small-box bg-primary">
      <div class="inner">
        <h3>Network</h3>
        <p>Connected to {state.content.status.neighbors.length} neighbors</p>
      </div>
      <div class="icon">
        <i class="fas fa-network-wired"></i>
      </div>
    </div>
  </a>
</div>

<div class="col-lg-3 col-6">
  <a href="#/connect">
    <div class="small-box bg-primary">
      <div class="inner">
        <h3>Connect</h3>
        <p>Click to connect to other nodes</p>
      </div>
      <div class="icon">
        <i class="fas fa-plug"></i>
      </div>
    </div>
  </a>
</div>
