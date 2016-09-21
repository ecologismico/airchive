loader=new loader();
resizer=new resizer();
loader.addF(function(){loadNavV('navV')});
loader.addF(function(){initNavV('navV','menuV')});
loader.addF(function(){bgFix();});
loader.addF(function(){positionFooter('head','main03','footer');});
resizer.addF(function(){positionFooter('head','main03','footer');});
window.onload=function(){loader.onload();initialize_gmap();}
window.onresize=function(){resizer.onresize();}