var app=function(){"use strict";function t(){}function n(t){return t()}function e(){return Object.create(null)}function o(t){t.forEach(n)}function r(t){return"function"==typeof t}function c(t,n){return t!=t?n==n:t!==n||t&&"object"==typeof t||"function"==typeof t}let u;function f(t){u=t}const a=[],l=[],s=[],i=[],d=Promise.resolve();let p=!1;function $(t){s.push(t)}let h=!1;const g=new Set;function m(){if(!h){h=!0;do{for(let t=0;t<a.length;t+=1){const n=a[t];f(n),y(n.$$)}for(a.length=0;l.length;)l.pop()();for(let t=0;t<s.length;t+=1){const n=s[t];g.has(n)||(g.add(n),n())}s.length=0}while(a.length);for(;i.length;)i.pop()();p=!1,h=!1,g.clear()}}function y(t){if(null!==t.fragment){t.update(),o(t.before_update);const n=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,n),t.after_update.forEach($)}}const _=new Set;function x(t,n){-1===t.$$.dirty[0]&&(a.push(t),p||(p=!0,d.then(m)),t.$$.dirty.fill(0)),t.$$.dirty[n/31|0]|=1<<n%31}function b(c,a,l,s,i,d,p=[-1]){const h=u;f(c);const g=a.props||{},y=c.$$={fragment:null,ctx:null,props:d,update:t,not_equal:i,bound:e(),on_mount:[],on_destroy:[],before_update:[],after_update:[],context:new Map(h?h.$$.context:[]),callbacks:e(),dirty:p};let b=!1;var w,v;y.ctx=l?l(c,g,(t,n,...e)=>{const o=e.length?e[0]:n;return y.ctx&&i(y.ctx[t],y.ctx[t]=o)&&(y.bound[t]&&y.bound[t](o),b&&x(c,t)),n}):[],y.update(),b=!0,o(y.before_update),y.fragment=!!s&&s(y.ctx),a.target&&(a.hydrate?y.fragment&&y.fragment.l(function(t){return Array.from(t.childNodes)}(a.target)):y.fragment&&y.fragment.c(),a.intro&&((w=c.$$.fragment)&&w.i&&(_.delete(w),w.i(v))),function(t,e,c){const{fragment:u,on_mount:f,on_destroy:a,after_update:l}=t.$$;u&&u.m(e,c),$(()=>{const e=f.map(n).filter(r);a?a.push(...e):o(e),t.$$.on_mount=[]}),l.forEach($)}(c,a.target,a.anchor),m()),f(h)}function w(n){let e;return{c(){e=function(t){return document.createElement(t)}("h1"),e.textContent=`Hello ${v}!`},m(t,n){!function(t,n,e){t.insertBefore(n,e||null)}(t,e,n)},p:t,i:t,o:t,d(t){var n;t&&(n=e).parentNode.removeChild(n)}}}let v="world";return new class extends class{$destroy(){!function(t,n){const e=t.$$;null!==e.fragment&&(o(e.on_destroy),e.fragment&&e.fragment.d(n),e.on_destroy=e.fragment=null,e.ctx=[])}(this,1),this.$destroy=t}$on(t,n){const e=this.$$.callbacks[t]||(this.$$.callbacks[t]=[]);return e.push(n),()=>{const t=e.indexOf(n);-1!==t&&e.splice(t,1)}}$set(){}}{constructor(t){super(),b(this,t,null,w,c,{})}}({target:document.body})}();
//# sourceMappingURL=bundle.js.map
