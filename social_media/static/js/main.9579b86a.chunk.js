(this["webpackJsonppost-comment"]=this["webpackJsonppost-comment"]||[]).push([[0],{12:function(e,t,n){},13:function(e,t,n){},15:function(e,t,n){"use strict";n.r(t);var c=n(1),o=n.n(c),s=n(6),i=n.n(s),a=(n(12),n.p,n(13),n(7)),r=n(2),l=n(0);function d(e){403===e&&(alert("you are not login"),window.location.href="http://127.0.0.1:8000/login"),500===e&&alert("server side error")}function m(e){var t=Object(c.useState)([]),n=Object(r.a)(t,2),o=n[0],s=n[1],i=Object(c.useState)([]),m=Object(r.a)(i,2),b=m[0],p=m[1],O=Object(c.useState)("btn-outline-primary"),f=Object(r.a)(O,2),h=f[0],x=f[1],v=Object(c.useState)(!!o.is_like),g=Object(r.a)(v,2),k=g[0],N=g[1];Object(c.useEffect)((function(){!function(e){var t=new XMLHttpRequest;t.responseType="json";var n=window.location.href;console.log(n.split(":"));var c=n.split("=")[1];t.open("GET","http://127.0.0.1:8000/api/post/data/".concat(c)),t.onload=function(){var n=t.response;e(n)},t.onerror=function(e){console.log(e)},t.send()}((function(e){console.log(e),s(e),p(e.post_comment)}))}),[]);var S=o.id,T=o.likes,y=o.photo,w=o.post_description,R=Object(c.useState)(T),_=Object(r.a)(R,2),q=(_[0],_[1]);return Object(l.jsx)("div",{className:" mb-1 col-md-4 mx-auto ",children:Object(l.jsx)("div",{className:"col m-3 ",children:Object(l.jsxs)("div",{className:"card  ",children:[Object(l.jsx)("img",{src:y,className:"card-img-top m-1"}),Object(l.jsxs)("div",{className:"row m-3",children:[Object(l.jsx)("div",{className:"col-9 ",children:Object(l.jsx)("h4",{className:"card-text col-auto",children:w})}),Object(l.jsx)("div",{className:"col-3 text-right",children:Object(l.jsxs)("button",{className:"btn "+h,onClick:function(){console.log(k),k?u(JSON.stringify({id:o.id,action:"unlike"}),!0,"POST","api/post/action",(function(e,t){200===t?(x("btn-primary"),q(e.likes),s(e),N(!1)):d(t)})):u(JSON.stringify({id:o.id,action:"like"}),!0,"POST","api/post/action",(function(e,t){200===t?(x("btn-outline-primary"),N(!0),s(e),q(e.likes)):d(t)}))},children:[T," like"]})})]}),Object(l.jsx)("div",{children:Object(l.jsxs)("div",{className:" p-2 m-3 card",children:[Object(l.jsx)("form",{onSubmit:function(e){!function(e){e.preventDefault();var t=Object(a.a)(b),n=new FormData(e.target);n.append("post",S),u(n,!1,"POST","api/post/do_comment",(function(n,c){200===c?(t.unshift(n),p(t),e.target.reset()):(d(c),alert("there is an error"))}))}(e)},children:Object(l.jsxs)("div",{className:"row m-2",children:[Object(l.jsx)("div",{className:"col",children:Object(l.jsx)("input",{type:"text",name:"comment",className:"col-12 mt-1 border rounded-pill",required:!0})}),Object(l.jsx)("div",{className:"col-auto text-right  ",children:Object(l.jsx)("div",{className:"text-right",children:Object(l.jsx)("input",{type:"submit",name:"DoComment",className:"btn border rounded-pill",value:"comment"})})})]})}),Object(l.jsx)(j,{comments:b})]})})]})})})}function u(e,t,n,c,o){var s=new XMLHttpRequest,i=function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),c=0;c<n.length;c++){var o=n[c].trim();if(o.substring(0,e.length+1)===e+"="){t=decodeURIComponent(o.substring(e.length+1));break}}return t}("csrftoken");s.responseType="json",console.log(e,c),s.open(n,"http://127.0.0.1:8000/".concat(c)),t&&s.setRequestHeader("Content-Type","application/json"),i&&(console.log("csrf token"),s.setRequestHeader("HTTP_X_REQUESTED_WITH","XMLHttpRequest"),s.setRequestHeader("X-Requested-With","XMLHttpRequest"),s.setRequestHeader("X-CSRFToken",i)),s.onload=function(){var e=s.response,t=s.status;console.log(e),o(e,t)},s.onerror=function(e){console.log(e)},s.send(e)}function j(e){return void 0!=e.comments?e.comments.map((function(e,t){return Object(l.jsx)(b,{comment:e},t)})):Object(l.jsx)("h4",{children:"hi"})}function b(e){var t,n=e.comment;console.log(n.is_like),t=n.is_like?"unlike":"like";var o=Object(c.useState)({doLike:n.is_like,text:t}),s=Object(r.a)(o,2),i=s[0],a=s[1];return Object(l.jsx)("div",{className:"m-2 card p-2",id:n.comment,children:Object(l.jsxs)("div",{className:"row",children:[Object(l.jsx)("div",{className:"col-10  ",children:Object(l.jsx)("div",{className:"text-left",children:Object(l.jsxs)("p",{className:"text-left",children:[n.comment," "]})})}),Object(l.jsx)("div",{className:"col ",children:Object(l.jsx)("button",{className:"btn",onClick:function(e){return function(e){var t;console.log(e),i.doLike?(t={id:e,action:i.text},u(JSON.stringify(t),!0,"POST","api/post_comment/action",(function(e,t){200===t?a({doLike:!1,text:"like"}):d(t)}))):(t={id:e,action:i.text},u(JSON.stringify(t),!0,"POST","api/post_comment/action",(function(e,t){200===t?a({doLike:!0,text:"unlike"}):d(t)})))}(n.id)},children:Object(l.jsx)("a",{className:"text-right",name:"like-button","post-id":"+comment.id+",children:i.text})})})]})})}var p=function(){return Object(l.jsx)(m,{})},O=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,16)).then((function(t){var n=t.getCLS,c=t.getFID,o=t.getFCP,s=t.getLCP,i=t.getTTFB;n(e),c(e),o(e),s(e),i(e)}))};i.a.render(Object(l.jsx)(o.a.StrictMode,{children:Object(l.jsx)(p,{})}),document.getElementById("root")),O()}},[[15,1,2]]]);
//# sourceMappingURL=main.9579b86a.chunk.js.map