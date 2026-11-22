import os, xml.dom.minidom
Y,P,C,L,K="#FFE600","#FF3D81","#00D1FF","#B6FF3B","#000"
FONT="font-family:'Arial Black','Archivo Black',Impact,'Helvetica Neue',Arial,sans-serif;font-weight:900"
def w(name, s):
    xml.dom.minidom.parseString(s)
    open(f"assets/svg/{name}.svg","w",encoding="utf-8").write(s)

# ---------- BANNER ----------
tick = "★ PROGRAMMING &amp; AI ★ YEAR 2 BACCALAUREATE ★ INTERACTIVE ACTIVITIES ★ DR. WALAA EL-MASRY "
w("banner", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 340" width="1000" height="340" role="img" aria-label="Interactive Activities - Programming and AI, Year 2 Baccalaureate">
<style>
.f{{{FONT}}}
@keyframes bob{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-9px)}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes tick{{from{{transform:translateX(0)}}to{{transform:translateX(-1300px)}}}}
@keyframes pop{{0%,100%{{transform:rotate(-7deg) scale(1)}}50%{{transform:rotate(5deg) scale(1.1)}}}}
@keyframes blink{{0%,60%{{opacity:1}}61%,100%{{opacity:0}}}}
@keyframes drop{{from{{transform:translateY(-60px);opacity:0}}to{{transform:translateY(0);opacity:1}}}}
.t1{{animation:drop .6s cubic-bezier(.2,1.4,.4,1) both, bob 2.4s ease-in-out .6s infinite}}
.t2{{animation:drop .6s cubic-bezier(.2,1.4,.4,1) .2s both, bob 2.4s ease-in-out 1.2s infinite}}
.tk{{animation:tick 16s linear infinite}}
.sp{{transform-box:fill-box;transform-origin:center;animation:spin 7s linear infinite}}
.pp{{transform-box:fill-box;transform-origin:center;animation:pop 1.8s ease-in-out infinite}}
.bl{{animation:blink 1s steps(1) infinite}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<defs><clipPath id="c"><rect x="6" y="6" width="964" height="44"/></clipPath></defs>
<rect x="18" y="18" width="964" height="316" fill="#000"/>
<rect x="6" y="6" width="964" height="316" fill="{Y}" stroke="#000" stroke-width="6"/>
<rect x="6" y="6" width="964" height="44" fill="#000"/>
<g clip-path="url(#c)"><g class="tk f" font-size="22" fill="{Y}">
<text x="10" y="36" textLength="1300" lengthAdjust="spacing">{tick*2}</text>
<text x="1310" y="36" textLength="1300" lengthAdjust="spacing">{tick*2}</text></g></g>
<g class="f" font-size="96">
<g class="t1"><text x="47" y="147" textLength="700" lengthAdjust="spacingAndGlyphs" fill="{P}">INTERACTIVE</text>
<text x="40" y="140" textLength="700" lengthAdjust="spacingAndGlyphs" fill="#000">INTERACTIVE</text></g>
<g class="t2"><text x="47" y="239" textLength="700" lengthAdjust="spacingAndGlyphs" fill="{C}" stroke="{C}" stroke-width="1">ACTIVITIES</text>
<text x="40" y="232" textLength="700" lengthAdjust="spacingAndGlyphs" fill="#000">ACTIVITIES</text></g>
</g>
<g transform="translate(40 256)"><rect x="6" y="6" width="400" height="44" fill="#000"/><rect width="400" height="44" fill="#fff" stroke="#000" stroke-width="4"/>
<text class="f" x="16" y="30" font-size="19" fill="#000">PROGRAMMING &amp; AI · YEAR 2 BAC</text>
<rect class="bl" x="366" y="14" width="16" height="16" fill="{P}" stroke="#000" stroke-width="3"/></g>
<g transform="translate(860 110)">
<g class="sp"><rect x="-52" y="-52" width="104" height="104" fill="{L}" stroke="#000" stroke-width="5"/>
<rect x="-52" y="-52" width="104" height="104" fill="{L}" stroke="#000" stroke-width="5" transform="rotate(45)"/></g>
<g class="pp"><rect x="-58" y="-26" width="116" height="52" fill="#000" transform="translate(7 7)"/>
<rect x="-58" y="-26" width="116" height="52" fill="{P}" stroke="#000" stroke-width="4"/>
<text class="f" x="0" y="8" font-size="26" text-anchor="middle" fill="#000">YEAR 2</text></g></g>
<g transform="translate(790 240)"><g class="pp" style="animation-delay:.6s">
<rect x="0" y="0" width="150" height="52" fill="#000" transform="translate(7 7)"/>
<rect x="0" y="0" width="150" height="52" fill="{C}" stroke="#000" stroke-width="4"/>
<text class="f" x="75" y="35" font-size="24" text-anchor="middle" fill="#000">AI + CODE</text></g></g>
</svg>''')

# ---------- MARQUEE TAPES ----------
def tape(name, text, bg, fg, rot, speed, direction=1):
    t = (text+"   ★   ")*4
    L = 1500
    frm,to = (0,-L) if direction==1 else (-L,0)
    w(name, f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 90" width="1000" height="90" role="img" aria-label="{text}">
<style>.f{{{FONT}}}@keyframes m{{from{{transform:translateX({frm}px)}}to{{transform:translateX({to}px)}}}}.m{{animation:m {speed}s linear infinite}}@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style>
<defs><clipPath id="c"><rect x="-30" y="22" width="1060" height="48"/></clipPath></defs>
<g transform="rotate({rot} 500 45)"><rect x="-30" y="28" width="1060" height="48" fill="#000"/>
<rect x="-30" y="22" width="1060" height="48" fill="{bg}" stroke="#000" stroke-width="5"/>
<g clip-path="url(#c)"><g class="m f" font-size="26" fill="{fg}"><text x="0" y="55" textLength="{L}" lengthAdjust="spacing">{t}</text><text x="{L}" y="55" textLength="{L}" lengthAdjust="spacing">{t}</text></g></g></g></svg>''')
tape("tape-1","PROPRIETARY ★ ALL RIGHTS RESERVED ★ AUTHORIZATION REQUIRED",P,"#000",-1.5,18)
tape("tape-2","NOT OPEN SOURCE ★ NO COPYING ★ NO REDISTRIBUTION ★ ASK FIRST",L,"#000",1.5,22,-1)

