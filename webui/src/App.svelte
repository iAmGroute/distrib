<script>
    import Sync    from './Sync.js';
    import Navbar  from './Navbar.svelte';
    import Sidebar from './Sidebar.svelte';
    import Page    from './Page.svelte';
    import Footer  from './Footer.svelte';

    export let state;

    const sync = new Sync(data => {
        state.isLive = true;
        state.content.status = data;
    },
    error => {
        state.isLive = false;
    });
</script>

<Navbar  {state}/>
<Sidebar {state}/>
<Page    {state}/>
<Footer  {state}/>
