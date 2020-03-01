<script>
  export let state;
</script>

<div class="col-lg-6">
  <div class="card card-primary card-outline">
    <div class="card-body">
      <h5 class="card-title">Status</h5>
      <p class="card-text">
        {JSON.stringify(state.content.status)}
      </p>
    </div>
  </div>
</div>