# ---------- SECTION HEADERS ----------
heads=[("ownership","PROJECT OWNERSHIP",P),("about","ABOUT THE PROJECT",C),("proprietary","PROPRIETARY PROJECT",Y),
("restricted","RESTRICTED ACTIVITIES",P),("ip","INTELLECTUAL PROPERTY",L),("license","STRICT PROPRIETARY LICENSE",C),
("permission","REQUESTING PERMISSION",Y),("credits","DEVELOPMENT &amp; CREDITS",L),("notice","COPYRIGHT NOTICE",P)]
for slug,text,col in heads:
    n=len(text.replace("&amp;","&"))
    tl=min(n*37,760)
    stripes="".join(f'<polygon points="{800+i*48+20},9 {800+i*48+44},9 {800+i*48+24},81 {800+i*48},81" fill="#000"/>' for i in range(8))
    w("h-"+slug, f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 100" width="1000" height="100" role="img" aria-label="{text}">
<style>.f{{{FONT}}}
@keyframes in{{from{{transform:translateX(-50px);opacity:0}}to{{transform:none;opacity:1}}}}
@keyframes st{{from{{transform:translateX(0)}}to{{transform:translateX(-48px)}}}}
@keyframes sh{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(-4px,-4px)}}}}
.a{{animation:in .5s cubic-bezier(.2,1.3,.4,1) both}}.s{{animation:st .8s linear infinite}}.sh{{animation:sh 1.6s ease-in-out infinite}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style>
<defs><clipPath id="c"><rect x="790" y="9" width="186" height="72"/></clipPath></defs>
<g class="a"><rect x="18" y="18" width="976" height="78" fill="#000"/>
<g class="sh"><rect x="6" y="6" width="976" height="78" fill="{col}" stroke="#000" stroke-width="6"/>
<g clip-path="url(#c)"><g class="s">{stripes}</g></g>
<rect x="790" y="6" width="6" height="78" fill="#000"/>
<text class="f" x="30" y="62" font-size="44" textLength="{tl}" lengthAdjust="spacingAndGlyphs" fill="#000">{text}</text></g></g></svg>''')

# ---------- STAMP ----------
w("stamp", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 150" width="560" height="150" role="img" aria-label="This project is not open source">
<style>.f{{{FONT}}}@keyframes shake{{0%,100%{{transform:rotate(-3deg)}}20%{{transform:rotate(2deg) translateX(4px)}}40%{{transform:rotate(-4deg)}}60%{{transform:rotate(3deg) translateX(-4px)}}80%{{transform:rotate(-2deg)}}}}
@keyframes fl{{0%,70%{{fill:{P}}}71%,100%{{fill:{Y}}}}}
.sk{{transform-box:fill-box;transform-origin:center;animation:shake 1.4s ease-in-out infinite}}.fl{{animation:fl 1.4s steps(1) infinite}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style>
<g class="sk"><rect x="30" y="30" width="500" height="100" fill="#000"/><rect class="fl" x="18" y="18" width="500" height="100" stroke="#000" stroke-width="6"/>
<text class="f" x="268" y="62" font-size="30" text-anchor="middle" fill="#000">⛔ THIS PROJECT IS</text>
<text class="f" x="268" y="104" font-size="40" text-anchor="middle" fill="#000" textLength="440" lengthAdjust="spacingAndGlyphs">NOT OPEN SOURCE</text></g></svg>''')

