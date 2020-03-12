var app=function(){"use strict";function t(){}function e(t){return t()}function n(){return Object.create(null)}function r(t){t.forEach(e)}function s(t){return"function"==typeof t}function a(t,e){return t!=t?e==e:t!==e||t&&"object"==typeof t||"function"==typeof t}function o(e){return e&&s(e.destroy)?e.destroy:t}function i(t,e){t.appendChild(e)}function c(t,e,n){t.insertBefore(e,n||null)}function l(t){t.parentNode.removeChild(t)}function u(t,e){for(let n=0;n<t.length;n+=1)t[n]&&t[n].d(e)}function f(t){return document.createElement(t)}function d(t){return document.createTextNode(t)}function h(){return d(" ")}function p(t,e,n,r){return t.addEventListener(e,n,r),()=>t.removeEventListener(e,n,r)}function m(t,e,n){null==n?t.removeAttribute(e):t.getAttribute(e)!==n&&t.setAttribute(e,n)}function g(t,e){e=""+e,t.data!==e&&(t.data=e)}function v(t,e){(null!=e||t.value)&&(t.value=e)}let b;function y(t){b=t}const w=[],x=[],$=[],E=[],L=Promise.resolve();let C=!1;function k(t){$.push(t)}let N=!1;const T=new Set;function A(){if(!N){N=!0;do{for(let t=0;t<w.length;t+=1){const e=w[t];y(e),S(e.$$)}for(w.length=0;x.length;)x.pop()();for(let t=0;t<$.length;t+=1){const e=$[t];T.has(e)||(T.add(e),e())}$.length=0}while(w.length);for(;E.length;)E.pop()();C=!1,N=!1,T.clear()}}function S(t){if(null!==t.fragment){t.update(),r(t.before_update);const e=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,e),t.after_update.forEach(k)}}const O=new Set;let R;function H(t,e){t&&t.i&&(O.delete(t),t.i(e))}function j(t,e,n,r){if(t&&t.o){if(O.has(t))return;O.add(t),R.c.push(()=>{O.delete(t),r&&(n&&t.d(1),r())}),t.o(e)}}function B(t){t&&t.c()}function M(t,n,a){const{fragment:o,on_mount:i,on_destroy:c,after_update:l}=t.$$;o&&o.m(n,a),k(()=>{const n=i.map(e).filter(s);c?c.push(...n):r(n),t.$$.on_mount=[]}),l.forEach(k)}function _(t,e){const n=t.$$;null!==n.fragment&&(r(n.on_destroy),n.fragment&&n.fragment.d(e),n.on_destroy=n.fragment=null,n.ctx=[])}function U(t,e){-1===t.$$.dirty[0]&&(w.push(t),C||(C=!0,L.then(A)),t.$$.dirty.fill(0)),t.$$.dirty[e/31|0]|=1<<e%31}function q(e,s,a,o,i,c,l=[-1]){const u=b;y(e);const f=s.props||{},d=e.$$={fragment:null,ctx:null,props:c,update:t,not_equal:i,bound:n(),on_mount:[],on_destroy:[],before_update:[],after_update:[],context:new Map(u?u.$$.context:[]),callbacks:n(),dirty:l};let h=!1;d.ctx=a?a(e,f,(t,n,...r)=>{const s=r.length?r[0]:n;return d.ctx&&i(d.ctx[t],d.ctx[t]=s)&&(d.bound[t]&&d.bound[t](s),h&&U(e,t)),n}):[],d.update(),h=!0,r(d.before_update),d.fragment=!!o&&o(d.ctx),s.target&&(s.hydrate?d.fragment&&d.fragment.l(function(t){return Array.from(t.childNodes)}(s.target)):d.fragment&&d.fragment.c(),s.intro&&H(e.$$.fragment),M(e,s.target,s.anchor),A()),y(u)}class D{$destroy(){_(this,1),this.$destroy=t}$on(t,e){const n=this.$$.callbacks[t]||(this.$$.callbacks[t]=[]);return n.push(e),()=>{const t=n.indexOf(e);-1!==t&&n.splice(t,1)}}$set(){}}var P=function(t,e){return function(){for(var n=new Array(arguments.length),r=0;r<n.length;r++)n[r]=arguments[r];return t.apply(e,n)}},I=Object.prototype.toString;function F(t){return"[object Array]"===I.call(t)}function z(t){return void 0===t}function V(t){return null!==t&&"object"==typeof t}function W(t){return"[object Function]"===I.call(t)}function X(t,e){if(null!=t)if("object"!=typeof t&&(t=[t]),F(t))for(var n=0,r=t.length;n<r;n++)e.call(null,t[n],n,t);else for(var s in t)Object.prototype.hasOwnProperty.call(t,s)&&e.call(null,t[s],s,t)}var J={isArray:F,isArrayBuffer:function(t){return"[object ArrayBuffer]"===I.call(t)},isBuffer:function(t){return null!==t&&!z(t)&&null!==t.constructor&&!z(t.constructor)&&"function"==typeof t.constructor.isBuffer&&t.constructor.isBuffer(t)},isFormData:function(t){return"undefined"!=typeof FormData&&t instanceof FormData},isArrayBufferView:function(t){return"undefined"!=typeof ArrayBuffer&&ArrayBuffer.isView?ArrayBuffer.isView(t):t&&t.buffer&&t.buffer instanceof ArrayBuffer},isString:function(t){return"string"==typeof t},isNumber:function(t){return"number"==typeof t},isObject:V,isUndefined:z,isDate:function(t){return"[object Date]"===I.call(t)},isFile:function(t){return"[object File]"===I.call(t)},isBlob:function(t){return"[object Blob]"===I.call(t)},isFunction:W,isStream:function(t){return V(t)&&W(t.pipe)},isURLSearchParams:function(t){return"undefined"!=typeof URLSearchParams&&t instanceof URLSearchParams},isStandardBrowserEnv:function(){return("undefined"==typeof navigator||"ReactNative"!==navigator.product&&"NativeScript"!==navigator.product&&"NS"!==navigator.product)&&("undefined"!=typeof window&&"undefined"!=typeof document)},forEach:X,merge:function t(){var e={};function n(n,r){"object"==typeof e[r]&&"object"==typeof n?e[r]=t(e[r],n):e[r]=n}for(var r=0,s=arguments.length;r<s;r++)X(arguments[r],n);return e},deepMerge:function t(){var e={};function n(n,r){"object"==typeof e[r]&&"object"==typeof n?e[r]=t(e[r],n):e[r]="object"==typeof n?t({},n):n}for(var r=0,s=arguments.length;r<s;r++)X(arguments[r],n);return e},extend:function(t,e,n){return X(e,(function(e,r){t[r]=n&&"function"==typeof e?P(e,n):e})),t},trim:function(t){return t.replace(/^\s*/,"").replace(/\s*$/,"")}};function K(t){return encodeURIComponent(t).replace(/%40/gi,"@").replace(/%3A/gi,":").replace(/%24/g,"$").replace(/%2C/gi,",").replace(/%20/g,"+").replace(/%5B/gi,"[").replace(/%5D/gi,"]")}var G=function(t,e,n){if(!e)return t;var r;if(n)r=n(e);else if(J.isURLSearchParams(e))r=e.toString();else{var s=[];J.forEach(e,(function(t,e){null!=t&&(J.isArray(t)?e+="[]":t=[t],J.forEach(t,(function(t){J.isDate(t)?t=t.toISOString():J.isObject(t)&&(t=JSON.stringify(t)),s.push(K(e)+"="+K(t))})))})),r=s.join("&")}if(r){var a=t.indexOf("#");-1!==a&&(t=t.slice(0,a)),t+=(-1===t.indexOf("?")?"?":"&")+r}return t};function Q(){this.handlers=[]}Q.prototype.use=function(t,e){return this.handlers.push({fulfilled:t,rejected:e}),this.handlers.length-1},Q.prototype.eject=function(t){this.handlers[t]&&(this.handlers[t]=null)},Q.prototype.forEach=function(t){J.forEach(this.handlers,(function(e){null!==e&&t(e)}))};var Y=Q,Z=function(t,e,n){return J.forEach(n,(function(n){t=n(t,e)})),t},tt=function(t){return!(!t||!t.__CANCEL__)},et=function(t,e){J.forEach(t,(function(n,r){r!==e&&r.toUpperCase()===e.toUpperCase()&&(t[e]=n,delete t[r])}))},nt=function(t,e,n,r,s){return function(t,e,n,r,s){return t.config=e,n&&(t.code=n),t.request=r,t.response=s,t.isAxiosError=!0,t.toJSON=function(){return{message:this.message,name:this.name,description:this.description,number:this.number,fileName:this.fileName,lineNumber:this.lineNumber,columnNumber:this.columnNumber,stack:this.stack,config:this.config,code:this.code}},t}(new Error(t),e,n,r,s)},rt=["age","authorization","content-length","content-type","etag","expires","from","host","if-modified-since","if-unmodified-since","last-modified","location","max-forwards","proxy-authorization","referer","retry-after","user-agent"],st=J.isStandardBrowserEnv()?function(){var t,e=/(msie|trident)/i.test(navigator.userAgent),n=document.createElement("a");function r(t){var r=t;return e&&(n.setAttribute("href",r),r=n.href),n.setAttribute("href",r),{href:n.href,protocol:n.protocol?n.protocol.replace(/:$/,""):"",host:n.host,search:n.search?n.search.replace(/^\?/,""):"",hash:n.hash?n.hash.replace(/^#/,""):"",hostname:n.hostname,port:n.port,pathname:"/"===n.pathname.charAt(0)?n.pathname:"/"+n.pathname}}return t=r(window.location.href),function(e){var n=J.isString(e)?r(e):e;return n.protocol===t.protocol&&n.host===t.host}}():function(){return!0},at=J.isStandardBrowserEnv()?{write:function(t,e,n,r,s,a){var o=[];o.push(t+"="+encodeURIComponent(e)),J.isNumber(n)&&o.push("expires="+new Date(n).toGMTString()),J.isString(r)&&o.push("path="+r),J.isString(s)&&o.push("domain="+s),!0===a&&o.push("secure"),document.cookie=o.join("; ")},read:function(t){var e=document.cookie.match(new RegExp("(^|;\\s*)("+t+")=([^;]*)"));return e?decodeURIComponent(e[3]):null},remove:function(t){this.write(t,"",Date.now()-864e5)}}:{write:function(){},read:function(){return null},remove:function(){}},ot=function(t){return new Promise((function(e,n){var r=t.data,s=t.headers;J.isFormData(r)&&delete s["Content-Type"];var a=new XMLHttpRequest;if(t.auth){var o=t.auth.username||"",i=t.auth.password||"";s.Authorization="Basic "+btoa(o+":"+i)}var c,l,u=(c=t.baseURL,l=t.url,c&&!/^([a-z][a-z\d\+\-\.]*:)?\/\//i.test(l)?function(t,e){return e?t.replace(/\/+$/,"")+"/"+e.replace(/^\/+/,""):t}(c,l):l);if(a.open(t.method.toUpperCase(),G(u,t.params,t.paramsSerializer),!0),a.timeout=t.timeout,a.onreadystatechange=function(){if(a&&4===a.readyState&&(0!==a.status||a.responseURL&&0===a.responseURL.indexOf("file:"))){var r,s,o,i,c,l="getAllResponseHeaders"in a?(r=a.getAllResponseHeaders(),c={},r?(J.forEach(r.split("\n"),(function(t){if(i=t.indexOf(":"),s=J.trim(t.substr(0,i)).toLowerCase(),o=J.trim(t.substr(i+1)),s){if(c[s]&&rt.indexOf(s)>=0)return;c[s]="set-cookie"===s?(c[s]?c[s]:[]).concat([o]):c[s]?c[s]+", "+o:o}})),c):c):null,u={data:t.responseType&&"text"!==t.responseType?a.response:a.responseText,status:a.status,statusText:a.statusText,headers:l,config:t,request:a};!function(t,e,n){var r=n.config.validateStatus;!r||r(n.status)?t(n):e(nt("Request failed with status code "+n.status,n.config,null,n.request,n))}(e,n,u),a=null}},a.onabort=function(){a&&(n(nt("Request aborted",t,"ECONNABORTED",a)),a=null)},a.onerror=function(){n(nt("Network Error",t,null,a)),a=null},a.ontimeout=function(){var e="timeout of "+t.timeout+"ms exceeded";t.timeoutErrorMessage&&(e=t.timeoutErrorMessage),n(nt(e,t,"ECONNABORTED",a)),a=null},J.isStandardBrowserEnv()){var f=at,d=(t.withCredentials||st(u))&&t.xsrfCookieName?f.read(t.xsrfCookieName):void 0;d&&(s[t.xsrfHeaderName]=d)}if("setRequestHeader"in a&&J.forEach(s,(function(t,e){void 0===r&&"content-type"===e.toLowerCase()?delete s[e]:a.setRequestHeader(e,t)})),J.isUndefined(t.withCredentials)||(a.withCredentials=!!t.withCredentials),t.responseType)try{a.responseType=t.responseType}catch(e){if("json"!==t.responseType)throw e}"function"==typeof t.onDownloadProgress&&a.addEventListener("progress",t.onDownloadProgress),"function"==typeof t.onUploadProgress&&a.upload&&a.upload.addEventListener("progress",t.onUploadProgress),t.cancelToken&&t.cancelToken.promise.then((function(t){a&&(a.abort(),n(t),a=null)})),void 0===r&&(r=null),a.send(r)}))},it={"Content-Type":"application/x-www-form-urlencoded"};function ct(t,e){!J.isUndefined(t)&&J.isUndefined(t["Content-Type"])&&(t["Content-Type"]=e)}var lt,ut={adapter:(("undefined"!=typeof XMLHttpRequest||"undefined"!=typeof process&&"[object process]"===Object.prototype.toString.call(process))&&(lt=ot),lt),transformRequest:[function(t,e){return et(e,"Accept"),et(e,"Content-Type"),J.isFormData(t)||J.isArrayBuffer(t)||J.isBuffer(t)||J.isStream(t)||J.isFile(t)||J.isBlob(t)?t:J.isArrayBufferView(t)?t.buffer:J.isURLSearchParams(t)?(ct(e,"application/x-www-form-urlencoded;charset=utf-8"),t.toString()):J.isObject(t)?(ct(e,"application/json;charset=utf-8"),JSON.stringify(t)):t}],transformResponse:[function(t){if("string"==typeof t)try{t=JSON.parse(t)}catch(t){}return t}],timeout:0,xsrfCookieName:"XSRF-TOKEN",xsrfHeaderName:"X-XSRF-TOKEN",maxContentLength:-1,validateStatus:function(t){return t>=200&&t<300}};ut.headers={common:{Accept:"application/json, text/plain, */*"}},J.forEach(["delete","get","head"],(function(t){ut.headers[t]={}})),J.forEach(["post","put","patch"],(function(t){ut.headers[t]=J.merge(it)}));var ft=ut;function dt(t){t.cancelToken&&t.cancelToken.throwIfRequested()}var ht=function(t){return dt(t),t.headers=t.headers||{},t.data=Z(t.data,t.headers,t.transformRequest),t.headers=J.merge(t.headers.common||{},t.headers[t.method]||{},t.headers),J.forEach(["delete","get","head","post","put","patch","common"],(function(e){delete t.headers[e]})),(t.adapter||ft.adapter)(t).then((function(e){return dt(t),e.data=Z(e.data,e.headers,t.transformResponse),e}),(function(e){return tt(e)||(dt(t),e&&e.response&&(e.response.data=Z(e.response.data,e.response.headers,t.transformResponse))),Promise.reject(e)}))},pt=function(t,e){e=e||{};var n={},r=["url","method","params","data"],s=["headers","auth","proxy"],a=["baseURL","url","transformRequest","transformResponse","paramsSerializer","timeout","withCredentials","adapter","responseType","xsrfCookieName","xsrfHeaderName","onUploadProgress","onDownloadProgress","maxContentLength","validateStatus","maxRedirects","httpAgent","httpsAgent","cancelToken","socketPath"];J.forEach(r,(function(t){void 0!==e[t]&&(n[t]=e[t])})),J.forEach(s,(function(r){J.isObject(e[r])?n[r]=J.deepMerge(t[r],e[r]):void 0!==e[r]?n[r]=e[r]:J.isObject(t[r])?n[r]=J.deepMerge(t[r]):void 0!==t[r]&&(n[r]=t[r])})),J.forEach(a,(function(r){void 0!==e[r]?n[r]=e[r]:void 0!==t[r]&&(n[r]=t[r])}));var o=r.concat(s).concat(a),i=Object.keys(e).filter((function(t){return-1===o.indexOf(t)}));return J.forEach(i,(function(r){void 0!==e[r]?n[r]=e[r]:void 0!==t[r]&&(n[r]=t[r])})),n};function mt(t){this.defaults=t,this.interceptors={request:new Y,response:new Y}}mt.prototype.request=function(t){"string"==typeof t?(t=arguments[1]||{}).url=arguments[0]:t=t||{},(t=pt(this.defaults,t)).method?t.method=t.method.toLowerCase():this.defaults.method?t.method=this.defaults.method.toLowerCase():t.method="get";var e=[ht,void 0],n=Promise.resolve(t);for(this.interceptors.request.forEach((function(t){e.unshift(t.fulfilled,t.rejected)})),this.interceptors.response.forEach((function(t){e.push(t.fulfilled,t.rejected)}));e.length;)n=n.then(e.shift(),e.shift());return n},mt.prototype.getUri=function(t){return t=pt(this.defaults,t),G(t.url,t.params,t.paramsSerializer).replace(/^\?/,"")},J.forEach(["delete","get","head","options"],(function(t){mt.prototype[t]=function(e,n){return this.request(J.merge(n||{},{method:t,url:e}))}})),J.forEach(["post","put","patch"],(function(t){mt.prototype[t]=function(e,n,r){return this.request(J.merge(r||{},{method:t,url:e,data:n}))}}));var gt=mt;function vt(t){this.message=t}vt.prototype.toString=function(){return"Cancel"+(this.message?": "+this.message:"")},vt.prototype.__CANCEL__=!0;var bt=vt;function yt(t){if("function"!=typeof t)throw new TypeError("executor must be a function.");var e;this.promise=new Promise((function(t){e=t}));var n=this;t((function(t){n.reason||(n.reason=new bt(t),e(n.reason))}))}yt.prototype.throwIfRequested=function(){if(this.reason)throw this.reason},yt.source=function(){var t;return{token:new yt((function(e){t=e})),cancel:t}};var wt=yt;function xt(t){var e=new gt(t),n=P(gt.prototype.request,e);return J.extend(n,gt.prototype,e),J.extend(n,e),n}var $t=xt(ft);$t.Axios=gt,$t.create=function(t){return xt(pt($t.defaults,t))},$t.Cancel=bt,$t.CancelToken=wt,$t.isCancel=tt,$t.all=function(t){return Promise.all(t)},$t.spread=function(t){return function(e){return t.apply(null,e)}};var Et=$t,Lt=$t;Et.default=Lt;var Ct=Et;async function kt(t,e){const n=await Ct.get("/api/"+t,{params:e});if(!n.data)throw Error("No reply from server");return n.data}class Nt{constructor(t,e){this.onRefresh=t,this.every=e,this.intervalID=0,this.active=!1,document.addEventListener("visibilitychange",()=>this.handleVisibilityChange())}handleVisibilityChange(){document.hidden?this._off():this.active&&this.on(!0)}_off(){clearInterval(this.intervalID),this.intervalID=0}off(){this.active=!1,this._off()}on(t=!1){this.active=!0,this._off(),document.hidden||(this.intervalID=setInterval(this.onRefresh,this.every),t&&this.onRefresh())}setEvery(t){t!=this.every&&(this._off(),this.every=t,this.on())}}class Tt{constructor(t,e){this.onUpdate=t,this.onError=e,this.pending=0,this.maxPending=5,this.refresher=new Nt(()=>this.refresh(),500),this.refresher.on()}async refresh(){if(this.pending<this.maxPending){this.pending+=1;try{const t=await kt("status");this.refresher.setEvery(2500),this.onUpdate(t)}catch(t){this.refresher.setEvery(7500),this.onError(t)}finally{this.pending-=1,this.pending<0&&(this.pending=0)}}}}const At=[];function St(t,e){return{subscribe:Ot(t,e).subscribe}}function Ot(e,n=t){let r;const s=[];function o(t){if(a(e,t)&&(e=t,r)){const t=!At.length;for(let t=0;t<s.length;t+=1){const n=s[t];n[1](),At.push(n,e)}if(t){for(let t=0;t<At.length;t+=2)At[t][0](At[t+1]);At.length=0}}}return{set:o,update:function(t){o(t(e))},subscribe:function(a,i=t){const c=[a,i];return s.push(c),1===s.length&&(r=n(o)||t),a(e),()=>{const t=s.indexOf(c);-1!==t&&s.splice(t,1),0===s.length&&(r(),r=null)}}}}function Rt(e,n,a){const o=!Array.isArray(e),i=o?[e]:e,c=n.length<2;return St(a,e=>{let a=!1;const l=[];let u=0,f=t;const d=()=>{if(u)return;f();const r=n(o?l[0]:l,e);c?e(r):f=s(r)?r:t},h=i.map((e,n)=>function(e,...n){if(null==e)return t;const r=e.subscribe(...n);return r.unsubscribe?()=>r.unsubscribe():r}(e,t=>{l[n]=t,u&=~(1<<n),a&&d()},()=>{u|=1<<n}));return a=!0,d(),function(){r(h),f()}})}function Ht(){const t=window.location.href.indexOf("#/");let e=t>-1?window.location.href.substr(t+1):"/";const n=e.indexOf("?");let r="";return n>-1&&(r=e.substr(n+1),e=e.substr(0,n)),{location:e,querystring:r}}const jt=St(Ht(),(function(t){const e=()=>{t(Ht())};return window.addEventListener("hashchange",e,!1),function(){window.removeEventListener("hashchange",e,!1)}})),Bt=Rt(jt,t=>t.location);Rt(jt,t=>t.querystring);const Mt=[];let _t;function Ut(t){t.node.classList.remove(t.className),t.pattern.test(_t)&&t.node.classList.add(t.className)}function qt(t,e){if(!(e=e&&"string"==typeof e?{path:e}:e||{}).path&&t.hasAttribute("href")&&(e.path=t.getAttribute("href"),e.path&&e.path.length>1&&"#"==e.path.charAt(0)&&(e.path=e.path.substring(1))),e.className||(e.className="active"),!e.path||e.path.length<1||"/"!=e.path.charAt(0)&&"*"!=e.path.charAt(0))throw Error('Invalid value for "path" argument');const{pattern:n}=function(t,e){if(t instanceof RegExp)return{keys:!1,pattern:t};var n,r,s,a,o=[],i="",c=t.split("/");for(c[0]||c.shift();s=c.shift();)"*"===(n=s[0])?(o.push("wild"),i+="/(.*)"):":"===n?(r=s.indexOf("?",1),a=s.indexOf(".",1),o.push(s.substring(1,~r?r:~a?a:s.length)),i+=~r&&!~a?"(?:/([^/]+?))?":"/([^/]+?)",~a&&(i+=(~r?"?":"")+"\\"+s.substring(a))):i+="/"+s;return{keys:o,pattern:new RegExp("^"+i+(e?"(?=$|/)":"/?$"),"i")}}(e.path),r={node:t,className:e.className,pattern:n};return Mt.push(r),Ut(r),{destroy(){Mt.splice(Mt.indexOf(r),1)}}}function Dt(e){let n,r,s,a,u,p,v,b,y,w,x,$=e[0].isLive?"Live":"Offline";return{c(){n=f("nav"),r=f("ul"),s=f("li"),a=f("a"),a.textContent="Home",p=h(),v=f("ul"),b=f("li"),y=f("h5"),w=d($),m(a,"href","#/"),m(a,"class","nav-link"),m(s,"class","nav-item d-none d-sm-inline-block"),m(r,"class","navbar-nav"),m(y,"class","nav-link m-0"),m(b,"class","nav-item"),m(v,"class","navbar-nav ml-auto"),m(n,"class","main-header navbar navbar-expand navbar-white navbar-light")},m(t,e){c(t,n,e),i(n,r),i(r,s),i(s,a),i(n,p),i(n,v),i(v,b),i(b,y),i(y,w),x=o(u=qt.call(null,a))},p(t,[e]){1&e&&$!==($=t[0].isLive?"Live":"Offline")&&g(w,$)},i:t,o:t,d(t){t&&l(n),x()}}}function Pt(t,e,n){let{state:r}=e;return t.$set=t=>{"state"in t&&n(0,r=t.state)},[r]}jt.subscribe(t=>{_t=t.location+(t.querystring?"?"+t.querystring:""),Mt.map(Ut)});class It extends D{constructor(t){super(),q(this,t,Pt,Dt,a,{state:0})}}function Ft(e){let n,s,a,u,d,p,g,v,b,y,w,x,$,E,L,C,k,N,T,A,S,O,R,H,j,B,M,_,U,q;return{c(){n=f("aside"),s=f("a"),s.innerHTML='<img src="dist/img/logo.png" alt="logo" class="brand-image"> \n    <span class="brand-text">Noobcash</span>',a=h(),u=f("div"),d=f("nav"),p=f("ul"),g=f("li"),v=f("a"),v.innerHTML='<i class="nav-icon fas fa-home"></i> \n            <p>Home</p>',y=h(),w=f("li"),x=f("a"),x.innerHTML='<i class="nav-icon fas fa-tachometer-alt"></i> \n            <p>Status</p>',E=h(),L=f("li"),C=f("a"),C.innerHTML='<i class="nav-icon fas fa-wallet"></i> \n            <p>Wallet</p>',N=h(),T=f("li"),A=f("a"),A.innerHTML='<i class="nav-icon fas fa-network-wired"></i> \n            <p>Network</p>',O=h(),R=f("li"),H=f("a"),H.innerHTML='<i class="nav-icon fas fa-plug"></i> \n            <p>Connect</p>',B=h(),M=f("li"),_=f("a"),_.innerHTML='<i class="nav-icon fas fa-th"></i> \n            <p>\n              Example\n              <span class="right badge badge-danger">New</span></p>',m(s,"href","/"),m(s,"class","brand-link"),m(v,"href","#/"),m(v,"class","nav-link"),m(g,"class","nav-item"),m(x,"href","#/status"),m(x,"class","nav-link"),m(w,"class","nav-item"),m(C,"href","#/wallet"),m(C,"class","nav-link"),m(L,"class","nav-item"),m(A,"href","#/network"),m(A,"class","nav-link"),m(T,"class","nav-item"),m(H,"href","#/connect"),m(H,"class","nav-link"),m(R,"class","nav-item"),m(_,"href","#/example"),m(_,"class","nav-link"),m(M,"class","nav-item"),m(p,"class","nav nav-pills nav-sidebar flex-column"),m(d,"class","mt-2"),m(u,"class","sidebar"),m(n,"class","main-sidebar sidebar-dark-primary")},m(t,e){c(t,n,e),i(n,s),i(n,a),i(n,u),i(u,d),i(d,p),i(p,g),i(g,v),i(p,y),i(p,w),i(w,x),i(p,E),i(p,L),i(L,C),i(p,N),i(p,T),i(T,A),i(p,O),i(p,R),i(R,H),i(p,B),i(p,M),i(M,_),q=[o(b=qt.call(null,v)),o($=qt.call(null,x)),o(k=qt.call(null,C)),o(S=qt.call(null,A)),o(j=qt.call(null,H)),o(U=qt.call(null,_))]},p:t,i:t,o:t,d(t){t&&l(n),r(q)}}}class zt extends D{constructor(t){super(),q(this,t,null,Ft,a,{})}}function Vt(e){let n,r,s,a,o,u,p,v,b,y,w,x,$,E,L,C,k,N,T,A,S,O,R,H,j,B,M,_,U,q,D,P,I,F,z,V,W,X,J,K,G=e[0].content.status.blockchain.length+"",Q=e[0].content.status.balance+"",Y=e[0].content.status.neighbors.length+"";return{c(){n=f("div"),r=f("a"),s=f("div"),a=f("div"),o=f("h3"),o.textContent="Status",u=h(),p=f("p"),v=d("Blockchain has "),b=d(G),y=d(" blocks"),w=h(),x=f("div"),x.innerHTML='<i class="fas fa-tachometer-alt svelte-tvxc5o"></i>',$=h(),E=f("div"),L=f("a"),C=f("div"),k=f("div"),N=f("h3"),N.textContent="Wallet",T=h(),A=f("p"),S=d("Balance is "),O=d(Q),R=d(" NBC"),H=h(),j=f("div"),j.innerHTML='<i class="fas fa-wallet svelte-tvxc5o"></i>',B=h(),M=f("div"),_=f("a"),U=f("div"),q=f("div"),D=f("h3"),D.textContent="Network",P=h(),I=f("p"),F=d("Connected to "),z=d(Y),V=d(" neighbors"),W=h(),X=f("div"),X.innerHTML='<i class="fas fa-network-wired svelte-tvxc5o"></i>',J=h(),K=f("div"),K.innerHTML='<a href="#/connect"><div class="small-box bg-primary svelte-tvxc5o"><div class="inner"><h3>Connect</h3> \n        <p>Click to connect to other nodes</p></div> \n      <div class="icon svelte-tvxc5o"><i class="fas fa-plug svelte-tvxc5o"></i></div></div></a>',m(a,"class","inner"),m(x,"class","icon svelte-tvxc5o"),m(s,"class","small-box bg-primary svelte-tvxc5o"),m(r,"href","#/status"),m(n,"class","col-lg-3 col-6"),m(k,"class","inner"),m(j,"class","icon svelte-tvxc5o"),m(C,"class","small-box bg-primary svelte-tvxc5o"),m(L,"href","#/wallet"),m(E,"class","col-lg-3 col-6"),m(q,"class","inner"),m(X,"class","icon svelte-tvxc5o"),m(U,"class","small-box bg-primary svelte-tvxc5o"),m(_,"href","#/network"),m(M,"class","col-lg-3 col-6"),m(K,"class","col-lg-3 col-6")},m(t,e){c(t,n,e),i(n,r),i(r,s),i(s,a),i(a,o),i(a,u),i(a,p),i(p,v),i(p,b),i(p,y),i(s,w),i(s,x),c(t,$,e),c(t,E,e),i(E,L),i(L,C),i(C,k),i(k,N),i(k,T),i(k,A),i(A,S),i(A,O),i(A,R),i(C,H),i(C,j),c(t,B,e),c(t,M,e),i(M,_),i(_,U),i(U,q),i(q,D),i(q,P),i(q,I),i(I,F),i(I,z),i(I,V),i(U,W),i(U,X),c(t,J,e),c(t,K,e)},p(t,[e]){1&e&&G!==(G=t[0].content.status.blockchain.length+"")&&g(b,G),1&e&&Q!==(Q=t[0].content.status.balance+"")&&g(O,Q),1&e&&Y!==(Y=t[0].content.status.neighbors.length+"")&&g(z,Y)},i:t,o:t,d(t){t&&l(n),t&&l($),t&&l(E),t&&l(B),t&&l(M),t&&l(J),t&&l(K)}}}function Wt(t,e,n){let{state:r}=e;return t.$set=t=>{"state"in t&&n(0,r=t.state)},[r]}class Xt extends D{constructor(t){super(),q(this,t,Wt,Vt,a,{state:0})}}function Jt(e){let n,r,s,a,o,u,p,v,b,y,w,x,$,E,L,C,k,N,T,A,S,O,R,H,j,B=e[0].content.status.host+"",M=e[0].content.status.port+"",_=e[0].content.status.blockchain.length+"",U=e[0].content.status.neighbors.length+"";return{c(){n=f("div"),r=f("div"),s=f("div"),s.innerHTML='<h5 class="card-title">Listening on</h5>',a=h(),o=f("div"),u=d("["),p=d(B),v=d("]:"),b=d(M),y=h(),w=f("div"),x=f("div"),$=f("div"),$.innerHTML='<h5 class="card-title">Blockchain length</h5>',E=h(),L=f("div"),C=d(_),k=d(" Blocks"),N=h(),T=f("div"),A=f("div"),S=f("div"),S.innerHTML='<h5 class="card-title">Connected to</h5>',O=h(),R=f("div"),H=d(U),j=d(" Neighbors"),m(s,"class","card-header"),m(o,"class","card-body"),m(r,"class","card card-primary card-outline"),m(n,"class","col-sm-2"),m($,"class","card-header"),m(L,"class","card-body"),m(x,"class","card card-primary card-outline"),m(w,"class","col-sm-2"),m(S,"class","card-header"),m(R,"class","card-body"),m(A,"class","card card-primary card-outline"),m(T,"class","col-sm-2")},m(t,e){c(t,n,e),i(n,r),i(r,s),i(r,a),i(r,o),i(o,u),i(o,p),i(o,v),i(o,b),c(t,y,e),c(t,w,e),i(w,x),i(x,$),i(x,E),i(x,L),i(L,C),i(L,k),c(t,N,e),c(t,T,e),i(T,A),i(A,S),i(A,O),i(A,R),i(R,H),i(R,j)},p(t,[e]){1&e&&B!==(B=t[0].content.status.host+"")&&g(p,B),1&e&&M!==(M=t[0].content.status.port+"")&&g(b,M),1&e&&_!==(_=t[0].content.status.blockchain.length+"")&&g(C,_),1&e&&U!==(U=t[0].content.status.neighbors.length+"")&&g(H,U)},i:t,o:t,d(t){t&&l(n),t&&l(y),t&&l(w),t&&l(N),t&&l(T)}}}function Kt(t,e,n){let{state:r}=e;return t.$set=t=>{"state"in t&&n(0,r=t.state)},[r]}class Gt extends D{constructor(t){super(),q(this,t,Kt,Jt,a,{state:0})}}function Qt(t,e,n){const r=t.slice();return r[1]=e[n][0],r[2]=e[n][1],r[4]=n,r}function Yt(t){let e,n,r,s,a,o,u,p,v,b,y,w,x=t[1]+"",$=t[2]+"";return{c(){e=f("tr"),n=f("td"),r=d(t[4]),s=h(),a=f("td"),o=f("a"),u=d(x),v=h(),b=f("td"),y=d($),w=h(),m(o,"href",p="#/tx/"+t[1])},m(t,l){c(t,e,l),i(e,n),i(n,r),i(e,s),i(e,a),i(a,o),i(o,u),i(e,v),i(e,b),i(b,y),i(e,w)},p(t,e){1&e&&x!==(x=t[1]+"")&&g(u,x),1&e&&p!==(p="#/tx/"+t[1])&&m(o,"href",p),1&e&&$!==($=t[2]+"")&&g(y,$)},d(t){t&&l(e)}}}function Zt(e){let n,r,s,a,o,p,v,b,y,w,x,$,E,L,C,k,N,T,A=e[0].content.status.balance+"",S=e[0].content.status.utxos,O=[];for(let t=0;t<S.length;t+=1)O[t]=Yt(Qt(e,S,t));return{c(){n=f("div"),r=f("div"),s=f("div"),s.innerHTML='<h5 class="m-0">Balance</h5>',a=h(),o=f("div"),p=f("h6"),v=d(A),b=d(" NBC"),y=h(),w=f("div"),x=f("div"),$=f("div"),$.innerHTML='<h5 class="m-0">Unspent transaction outputs</h5>',E=h(),L=f("div"),C=f("table"),k=f("thead"),k.innerHTML="<tr><th>#</th> \n            <th>Transaction hash</th> \n            <th>Amount (NBC)</th></tr>",N=h(),T=f("tbody");for(let t=0;t<O.length;t+=1)O[t].c();m(s,"class","card-header"),m(p,"class","card-title"),m(o,"class","card-body"),m(r,"class","card card-primary card-outline"),m(n,"class","col-lg-3"),m($,"class","card-header"),m(C,"class","table table-striped"),m(L,"class","card-body p-0"),m(x,"class","card card-primary"),m(w,"class","col-lg-9")},m(t,e){c(t,n,e),i(n,r),i(r,s),i(r,a),i(r,o),i(o,p),i(p,v),i(p,b),c(t,y,e),c(t,w,e),i(w,x),i(x,$),i(x,E),i(x,L),i(L,C),i(C,k),i(C,N),i(C,T);for(let t=0;t<O.length;t+=1)O[t].m(T,null)},p(t,[e]){if(1&e&&A!==(A=t[0].content.status.balance+"")&&g(v,A),1&e){let n;for(S=t[0].content.status.utxos,n=0;n<S.length;n+=1){const r=Qt(t,S,n);O[n]?O[n].p(r,e):(O[n]=Yt(r),O[n].c(),O[n].m(T,null))}for(;n<O.length;n+=1)O[n].d(1);O.length=S.length}},i:t,o:t,d(t){t&&l(n),t&&l(y),t&&l(w),u(O,t)}}}function te(t,e,n){let{state:r}=e;return t.$set=t=>{"state"in t&&n(0,r=t.state)},[r]}class ee extends D{constructor(t){super(),q(this,t,te,Zt,a,{state:0})}}function ne(e){let n,s,a,o,u,b,y,w,x,$,E,L;return{c(){n=f("div"),s=f("div"),a=f("div"),a.innerHTML='<h5 class="card-title">Enter hosts to connect to (one per line)</h5>',o=h(),u=f("div"),b=f("textarea"),y=h(),w=f("div"),x=f("button"),$=d(e[1]),m(a,"class","card-header"),m(b,"class","form-control"),m(b,"rows","10"),m(b,"placeholder","10.0.0.1:5000"),m(u,"class","card-body"),m(x,"class",E="btn "+e[2]),m(w,"class","card-footer"),m(s,"class","card card-primary card-outline"),m(n,"class","col-lg-6")},m(t,r){c(t,n,r),i(n,s),i(s,a),i(s,o),i(s,u),i(u,b),v(b,e[0]),i(s,y),i(s,w),i(w,x),i(x,$),L=[p(b,"input",e[5]),p(x,"click",e[3])]},p(t,[e]){1&e&&v(b,t[0]),2&e&&g($,t[1]),4&e&&E!==(E="btn "+t[2])&&m(x,"class",E)},i:t,o:t,d(t){t&&l(n),r(L)}}}function re(t,e,n){let r=!0,s="",a="Connect",o="btn-primary";return[s,a,o,async function(t){if(r){r=!1;try{n(1,a="Connecting"),n(2,o="btn-warning");let t=0;for(const e of s.split("\n")){const n=e.lastIndexOf(":");if(n<0)continue;const r=e.slice(0,n),s=e.slice(n+1);t+=1,await kt("connectToNeighbor",{host:r,port:s})}t?(n(1,a=`Will connect to ${t} neighbors`),n(2,o="btn-success")):(n(1,a="Connect"),n(2,o="btn-primary"))}catch(t){n(1,a="Connect failed"),n(2,o="btn-danger"),r=!0}}},r,function(){s=this.value,n(0,s)}]}class se extends D{constructor(t){super(),q(this,t,re,ne,a,{})}}function ae(t,e,n){const r=t.slice();return r[1]=e[n].peerName,r[2]=e[n].lastBlockID,r[3]=e[n].connected,r[5]=n,r}function oe(t){let e,n,r,s,a,o,u,p,v,b,y,w,x,$,E,L,C,k,N=t[1][0]+"",T=t[1][1]+"",A=t[2]+"",S=t[3]?"OK":"DISC";return{c(){e=f("tr"),n=f("td"),r=d(t[5]),s=h(),a=f("td"),o=d(N),u=h(),p=f("td"),v=d(T),b=h(),y=f("td"),w=d(A),x=h(),$=f("td"),E=f("span"),L=d(S),k=h(),m(E,"class",C=t[3]?"badge badge-success":"badge badge-danger")},m(t,l){c(t,e,l),i(e,n),i(n,r),i(e,s),i(e,a),i(a,o),i(e,u),i(e,p),i(p,v),i(e,b),i(e,y),i(y,w),i(e,x),i(e,$),i($,E),i(E,L),i(e,k)},p(t,e){1&e&&N!==(N=t[1][0]+"")&&g(o,N),1&e&&T!==(T=t[1][1]+"")&&g(v,T),1&e&&A!==(A=t[2]+"")&&g(w,A),1&e&&S!==(S=t[3]?"OK":"DISC")&&g(L,S),1&e&&C!==(C=t[3]?"badge badge-success":"badge badge-danger")&&m(E,"class",C)},d(t){t&&l(e)}}}function ie(e){let n,r,s,a,o,p,v,b,y,w,x,$,E,L=e[0].content.status.neighbors.length+"",C=e[0].content.status.neighbors,k=[];for(let t=0;t<C.length;t+=1)k[t]=oe(ae(e,C,t));return{c(){n=f("div"),r=f("div"),s=f("div"),a=f("h3"),a.textContent="Neighbors",o=h(),p=f("span"),v=d(L),b=h(),y=f("div"),w=f("table"),x=f("thead"),x.innerHTML="<tr><th>#</th> \n            <th>Host</th> \n            <th>Port</th> \n            <th>Latest block</th> \n            <th>Status</th></tr>",$=h(),E=f("tbody");for(let t=0;t<k.length;t+=1)k[t].c();m(a,"class","card-title"),m(p,"class","badge badge-light badge-pill float-right"),m(s,"class","card-header"),m(w,"class","table table-striped"),m(y,"class","card-body p-0"),m(r,"class","card card-primary"),m(n,"class","col")},m(t,e){c(t,n,e),i(n,r),i(r,s),i(s,a),i(s,o),i(s,p),i(p,v),i(r,b),i(r,y),i(y,w),i(w,x),i(w,$),i(w,E);for(let t=0;t<k.length;t+=1)k[t].m(E,null)},p(t,[e]){if(1&e&&L!==(L=t[0].content.status.neighbors.length+"")&&g(v,L),1&e){let n;for(C=t[0].content.status.neighbors,n=0;n<C.length;n+=1){const r=ae(t,C,n);k[n]?k[n].p(r,e):(k[n]=oe(r),k[n].c(),k[n].m(E,null))}for(;n<k.length;n+=1)k[n].d(1);k.length=C.length}},i:t,o:t,d(t){t&&l(n),u(k,t)}}}function ce(t,e,n){let{state:r}=e;return t.$set=t=>{"state"in t&&n(0,r=t.state)},[r]}class le extends D{constructor(t){super(),q(this,t,ce,ie,a,{state:0})}}function ue(e){let n;return{c(){n=f("li"),n.textContent="Home",m(n,"class","breadcrumb-item active")},m(t,e){c(t,n,e)},p:t,d(t){t&&l(n)}}}function fe(t){let e,n,r,s;return{c(){e=f("li"),e.innerHTML='<a href="#/">Home</a>',n=h(),r=f("li"),s=d(t[2]),m(e,"class","breadcrumb-item"),m(r,"class","breadcrumb-item active")},m(t,a){c(t,e,a),c(t,n,a),c(t,r,a),i(r,s)},p(t,e){4&e&&g(s,t[2])},d(t){t&&l(e),t&&l(n),t&&l(r)}}}function de(t){let e,n,s,a,o,u,p,v,b,y,w,x,$,E,L=(t[2]||"Home")+"";function C(t,e){return t[2]?fe:ue}let k=C(t),N=k(t);var T=t[1];function A(t){return{props:{state:t[0]}}}if(T)var S=new T(A(t));return{c(){e=f("div"),n=f("div"),s=f("div"),a=f("div"),o=f("div"),u=f("h1"),p=d(L),v=h(),b=f("div"),y=f("ol"),N.c(),w=h(),x=f("div"),$=f("div"),S&&B(S.$$.fragment),m(u,"class","m-0 text-dark"),m(o,"class","col-sm-6"),m(y,"class","breadcrumb float-sm-right"),m(b,"class","col-sm-6"),m(a,"class","row mb-2"),m(s,"class","container-fluid"),m(n,"class","content-header"),m($,"class","container-fluid row"),m(x,"class","content"),m(e,"class","content-wrapper")},m(t,r){c(t,e,r),i(e,n),i(n,s),i(s,a),i(a,o),i(o,u),i(u,p),i(a,v),i(a,b),i(b,y),N.m(y,null),i(e,w),i(e,x),i(x,$),S&&M(S,$,null),E=!0},p(t,[e]){(!E||4&e)&&L!==(L=(t[2]||"Home")+"")&&g(p,L),k===(k=C(t))&&N?N.p(t,e):(N.d(1),N=k(t),N&&(N.c(),N.m(y,null)));const n={};if(1&e&&(n.state=t[0]),T!==(T=t[1])){if(S){R={r:0,c:[],p:R};const t=S;j(t.$$.fragment,1,0,()=>{_(t,1)}),R.r||r(R.c),R=R.p}T?(B((S=new T(A(t))).$$.fragment),H(S.$$.fragment,1),M(S,$,null)):S=null}else T&&S.$set(n)},i(t){E||(S&&H(S.$$.fragment,t),E=!0)},o(t){S&&j(S.$$.fragment,t),E=!1},d(t){t&&l(e),N.d(),S&&_(S)}}}function he(t,e,n){let{state:r}=e;const s={"/":[Xt,null],"/status":[Gt,"Status"],"/wallet":[ee,"Wallet"],"/connect":[se,"Connect"],"/network":[le,"Network"]};let[a,o]=s["/status"];return Bt.subscribe(t=>{const e=s[t];console.log(t,e),e?function(t){n(1,[a,o]=t,a,n(2,o)),document.title="Noobcash"+(o?" "+o:"")}(e):function(t){if(!t||t.length<1||"/"!=t.charAt(0)&&0!==t.indexOf("#/"))throw Error("Invalid parameter location");setTimeout(()=>{const e=("#"==t.charAt(0)?"":"#")+t;history.replaceState(void 0,void 0,e),window.dispatchEvent(new Event("hashchange"))},0)}("/")}),t.$set=t=>{"state"in t&&n(0,r=t.state)},[r,a,o]}class pe extends D{constructor(t){super(),q(this,t,he,de,a,{state:0})}}function me(e){let n,r,s,a,o,u=e[0].isLive?"Live":"Offline";return{c(){n=f("footer"),r=f("span"),r.innerHTML='<strong>Noobcash Web UI</strong>, based on <a href="https://github.com/ColorlibHQ/AdminLTE" target="_blank">AdminLTE.io</a>',s=h(),a=f("h5"),o=d(u),m(r,"class","float-right"),m(a,"class","m-0"),m(n,"class","main-footer")},m(t,e){c(t,n,e),i(n,r),i(n,s),i(n,a),i(a,o)},p(t,[e]){1&e&&u!==(u=t[0].isLive?"Live":"Offline")&&g(o,u)},i:t,o:t,d(t){t&&l(n)}}}function ge(t,e,n){let{state:r}=e;return t.$set=t=>{"state"in t&&n(0,r=t.state)},[r]}class ve extends D{constructor(t){super(),q(this,t,ge,me,a,{state:0})}}function be(t){let e,n,r,s;const a=new It({props:{state:t[0]}}),o=new zt({props:{state:t[0]}}),i=new pe({props:{state:t[0]}}),u=new ve({props:{state:t[0]}});return{c(){B(a.$$.fragment),e=h(),B(o.$$.fragment),n=h(),B(i.$$.fragment),r=h(),B(u.$$.fragment)},m(t,l){M(a,t,l),c(t,e,l),M(o,t,l),c(t,n,l),M(i,t,l),c(t,r,l),M(u,t,l),s=!0},p(t,[e]){const n={};1&e&&(n.state=t[0]),a.$set(n);const r={};1&e&&(r.state=t[0]),o.$set(r);const s={};1&e&&(s.state=t[0]),i.$set(s);const c={};1&e&&(c.state=t[0]),u.$set(c)},i(t){s||(H(a.$$.fragment,t),H(o.$$.fragment,t),H(i.$$.fragment,t),H(u.$$.fragment,t),s=!0)},o(t){j(a.$$.fragment,t),j(o.$$.fragment,t),j(i.$$.fragment,t),j(u.$$.fragment,t),s=!1},d(t){_(a,t),t&&l(e),_(o,t),t&&l(n),_(i,t),t&&l(r),_(u,t)}}}function ye(t,e,n){let{state:r}=e;new Tt(t=>{n(0,r.isLive=!0,r),n(0,r.content.status=t,r)},t=>{n(0,r.isLive=!1,r)});return t.$set=t=>{"state"in t&&n(0,r=t.state)},[r]}return new class extends D{constructor(t){super(),q(this,t,ye,be,a,{state:0})}}({target:document.body,props:{state:{isLive:!1,content:{status:{host:"0.0.0.0",port:5e3,neighbors:[],blockchain:[],utxos:[],balance:null}}}}})}();
//# sourceMappingURL=bundle.js.map
