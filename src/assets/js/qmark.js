
/* q_status (18.09.2026): метка визита для Директа — «бот» сразу, «человек» после живых действий
   (мышь с поворотами, касания, увеличение пальцами, клавиатура). Сегмент «не человек» = −100 % в кампаниях. */
(function(){var C=104009490;if(window.__qmark)return;window.__qmark=1;
var ua=navigator.userAgent||"",bot=!!navigator.webdriver||/HeadlessChrome|PhantomJS|Lighthouse|bot|crawl|spider|slurp/i.test(ua)||!navigator.languages||navigator.languages.length===0||!screen.width||!screen.height;
var t=0,dx=0,dy=0,tc=0,k=0,z=false,done=false;
addEventListener("mousemove",function(e){var x=Math.sign(e.movementX||0),y=Math.sign(e.movementY||0);if((x&&dx&&x!==dx)||(y&&dy&&y!==dy))t++;if(x)dx=x;if(y)dy=y;},{passive:true});
addEventListener("touchstart",function(){tc++;},{passive:true});
addEventListener("keydown",function(){k++;});
if(window.visualViewport)visualViewport.addEventListener("resize",function(){if(visualViewport.scale>1.05)z=true;});
var iv=setInterval(function(){if(done||typeof window.ym!=="function")return;
if(bot){ym(C,"params",{q_status:"bot"});done=true;}else if(t>=8||tc>=3||z||k>=3){ym(C,"params",{q_status:"human"});done=true;}
if(done)clearInterval(iv);},2000);})();
