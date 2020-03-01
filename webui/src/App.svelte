<script>
    import Sync    from "./Sync.js";
    import Navbar  from './Navbar.svelte';
    import Sidebar from './Sidebar.svelte';
    import Page    from './Page.svelte';
    import Footer  from './Footer.svelte';

    export let state;

    const sync = new Sync(data => {state.content.status = data});
</script>

<Navbar  state={state}/>
<Sidebar state={state}/>
<Page    state={state}/>
<Footer  state={state}/>
