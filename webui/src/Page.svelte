<script>
  import {location, replace} from 'svelte-spa-router';
  import Status  from './pages/Status.svelte';
  import Wallet  from './pages/Wallet.svelte';
  import Connect from './pages/Connect.svelte';

  export let state;

  const pages = {
    '/':        [null, null],
    '/status':  [Status,  'Status'],
    '/wallet':  [Wallet,  'Wallet'],
    '/connect': [Connect, 'Connect']
  };

  let [pageComponent, pageTitle] = pages['/status'];

  function setPage(page) {
    [pageComponent, pageTitle] = page;
    document.title = 'Noobcash' + (pageTitle ? ' ' + pageTitle : '');
  }

  location.subscribe(v => {
    console.log(v);
    for (const expr in pages) if (expr === v) return setPage(pages[expr]);
    replace('/');
  });
</script>

<!-- Content Wrapper. Contains page content -->
<div class="content-wrapper">
  <!-- Content Header (Page header) -->
  <div class="content-header">
    <div class="container-fluid">
      <div class="row mb-2">
        <div class="col-sm-6">
          <h1 class="m-0 text-dark">{pageTitle || 'Home'}</h1>
        </div>
        <div class="col-sm-6">
          <ol class="breadcrumb float-sm-right">
            {#if pageTitle}
              <li class="breadcrumb-item"><a href="#/">Home</a></li>
              <li class="breadcrumb-item active">{pageTitle}</li>
            {:else}
              <li class="breadcrumb-item active">Home</li>
            {/if}
          </ol>
        </div>
      </div>
    </div>
  </div>
  <!-- Main content -->
  <div class="content">
    <div class="container-fluid row">
      <!-- {#if      $location == "/"}       <Status {state}/> -->
      <!-- {:else if $location == "/wallet"} <Wallet {state}/> -->
      <!-- {/if} -->
      <svelte:component this={pageComponent} {state}/>
    </div>
  </div>
</div>
