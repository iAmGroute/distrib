import App          from './App.svelte';
import initialState from './initialState.js';

var app = new App({
	target: document.body,
    props: {
        state: initialState
    }
});

export default app;