# ---------- FOOTER ----------
w("footer", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 220" width="1000" height="220" role="img" aria-label="Copyright Dr. Walaa El-Masry. Proprietary. All rights reserved.">
<style>.f{{{FONT}}}@keyframes bob{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-8px)}}}}@keyframes spin{{to{{transform:rotate(360deg)}}}}@keyframes bl{{0%,60%{{opacity:1}}61%,100%{{opacity:0}}}}
.b{{animation:bob 2s ease-in-out infinite}}.sp{{transform-box:fill-box;transform-origin:center;animation:spin 6s linear infinite}}.bl{{animation:bl 1s steps(1) infinite}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style>
<rect x="18" y="18" width="976" height="196" fill="#000"/><rect x="6" y="6" width="976" height="196" fill="{L}" stroke="#000" stroke-width="6"/>
<g class="b"><text class="f" x="500" y="85" font-size="54" text-anchor="middle" fill="#000" textLength="760" lengthAdjust="spacingAndGlyphs">© DR. WALAA EL-MASRY</text></g>
<text class="f" x="500" y="125" font-size="22" text-anchor="middle" fill="#000">PROGRAMMING &amp; ARTIFICIAL INTELLIGENCE</text>
<rect x="150" y="142" width="700" height="44" fill="#000"/>
<text class="f" x="500" y="172" font-size="20" text-anchor="middle" fill="{Y}">PROPRIETARY · ALL RIGHTS RESERVED · AUTHORIZATION REQUIRED</text>
<rect class="bl" x="168" y="156" width="16" height="16" fill="{P}"/><rect class="bl" x="816" y="156" width="16" height="16" fill="{P}"/>
<g transform="translate(70 100)"><rect class="sp" x="-26" y="-26" width="52" height="52" fill="{P}" stroke="#000" stroke-width="5"/></g>
<g transform="translate(930 100)"><rect class="sp" x="-26" y="-26" width="52" height="52" fill="{C}" stroke="#000" stroke-width="5"/></g></svg>''')
print(sorted(os.listdir("assets/svg")))
