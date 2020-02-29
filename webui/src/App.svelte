<script>
    import Navbar  from './Navbar.svelte';
    import Sidebar from './Sidebar.svelte';
    import Page    from './Page.svelte';
    import Footer  from './Footer.svelte';
    import { get } from "./api.js";
    export let state;
    get('status').then(console.log);
</script>

<Navbar></Navbar>
<Sidebar></Sidebar>
<Page></Page>
<Footer></Footer>
