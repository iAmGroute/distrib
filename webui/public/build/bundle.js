
(function(l, r) { if (l.getElementById('livereloadscript')) return; r = l.createElement('script'); r.async = 1; r.src = '//' + (window.location.host || 'localhost').split(':')[0] + ':35729/livereload.js?snipver=1'; r.id = 'livereloadscript'; l.head.appendChild(r) })(window.document);
var app = (function () {
    'use strict';

    function noop() { }
    function add_location(element, file, line, column, char) {
        element.__svelte_meta = {
            loc: { file, line, column, char }
        };
    }
    function run(fn) {
        return fn();
    }
    function blank_object() {
        return Object.create(null);
    }
    function run_all(fns) {
        fns.forEach(run);
    }
    function is_function(thing) {
        return typeof thing === 'function';
    }
    function safe_not_equal(a, b) {
        return a != a ? b == b : a !== b || ((a && typeof a === 'object') || typeof a === 'function');
    }

    function append(target, node) {
        target.appendChild(node);
    }
    function insert(target, node, anchor) {
        target.insertBefore(node, anchor || null);
    }
    function detach(node) {
        node.parentNode.removeChild(node);
    }
    function element(name) {
        return document.createElement(name);
    }
    function text(data) {
        return document.createTextNode(data);
    }
    function space() {
        return text(' ');
    }
    function attr(node, attribute, value) {
        if (value == null)
            node.removeAttribute(attribute);
        else if (node.getAttribute(attribute) !== value)
            node.setAttribute(attribute, value);
    }
    function children(element) {
        return Array.from(element.childNodes);
    }
    function custom_event(type, detail) {
        const e = document.createEvent('CustomEvent');
        e.initCustomEvent(type, false, false, detail);
        return e;
    }

    let current_component;
    function set_current_component(component) {
        current_component = component;
    }

    const dirty_components = [];
    const binding_callbacks = [];
    const render_callbacks = [];
    const flush_callbacks = [];
    const resolved_promise = Promise.resolve();
    let update_scheduled = false;
    function schedule_update() {
        if (!update_scheduled) {
            update_scheduled = true;
            resolved_promise.then(flush);
        }
    }
    function add_render_callback(fn) {
        render_callbacks.push(fn);
    }
    let flushing = false;
    const seen_callbacks = new Set();
    function flush() {
        if (flushing)
            return;
        flushing = true;
        do {
            // first, call beforeUpdate functions
            // and update components
            for (let i = 0; i < dirty_components.length; i += 1) {
                const component = dirty_components[i];
                set_current_component(component);
                update(component.$$);
            }
            dirty_components.length = 0;
            while (binding_callbacks.length)
                binding_callbacks.pop()();
            // then, once components are updated, call
            // afterUpdate functions. This may cause
            // subsequent updates...
            for (let i = 0; i < render_callbacks.length; i += 1) {
                const callback = render_callbacks[i];
                if (!seen_callbacks.has(callback)) {
                    // ...so guard against infinite loops
                    seen_callbacks.add(callback);
                    callback();
                }
            }
            render_callbacks.length = 0;
        } while (dirty_components.length);
        while (flush_callbacks.length) {
            flush_callbacks.pop()();
        }
        update_scheduled = false;
        flushing = false;
        seen_callbacks.clear();
    }
    function update($$) {
        if ($$.fragment !== null) {
            $$.update();
            run_all($$.before_update);
            const dirty = $$.dirty;
            $$.dirty = [-1];
            $$.fragment && $$.fragment.p($$.ctx, dirty);
            $$.after_update.forEach(add_render_callback);
        }
    }
    const outroing = new Set();
    let outros;
    function transition_in(block, local) {
        if (block && block.i) {
            outroing.delete(block);
            block.i(local);
        }
    }
    function transition_out(block, local, detach, callback) {
        if (block && block.o) {
            if (outroing.has(block))
                return;
            outroing.add(block);
            outros.c.push(() => {
                outroing.delete(block);
                if (callback) {
                    if (detach)
                        block.d(1);
                    callback();
                }
            });
            block.o(local);
        }
    }
    function create_component(block) {
        block && block.c();
    }
    function mount_component(component, target, anchor) {
        const { fragment, on_mount, on_destroy, after_update } = component.$$;
        fragment && fragment.m(target, anchor);
        // onMount happens before the initial afterUpdate
        add_render_callback(() => {
            const new_on_destroy = on_mount.map(run).filter(is_function);
            if (on_destroy) {
                on_destroy.push(...new_on_destroy);
            }
            else {
                // Edge case - component was destroyed immediately,
                // most likely as a result of a binding initialising
                run_all(new_on_destroy);
            }
            component.$$.on_mount = [];
        });
        after_update.forEach(add_render_callback);
    }
    function destroy_component(component, detaching) {
        const $$ = component.$$;
        if ($$.fragment !== null) {
            run_all($$.on_destroy);
            $$.fragment && $$.fragment.d(detaching);
            // TODO null out other refs, including component.$$ (but need to
            // preserve final state?)
            $$.on_destroy = $$.fragment = null;
            $$.ctx = [];
        }
    }
    function make_dirty(component, i) {
        if (component.$$.dirty[0] === -1) {
            dirty_components.push(component);
            schedule_update();
            component.$$.dirty.fill(0);
        }
        component.$$.dirty[(i / 31) | 0] |= (1 << (i % 31));
    }
    function init(component, options, instance, create_fragment, not_equal, props, dirty = [-1]) {
        const parent_component = current_component;
        set_current_component(component);
        const prop_values = options.props || {};
        const $$ = component.$$ = {
            fragment: null,
            ctx: null,
            // state
            props,
            update: noop,
            not_equal,
            bound: blank_object(),
            // lifecycle
            on_mount: [],
            on_destroy: [],
            before_update: [],
            after_update: [],
            context: new Map(parent_component ? parent_component.$$.context : []),
            // everything else
            callbacks: blank_object(),
            dirty
        };
        let ready = false;
        $$.ctx = instance
            ? instance(component, prop_values, (i, ret, ...rest) => {
                const value = rest.length ? rest[0] : ret;
                if ($$.ctx && not_equal($$.ctx[i], $$.ctx[i] = value)) {
                    if ($$.bound[i])
                        $$.bound[i](value);
                    if (ready)
                        make_dirty(component, i);
                }
                return ret;
            })
            : [];
        $$.update();
        ready = true;
        run_all($$.before_update);
        // `false` as a special case of no DOM component
        $$.fragment = create_fragment ? create_fragment($$.ctx) : false;
        if (options.target) {
            if (options.hydrate) {
                // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
                $$.fragment && $$.fragment.l(children(options.target));
            }
            else {
                // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
                $$.fragment && $$.fragment.c();
            }
            if (options.intro)
                transition_in(component.$$.fragment);
            mount_component(component, options.target, options.anchor);
            flush();
        }
        set_current_component(parent_component);
    }
    class SvelteComponent {
        $destroy() {
            destroy_component(this, 1);
            this.$destroy = noop;
        }
        $on(type, callback) {
            const callbacks = (this.$$.callbacks[type] || (this.$$.callbacks[type] = []));
            callbacks.push(callback);
            return () => {
                const index = callbacks.indexOf(callback);
                if (index !== -1)
                    callbacks.splice(index, 1);
            };
        }
        $set() {
            // overridden by instance, if it has props
        }
    }

    function dispatch_dev(type, detail) {
        document.dispatchEvent(custom_event(type, Object.assign({ version: '3.19.1' }, detail)));
    }
    function append_dev(target, node) {
        dispatch_dev("SvelteDOMInsert", { target, node });
        append(target, node);
    }
    function insert_dev(target, node, anchor) {
        dispatch_dev("SvelteDOMInsert", { target, node, anchor });
        insert(target, node, anchor);
    }
    function detach_dev(node) {
        dispatch_dev("SvelteDOMRemove", { node });
        detach(node);
    }
    function attr_dev(node, attribute, value) {
        attr(node, attribute, value);
        if (value == null)
            dispatch_dev("SvelteDOMRemoveAttribute", { node, attribute });
        else
            dispatch_dev("SvelteDOMSetAttribute", { node, attribute, value });
    }
    class SvelteComponentDev extends SvelteComponent {
        constructor(options) {
            if (!options || (!options.target && !options.$$inline)) {
                throw new Error(`'target' is a required option`);
            }
            super();
        }
        $destroy() {
            super.$destroy();
            this.$destroy = () => {
                console.warn(`Component was already destroyed`); // eslint-disable-line no-console
            };
        }
        $capture_state() { }
        $inject_state() { }
    }

    /* src\Navbar.svelte generated by Svelte v3.19.1 */

    const file = "src\\Navbar.svelte";

    function create_fragment(ctx) {
    	let nav;
    	let ul0;
    	let li0;
    	let a0;
    	let t1;
    	let li1;
    	let a1;
    	let t3;
    	let ul1;
    	let li2;
    	let a2;
    	let i;

    	const block = {
    		c: function create() {
    			nav = element("nav");
    			ul0 = element("ul");
    			li0 = element("li");
    			a0 = element("a");
    			a0.textContent = "Home";
    			t1 = space();
    			li1 = element("li");
    			a1 = element("a");
    			a1.textContent = "Contact";
    			t3 = space();
    			ul1 = element("ul");
    			li2 = element("li");
    			a2 = element("a");
    			i = element("i");
    			attr_dev(a0, "href", "index.html");
    			attr_dev(a0, "class", "nav-link");
    			add_location(a0, file, 6, 6, 208);
    			attr_dev(li0, "class", "nav-item d-none d-sm-inline-block");
    			add_location(li0, file, 5, 4, 154);
    			attr_dev(a1, "href", "#");
    			attr_dev(a1, "class", "nav-link");
    			add_location(a1, file, 9, 6, 325);
    			attr_dev(li1, "class", "nav-item d-none d-sm-inline-block");
    			add_location(li1, file, 8, 4, 271);
    			attr_dev(ul0, "class", "navbar-nav");
    			add_location(ul0, file, 4, 2, 125);
    			attr_dev(i, "class", "fas fa-th-large");
    			add_location(i, file, 15, 97, 577);
    			attr_dev(a2, "class", "nav-link");
    			attr_dev(a2, "data-widget", "control-sidebar");
    			attr_dev(a2, "data-slide", "true");
    			attr_dev(a2, "href", "#");
    			attr_dev(a2, "role", "button");
    			add_location(a2, file, 15, 6, 486);
    			attr_dev(li2, "class", "nav-item");
    			add_location(li2, file, 14, 4, 457);
    			attr_dev(ul1, "class", "navbar-nav ml-auto");
    			add_location(ul1, file, 13, 2, 420);
    			attr_dev(nav, "class", "main-header navbar navbar-expand navbar-white navbar-light");
    			add_location(nav, file, 2, 0, 19);
    		},
    		l: function claim(nodes) {
    			throw new Error("options.hydrate only works if the component was compiled with the `hydratable: true` option");
    		},
    		m: function mount(target, anchor) {
    			insert_dev(target, nav, anchor);
    			append_dev(nav, ul0);
    			append_dev(ul0, li0);
    			append_dev(li0, a0);
    			append_dev(ul0, t1);
    			append_dev(ul0, li1);
    			append_dev(li1, a1);
    			append_dev(nav, t3);
    			append_dev(nav, ul1);
    			append_dev(ul1, li2);
    			append_dev(li2, a2);
    			append_dev(a2, i);
    		},
    		p: noop,
    		i: noop,
    		o: noop,
    		d: function destroy(detaching) {
    			if (detaching) detach_dev(nav);
    		}
    	};

    	dispatch_dev("SvelteRegisterBlock", {
    		block,
    		id: create_fragment.name,
    		type: "component",
    		source: "",
    		ctx
    	});

    	return block;
    }

    class Navbar extends SvelteComponentDev {
    	constructor(options) {
    		super(options);
    		init(this, options, null, create_fragment, safe_not_equal, {});

    		dispatch_dev("SvelteRegisterComponent", {
    			component: this,
    			tagName: "Navbar",
    			options,
    			id: create_fragment.name
    		});
    	}
    }

    /* src\Sidebar.svelte generated by Svelte v3.19.1 */

    const file$1 = "src\\Sidebar.svelte";

    function create_fragment$1(ctx) {
    	let aside;
    	let a0;
    	let img;
    	let img_src_value;
    	let t0;
    	let span0;
    	let t2;
    	let div;
    	let nav;
    	let ul;
    	let li0;
    	let a1;
    	let i0;
    	let t3;
    	let p0;
    	let t5;
    	let li1;
    	let a2;
    	let i1;
    	let t6;
    	let p1;
    	let t8;
    	let li2;
    	let a3;
    	let i2;
    	let t9;
    	let p2;
    	let t10;
    	let span1;

    	const block = {
    		c: function create() {
    			aside = element("aside");
    			a0 = element("a");
    			img = element("img");
    			t0 = space();
    			span0 = element("span");
    			span0.textContent = "Noobcash";
    			t2 = space();
    			div = element("div");
    			nav = element("nav");
    			ul = element("ul");
    			li0 = element("li");
    			a1 = element("a");
    			i0 = element("i");
    			t3 = space();
    			p0 = element("p");
    			p0.textContent = "Wallet";
    			t5 = space();
    			li1 = element("li");
    			a2 = element("a");
    			i1 = element("i");
    			t6 = space();
    			p1 = element("p");
    			p1.textContent = "Network";
    			t8 = space();
    			li2 = element("li");
    			a3 = element("a");
    			i2 = element("i");
    			t9 = space();
    			p2 = element("p");
    			t10 = text("Example\r\n              ");
    			span1 = element("span");
    			span1.textContent = "New";
    			if (img.src !== (img_src_value = "dist/img/logo.png")) attr_dev(img, "src", img_src_value);
    			attr_dev(img, "class", "brand-image");
    			add_location(img, file$1, 5, 4, 169);
    			attr_dev(span0, "class", "brand-text");
    			add_location(span0, file$1, 6, 4, 224);
    			attr_dev(a0, "href", "index.html");
    			attr_dev(a0, "class", "brand-link");
    			add_location(a0, file$1, 4, 2, 123);
    			attr_dev(i0, "class", "nav-icon fas fa-wallet");
    			add_location(i0, file$1, 14, 12, 492);
    			add_location(p0, file$1, 15, 12, 544);
    			attr_dev(a1, "href", "#");
    			attr_dev(a1, "class", "nav-link active");
    			add_location(a1, file$1, 13, 10, 442);
    			attr_dev(li0, "class", "nav-item");
    			add_location(li0, file$1, 12, 8, 409);
    			attr_dev(i1, "class", "nav-icon fas fa-network-wired");
    			add_location(i1, file$1, 20, 12, 674);
    			add_location(p1, file$1, 21, 12, 733);
    			attr_dev(a2, "href", "#");
    			attr_dev(a2, "class", "nav-link");
    			add_location(a2, file$1, 19, 10, 631);
    			attr_dev(li1, "class", "nav-item");
    			add_location(li1, file$1, 18, 8, 598);
    			attr_dev(i2, "class", "nav-icon fas fa-th");
    			add_location(i2, file$1, 26, 12, 864);
    			attr_dev(span1, "class", "right badge badge-danger");
    			add_location(span1, file$1, 29, 14, 954);
    			add_location(p2, file$1, 27, 12, 912);
    			attr_dev(a3, "href", "#");
    			attr_dev(a3, "class", "nav-link");
    			add_location(a3, file$1, 25, 10, 821);
    			attr_dev(li2, "class", "nav-item");
    			add_location(li2, file$1, 24, 8, 788);
    			attr_dev(ul, "class", "nav nav-pills nav-sidebar flex-column");
    			add_location(ul, file$1, 11, 6, 349);
    			attr_dev(nav, "class", "mt-2");
    			add_location(nav, file$1, 10, 4, 323);
    			attr_dev(div, "class", "sidebar");
    			add_location(div, file$1, 9, 2, 296);
    			attr_dev(aside, "class", "main-sidebar sidebar-dark-primary elevation-4");
    			add_location(aside, file$1, 2, 0, 35);
    		},
    		l: function claim(nodes) {
    			throw new Error("options.hydrate only works if the component was compiled with the `hydratable: true` option");
    		},
    		m: function mount(target, anchor) {
    			insert_dev(target, aside, anchor);
    			append_dev(aside, a0);
    			append_dev(a0, img);
    			append_dev(a0, t0);
    			append_dev(a0, span0);
    			append_dev(aside, t2);
    			append_dev(aside, div);
    			append_dev(div, nav);
    			append_dev(nav, ul);
    			append_dev(ul, li0);
    			append_dev(li0, a1);
    			append_dev(a1, i0);
    			append_dev(a1, t3);
    			append_dev(a1, p0);
    			append_dev(ul, t5);
    			append_dev(ul, li1);
    			append_dev(li1, a2);
    			append_dev(a2, i1);
    			append_dev(a2, t6);
    			append_dev(a2, p1);
    			append_dev(ul, t8);
    			append_dev(ul, li2);
    			append_dev(li2, a3);
    			append_dev(a3, i2);
    			append_dev(a3, t9);
    			append_dev(a3, p2);
    			append_dev(p2, t10);
    			append_dev(p2, span1);
    		},
    		p: noop,
    		i: noop,
    		o: noop,
    		d: function destroy(detaching) {
    			if (detaching) detach_dev(aside);
    		}
    	};

    	dispatch_dev("SvelteRegisterBlock", {
    		block,
    		id: create_fragment$1.name,
    		type: "component",
    		source: "",
    		ctx
    	});

    	return block;
    }

    class Sidebar extends SvelteComponentDev {
    	constructor(options) {
    		super(options);
    		init(this, options, null, create_fragment$1, safe_not_equal, {});

    		dispatch_dev("SvelteRegisterComponent", {
    			component: this,
    			tagName: "Sidebar",
    			options,
    			id: create_fragment$1.name
    		});
    	}
    }

    /* src\pages\Wallet.svelte generated by Svelte v3.19.1 */

    const file$2 = "src\\pages\\Wallet.svelte";

    function create_fragment$2(ctx) {
    	let div20;
    	let div4;
    	let div3;
    	let div2;
    	let div0;
    	let h1;
    	let t1;
    	let div1;
    	let ol;
    	let li0;
    	let a0;
    	let t3;
    	let li1;
    	let t5;
    	let div19;
    	let div18;
    	let div17;
    	let div9;
    	let div6;
    	let div5;
    	let h50;
    	let t7;
    	let p0;
    	let t9;
    	let a1;
    	let t11;
    	let a2;
    	let t13;
    	let div8;
    	let div7;
    	let h51;
    	let t15;
    	let p1;
    	let t17;
    	let a3;
    	let t19;
    	let a4;
    	let t21;
    	let div16;
    	let div12;
    	let div10;
    	let h52;
    	let t23;
    	let div11;
    	let h60;
    	let t25;
    	let p2;
    	let t27;
    	let a5;
    	let t29;
    	let div15;
    	let div13;
    	let h53;
    	let t31;
    	let div14;
    	let h61;
    	let t33;
    	let p3;
    	let t35;
    	let a6;

    	const block = {
    		c: function create() {
    			div20 = element("div");
    			div4 = element("div");
    			div3 = element("div");
    			div2 = element("div");
    			div0 = element("div");
    			h1 = element("h1");
    			h1.textContent = "Starter Page";
    			t1 = space();
    			div1 = element("div");
    			ol = element("ol");
    			li0 = element("li");
    			a0 = element("a");
    			a0.textContent = "Home";
    			t3 = space();
    			li1 = element("li");
    			li1.textContent = "Starter Page";
    			t5 = space();
    			div19 = element("div");
    			div18 = element("div");
    			div17 = element("div");
    			div9 = element("div");
    			div6 = element("div");
    			div5 = element("div");
    			h50 = element("h5");
    			h50.textContent = "Card title";
    			t7 = space();
    			p0 = element("p");
    			p0.textContent = "Some quick example text to build on the card title and make up the bulk of the card's\r\n                content.";
    			t9 = space();
    			a1 = element("a");
    			a1.textContent = "Card link";
    			t11 = space();
    			a2 = element("a");
    			a2.textContent = "Another link";
    			t13 = space();
    			div8 = element("div");
    			div7 = element("div");
    			h51 = element("h5");
    			h51.textContent = "Card title";
    			t15 = space();
    			p1 = element("p");
    			p1.textContent = "Some quick example text to build on the card title and make up the bulk of the card's\r\n                content.";
    			t17 = space();
    			a3 = element("a");
    			a3.textContent = "Card link";
    			t19 = space();
    			a4 = element("a");
    			a4.textContent = "Another link";
    			t21 = space();
    			div16 = element("div");
    			div12 = element("div");
    			div10 = element("div");
    			h52 = element("h5");
    			h52.textContent = "Featured";
    			t23 = space();
    			div11 = element("div");
    			h60 = element("h6");
    			h60.textContent = "Special title treatment";
    			t25 = space();
    			p2 = element("p");
    			p2.textContent = "With supporting text below as a natural lead-in to additional content.";
    			t27 = space();
    			a5 = element("a");
    			a5.textContent = "Go somewhere";
    			t29 = space();
    			div15 = element("div");
    			div13 = element("div");
    			h53 = element("h5");
    			h53.textContent = "Featured";
    			t31 = space();
    			div14 = element("div");
    			h61 = element("h6");
    			h61.textContent = "Special title treatment";
    			t33 = space();
    			p3 = element("p");
    			p3.textContent = "With supporting text below as a natural lead-in to additional content.";
    			t35 = space();
    			a6 = element("a");
    			a6.textContent = "Go somewhere";
    			attr_dev(h1, "class", "m-0 text-dark");
    			add_location(h1, file$2, 7, 10, 260);
    			attr_dev(div0, "class", "col-sm-6");
    			add_location(div0, file$2, 6, 8, 226);
    			attr_dev(a0, "href", "#");
    			add_location(a0, file$2, 11, 40, 443);
    			attr_dev(li0, "class", "breadcrumb-item");
    			add_location(li0, file$2, 11, 12, 415);
    			attr_dev(li1, "class", "breadcrumb-item active");
    			add_location(li1, file$2, 12, 12, 482);
    			attr_dev(ol, "class", "breadcrumb float-sm-right");
    			add_location(ol, file$2, 10, 10, 363);
    			attr_dev(div1, "class", "col-sm-6");
    			add_location(div1, file$2, 9, 8, 329);
    			attr_dev(div2, "class", "row mb-2");
    			add_location(div2, file$2, 5, 6, 194);
    			attr_dev(div3, "class", "container-fluid");
    			add_location(div3, file$2, 4, 4, 157);
    			attr_dev(div4, "class", "content-header");
    			add_location(div4, file$2, 3, 2, 123);
    			attr_dev(h50, "class", "card-title");
    			add_location(h50, file$2, 25, 14, 828);
    			attr_dev(p0, "class", "card-text");
    			add_location(p0, file$2, 26, 14, 882);
    			attr_dev(a1, "href", "#");
    			attr_dev(a1, "class", "card-link");
    			add_location(a1, file$2, 30, 14, 1068);
    			attr_dev(a2, "href", "#");
    			attr_dev(a2, "class", "card-link");
    			add_location(a2, file$2, 31, 14, 1127);
    			attr_dev(div5, "class", "card-body");
    			add_location(div5, file$2, 24, 12, 789);
    			attr_dev(div6, "class", "card");
    			add_location(div6, file$2, 23, 10, 757);
    			attr_dev(h51, "class", "card-title");
    			add_location(h51, file$2, 36, 14, 1320);
    			attr_dev(p1, "class", "card-text");
    			add_location(p1, file$2, 37, 14, 1374);
    			attr_dev(a3, "href", "#");
    			attr_dev(a3, "class", "card-link");
    			add_location(a3, file$2, 41, 14, 1560);
    			attr_dev(a4, "href", "#");
    			attr_dev(a4, "class", "card-link");
    			add_location(a4, file$2, 42, 14, 1619);
    			attr_dev(div7, "class", "card-body");
    			add_location(div7, file$2, 35, 12, 1281);
    			attr_dev(div8, "class", "card card-primary card-outline");
    			add_location(div8, file$2, 34, 10, 1223);
    			attr_dev(div9, "class", "col-lg-6");
    			add_location(div9, file$2, 22, 8, 723);
    			attr_dev(h52, "class", "m-0");
    			add_location(h52, file$2, 49, 14, 1836);
    			attr_dev(div10, "class", "card-header");
    			add_location(div10, file$2, 48, 12, 1795);
    			attr_dev(h60, "class", "card-title");
    			add_location(h60, file$2, 52, 14, 1938);
    			attr_dev(p2, "class", "card-text");
    			add_location(p2, file$2, 53, 14, 2005);
    			attr_dev(a5, "href", "#");
    			attr_dev(a5, "class", "btn btn-primary");
    			add_location(a5, file$2, 54, 14, 2116);
    			attr_dev(div11, "class", "card-body");
    			add_location(div11, file$2, 51, 12, 1899);
    			attr_dev(div12, "class", "card");
    			add_location(div12, file$2, 47, 10, 1763);
    			attr_dev(h53, "class", "m-0");
    			add_location(h53, file$2, 59, 14, 2317);
    			attr_dev(div13, "class", "card-header");
    			add_location(div13, file$2, 58, 12, 2276);
    			attr_dev(h61, "class", "card-title");
    			add_location(h61, file$2, 62, 14, 2419);
    			attr_dev(p3, "class", "card-text");
    			add_location(p3, file$2, 63, 14, 2486);
    			attr_dev(a6, "href", "#");
    			attr_dev(a6, "class", "btn btn-primary");
    			add_location(a6, file$2, 64, 14, 2597);
    			attr_dev(div14, "class", "card-body");
    			add_location(div14, file$2, 61, 12, 2380);
    			attr_dev(div15, "class", "card card-primary card-outline");
    			add_location(div15, file$2, 57, 10, 2218);
    			attr_dev(div16, "class", "col-lg-6");
    			add_location(div16, file$2, 46, 8, 1729);
    			attr_dev(div17, "class", "row");
    			add_location(div17, file$2, 21, 6, 696);
    			attr_dev(div18, "class", "container-fluid");
    			add_location(div18, file$2, 20, 4, 659);
    			attr_dev(div19, "class", "content");
    			add_location(div19, file$2, 19, 2, 632);
    			attr_dev(div20, "class", "content-wrapper");
    			add_location(div20, file$2, 1, 0, 49);
    		},
    		l: function claim(nodes) {
    			throw new Error("options.hydrate only works if the component was compiled with the `hydratable: true` option");
    		},
    		m: function mount(target, anchor) {
    			insert_dev(target, div20, anchor);
    			append_dev(div20, div4);
    			append_dev(div4, div3);
    			append_dev(div3, div2);
    			append_dev(div2, div0);
    			append_dev(div0, h1);
    			append_dev(div2, t1);
    			append_dev(div2, div1);
    			append_dev(div1, ol);
    			append_dev(ol, li0);
    			append_dev(li0, a0);
    			append_dev(ol, t3);
    			append_dev(ol, li1);
    			append_dev(div20, t5);
    			append_dev(div20, div19);
    			append_dev(div19, div18);
    			append_dev(div18, div17);
    			append_dev(div17, div9);
    			append_dev(div9, div6);
    			append_dev(div6, div5);
    			append_dev(div5, h50);
    			append_dev(div5, t7);
    			append_dev(div5, p0);
    			append_dev(div5, t9);
    			append_dev(div5, a1);
    			append_dev(div5, t11);
    			append_dev(div5, a2);
    			append_dev(div9, t13);
    			append_dev(div9, div8);
    			append_dev(div8, div7);
    			append_dev(div7, h51);
    			append_dev(div7, t15);
    			append_dev(div7, p1);
    			append_dev(div7, t17);
    			append_dev(div7, a3);
    			append_dev(div7, t19);
    			append_dev(div7, a4);
    			append_dev(div17, t21);
    			append_dev(div17, div16);
    			append_dev(div16, div12);
    			append_dev(div12, div10);
    			append_dev(div10, h52);
    			append_dev(div12, t23);
    			append_dev(div12, div11);
    			append_dev(div11, h60);
    			append_dev(div11, t25);
    			append_dev(div11, p2);
    			append_dev(div11, t27);
    			append_dev(div11, a5);
    			append_dev(div16, t29);
    			append_dev(div16, div15);
    			append_dev(div15, div13);
    			append_dev(div13, h53);
    			append_dev(div15, t31);
    			append_dev(div15, div14);
    			append_dev(div14, h61);
    			append_dev(div14, t33);
    			append_dev(div14, p3);
    			append_dev(div14, t35);
    			append_dev(div14, a6);
    		},
    		p: noop,
    		i: noop,
    		o: noop,
    		d: function destroy(detaching) {
    			if (detaching) detach_dev(div20);
    		}
    	};

    	dispatch_dev("SvelteRegisterBlock", {
    		block,
    		id: create_fragment$2.name,
    		type: "component",
    		source: "",
    		ctx
    	});

    	return block;
    }

    class Wallet extends SvelteComponentDev {
    	constructor(options) {
    		super(options);
    		init(this, options, null, create_fragment$2, safe_not_equal, {});

    		dispatch_dev("SvelteRegisterComponent", {
    			component: this,
    			tagName: "Wallet",
    			options,
    			id: create_fragment$2.name
    		});
    	}
    }

    /* src\Page.svelte generated by Svelte v3.19.1 */

    function create_fragment$3(ctx) {
    	let current;
    	const wallet = new Wallet({ $$inline: true });

    	const block = {
    		c: function create() {
    			create_component(wallet.$$.fragment);
    		},
    		l: function claim(nodes) {
    			throw new Error("options.hydrate only works if the component was compiled with the `hydratable: true` option");
    		},
    		m: function mount(target, anchor) {
    			mount_component(wallet, target, anchor);
    			current = true;
    		},
    		p: noop,
    		i: function intro(local) {
    			if (current) return;
    			transition_in(wallet.$$.fragment, local);
    			current = true;
    		},
    		o: function outro(local) {
    			transition_out(wallet.$$.fragment, local);
    			current = false;
    		},
    		d: function destroy(detaching) {
    			destroy_component(wallet, detaching);
    		}
    	};

    	dispatch_dev("SvelteRegisterBlock", {
    		block,
    		id: create_fragment$3.name,
    		type: "component",
    		source: "",
    		ctx
    	});

    	return block;
    }

    function instance($$self, $$props, $$invalidate) {
    	$$self.$capture_state = () => ({ Wallet });
    	return [];
    }

    class Page extends SvelteComponentDev {
    	constructor(options) {
    		super(options);
    		init(this, options, instance, create_fragment$3, safe_not_equal, {});

    		dispatch_dev("SvelteRegisterComponent", {
    			component: this,
    			tagName: "Page",
    			options,
    			id: create_fragment$3.name
    		});
    	}
    }

    /* src\Footer.svelte generated by Svelte v3.19.1 */

    const file$3 = "src\\Footer.svelte";

    function create_fragment$4(ctx) {
    	let footer;
    	let div;
    	let t1;
    	let strong;
    	let t3;
    	let a;

    	const block = {
    		c: function create() {
    			footer = element("footer");
    			div = element("div");
    			div.textContent = `${/*isLive*/ ctx[0] ? "Live" : "Offline"}`;
    			t1 = space();
    			strong = element("strong");
    			strong.textContent = "Noobcash Web UI";
    			t3 = text(", based on ");
    			a = element("a");
    			a.textContent = "AdminLTE.io";
    			attr_dev(div, "class", "float-right d-none d-sm-inline");
    			add_location(div, file$3, 7, 2, 124);
    			add_location(strong, file$3, 9, 2, 239);
    			attr_dev(a, "href", "https://github.com/ColorlibHQ/AdminLTE");
    			attr_dev(a, "target", "_blank");
    			add_location(a, file$3, 9, 45, 282);
    			attr_dev(footer, "class", "main-footer");
    			add_location(footer, file$3, 5, 0, 67);
    		},
    		l: function claim(nodes) {
    			throw new Error("options.hydrate only works if the component was compiled with the `hydratable: true` option");
    		},
    		m: function mount(target, anchor) {
    			insert_dev(target, footer, anchor);
    			append_dev(footer, div);
    			append_dev(footer, t1);
    			append_dev(footer, strong);
    			append_dev(footer, t3);
    			append_dev(footer, a);
    		},
    		p: noop,
    		i: noop,
    		o: noop,
    		d: function destroy(detaching) {
    			if (detaching) detach_dev(footer);
    		}
    	};

    	dispatch_dev("SvelteRegisterBlock", {
    		block,
    		id: create_fragment$4.name,
    		type: "component",
    		source: "",
    		ctx
    	});

    	return block;
    }

    function instance$1($$self, $$props, $$invalidate) {
    	let isLive = true;
    	$$self.$capture_state = () => ({ isLive });

    	$$self.$inject_state = $$props => {
    		if ("isLive" in $$props) $$invalidate(0, isLive = $$props.isLive);
    	};

    	if ($$props && "$$inject" in $$props) {
    		$$self.$inject_state($$props.$$inject);
    	}

    	return [isLive];
    }

    class Footer extends SvelteComponentDev {
    	constructor(options) {
    		super(options);
    		init(this, options, instance$1, create_fragment$4, safe_not_equal, {});

    		dispatch_dev("SvelteRegisterComponent", {
    			component: this,
    			tagName: "Footer",
    			options,
    			id: create_fragment$4.name
    		});
    	}
    }

    /* src\App.svelte generated by Svelte v3.19.1 */

    function create_fragment$5(ctx) {
    	let t0;
    	let t1;
    	let t2;
    	let current;
    	const navbar = new Navbar({ $$inline: true });
    	const sidebar = new Sidebar({ $$inline: true });
    	const page = new Page({ $$inline: true });
    	const footer = new Footer({ $$inline: true });

    	const block = {
    		c: function create() {
    			create_component(navbar.$$.fragment);
    			t0 = space();
    			create_component(sidebar.$$.fragment);
    			t1 = space();
    			create_component(page.$$.fragment);
    			t2 = space();
    			create_component(footer.$$.fragment);
    		},
    		l: function claim(nodes) {
    			throw new Error("options.hydrate only works if the component was compiled with the `hydratable: true` option");
    		},
    		m: function mount(target, anchor) {
    			mount_component(navbar, target, anchor);
    			insert_dev(target, t0, anchor);
    			mount_component(sidebar, target, anchor);
    			insert_dev(target, t1, anchor);
    			mount_component(page, target, anchor);
    			insert_dev(target, t2, anchor);
    			mount_component(footer, target, anchor);
    			current = true;
    		},
    		p: noop,
    		i: function intro(local) {
    			if (current) return;
    			transition_in(navbar.$$.fragment, local);
    			transition_in(sidebar.$$.fragment, local);
    			transition_in(page.$$.fragment, local);
    			transition_in(footer.$$.fragment, local);
    			current = true;
    		},
    		o: function outro(local) {
    			transition_out(navbar.$$.fragment, local);
    			transition_out(sidebar.$$.fragment, local);
    			transition_out(page.$$.fragment, local);
    			transition_out(footer.$$.fragment, local);
    			current = false;
    		},
    		d: function destroy(detaching) {
    			destroy_component(navbar, detaching);
    			if (detaching) detach_dev(t0);
    			destroy_component(sidebar, detaching);
    			if (detaching) detach_dev(t1);
    			destroy_component(page, detaching);
    			if (detaching) detach_dev(t2);
    			destroy_component(footer, detaching);
    		}
    	};

    	dispatch_dev("SvelteRegisterBlock", {
    		block,
    		id: create_fragment$5.name,
    		type: "component",
    		source: "",
    		ctx
    	});

    	return block;
    }

    function instance$2($$self, $$props, $$invalidate) {
    	$$self.$capture_state = () => ({ Navbar, Sidebar, Page, Footer });
    	return [];
    }

    class App extends SvelteComponentDev {
    	constructor(options) {
    		super(options);
    		init(this, options, instance$2, create_fragment$5, safe_not_equal, {});

    		dispatch_dev("SvelteRegisterComponent", {
    			component: this,
    			tagName: "App",
    			options,
    			id: create_fragment$5.name
    		});
    	}
    }

    var app = new App({
    	target: document.body
    });

    return app;

}());
//# sourceMappingURL=bundle.js.map
