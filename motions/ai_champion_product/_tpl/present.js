(function(){
  var deck=document.getElementById('deck'); if(!deck) return;
  var slides=[].slice.call(deck.querySelectorAll('.pslide'));
  var body=document.body, dots=document.getElementById('pdots'), count=document.getElementById('pcount'), prog=document.getElementById('prog');
  var cur=0, on=false, savedY=0;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  slides.forEach(function(s,i){var d=document.createElement('button');d.type='button';d.className='dot'+(i===0?' on':'');d.setAttribute('aria-label','Slide '+(i+1));d.onclick=function(e){e.stopPropagation();show(i);};dots.appendChild(d);});
  function runCounters(s){
    [].forEach.call(s.querySelectorAll('.cnt[data-to]'),function(el){
      var to=+el.getAttribute('data-to'), dec=+(el.getAttribute('data-dec')||0), pre=el.getAttribute('data-pre')||'', suf=el.getAttribute('data-suf')||'';
      function fmt(v){return pre+(dec?v.toFixed(dec):Math.round(v).toLocaleString('en-US'))+suf;}
      if(reduce){el.textContent=fmt(to);return;}
      var start=Date.now(), dur=1200;
      var iv=setInterval(function(){var p=Math.min(1,(Date.now()-start)/dur);var e=1-Math.pow(1-p,3);el.textContent=fmt(e*to);if(p>=1)clearInterval(iv);},16);
    });
  }
  function show(i){
    cur=Math.max(0,Math.min(slides.length-1,i));
    slides.forEach(function(s,j){s.classList.toggle('active',j===cur);s.classList.toggle('past',j<cur);if(j===cur)s.scrollTop=0;});
    [].forEach.call(dots.children,function(d,j){d.classList.toggle('on',j===cur);});
    count.textContent=(cur+1)+' / '+slides.length;
    prog.style.width=((cur+1)/slides.length*100)+'%';
    if(on){history.replaceState(null,'','#present-'+(cur+1));}
    runCounters(slides[cur]);
  }
  function go(d){show(cur+d);}
  function enter(i){ if(on)return; on=true; savedY=window.scrollY||0; body.classList.add('present'); document.documentElement.classList.add('present'); show(typeof i==='number'?i:0); }
  function exit(){ if(!on)return; on=false; body.classList.remove('present'); document.documentElement.classList.remove('present'); slides.forEach(function(s){s.classList.remove('active','past');}); history.replaceState(null,'',location.pathname+location.search); window.scrollTo(0,savedY); }
  document.getElementById('presentBtn').addEventListener('click',function(){enter(0);});
  document.getElementById('pprev').addEventListener('click',function(e){e.stopPropagation();go(-1);});
  document.getElementById('pnext').addEventListener('click',function(e){e.stopPropagation();go(1);});
  document.getElementById('pexit').addEventListener('click',function(e){e.stopPropagation();exit();});
  document.addEventListener('keydown',function(e){
    if(!on){ if(e.key==='p'||e.key==='P'){ if(!/input|textarea|select/i.test(document.activeElement.tagName)) enter(0);} return; }
    if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'||e.key==='Enter'){e.preventDefault();go(1);}
    else if(e.key==='ArrowLeft'||e.key==='PageUp'||e.key==='Backspace'){e.preventDefault();go(-1);}
    else if(e.key==='Home'){show(0);} else if(e.key==='End'){show(slides.length-1);}
    else if(e.key==='Escape'){exit();}
  });
  deck.addEventListener('click',function(e){ if(!on)return; if(e.target.closest('a,button,input,select'))return; go(e.clientX<window.innerWidth*0.18?-1:1); });
  var tx=null;
  document.addEventListener('touchstart',function(e){tx=e.touches[0].clientX;},{passive:true});
  document.addEventListener('touchend',function(e){if(!on||tx===null)return;var dx=e.changedTouches[0].clientX-tx;if(Math.abs(dx)>60)go(dx<0?1:-1);tx=null;},{passive:true});
  var m=/^#present(?:-(\d+))?$/.exec(location.hash||'');
  if(m){enter(m[1]?Math.max(0,parseInt(m[1],10)-1):0);}
})();
(function(){
  var heroEl=document.querySelector('.hero'); if(heroEl){ setTimeout(function(){heroEl.classList.add('on');},80); }
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  setTimeout(function(){ [].forEach.call(document.querySelectorAll('.hero .hc[data-to]'),function(el){
    var to=+el.getAttribute('data-to'), dec=+(el.getAttribute('data-dec')||0);
    function fmt(v){return dec?v.toFixed(dec):Math.round(v).toLocaleString('en-US');}
    if(reduce){el.textContent=fmt(to);return;}
    var start=Date.now(), dur=1400;
    var iv=setInterval(function(){var p=Math.min(1,(Date.now()-start)/dur);var e=1-Math.pow(1-p,3);el.textContent=fmt(e*to);if(p>=1)clearInterval(iv);},16);
  }); },700);
  var groups=['.wrap table tbody','.cal','.steps','.threads','.grid','.statband','.acc','.qs'];
  var items=[];
  groups.forEach(function(g){[].forEach.call(document.querySelectorAll('.sheet '+g),function(c){[].forEach.call(c.children,function(el,i){el.classList.add('rv');el.style.setProperty('--i',i);items.push(el);});});});
  if(!('IntersectionObserver' in window)){items.forEach(function(el){el.classList.add('in');});return;}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'0px 0px -6% 0px'});
  items.forEach(function(el){io.observe(el);});
  setTimeout(function(){items.forEach(function(el){el.classList.add('in');});},1500);
})();
