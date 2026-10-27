import math
from PIL import Image, ImageDraw, ImageFont
PAPER=(243,239,230); INK=(16,19,26); VERM=(229,65,45); STONE=(94,90,80)
D="/home/claude/ds/project/assets/"
CR="/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf"; CB="/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf"
hx=lambda c:"#%02x%02x%02x"%c
# ---------- SVG marks (96x60 units) ----------
def svg(ink,acc):
    c=30; r=22; R=30; a=math.radians(315)
    ox,oy=c+R*math.cos(a),c+R*math.sin(a); ix,iy=c+r*math.cos(a),c+r*math.sin(a)
    g=f"M60,30 A30,30 0 1 1 {ox:.3f},{oy:.3f} L{ix:.3f},{iy:.3f} A22,22 0 1 0 52,30 Z"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 60" width="960" height="600">
<path d="{g}" fill="{ink}"/>
<rect x="30" y="30" width="30" height="8" fill="{acc}"/>
<rect x="67" y="0" width="8" height="60" fill="{ink}"/>
<rect x="67" y="0" width="12" height="8" fill="{ink}"/><rect x="67" y="26" width="12" height="8" fill="{ink}"/><rect x="67" y="52" width="12" height="8" fill="{ink}"/>
<path d="M79,0 A17,17 0 0 1 79,34 L79,26 A9,9 0 0 0 79,8 Z" fill="{ink}"/>
<path d="M79,26 A17,17 0 0 1 79,60 L79,52 A9,9 0 0 0 79,34 Z" fill="{ink}"/>
</svg>'''
for n,(i,a) in {"gb-mark-primary":(INK,VERM),"gb-mark-reversed":(PAPER,VERM),"gb-mark-mono-ink":(INK,INK),"gb-mark-mono-paper":(PAPER,PAPER)}.items():
    open(D+f"Logos/{n}.svg","w").write(svg(hx(i),hx(a)))
# ---------- PIL mark (same construction) ----------
def mark(k,ink,acc,w=8,ss=4):
    K=k*ss; W=int(round(96*K)); H=int(round(60*K)); im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); u=lambda v:v*K
    d.arc((0,0,u(60)-1,u(60)-1),0,315,fill=ink,width=int(u(w))); d.rectangle((u(30),u(30),u(60)-1,u(30+w)),fill=acc)
    x0=67; cx=79; ro=17
    d.rectangle((u(x0),0,u(x0+w),H),fill=ink)
    for y0 in (0,26,52): d.rectangle((u(x0),u(y0),u(cx),u(y0+w)),fill=ink)
    for a,b in ((0,34),(26,60)): d.arc((u(cx-ro),u(a),u(cx+ro)-1,u(b)-1),-90,90,fill=ink,width=int(u(w)))
    return im.resize((int(round(96*k)),int(round(60*k))),Image.LANCZOS)
def fitfont(path,cap):
    f=ImageFont.truetype(path,100); b=f.getbbox("H"); return ImageFont.truetype(path,round(100*cap/(b[3]-b[1])))
# ---------- horizontal lockups (transparent) ----------
def lockup(ink,acc,name,name2):
    k=10; m=mark(k,ink,acc); mh=m.height  # 960x600
    cap=int(mh*180/480); f1=fitfont(CB,cap); f2=fitfont(CR,cap)
    gapx=int(mh*128/480); tx=m.width+2*gapx
    W=tx+int(f1.getlength("GUILLERMO"))+10; im=Image.new("RGBA",(W,mh),(0,0,0,0)); im.alpha_composite(m,(0,0)); d=ImageDraw.Draw(im)
    d.rectangle((m.width+gapx,0,m.width+gapx+5,mh),fill=ink)
    d.text((tx,cap),"GUILLERMO",font=f1,fill=ink,anchor="ls"); d.text((tx,mh),"BLANCO",font=f2,fill=acc,anchor="ls")
    return im
lockup(INK,VERM,0,0).save(D+"Logos/gb-lockup-horizontal.png",optimize=True)
lockup(PAPER,VERM,0,0).save(D+"Logos/gb-lockup-reversed.png",optimize=True)
# ---------- construction diagram ----------
S=3; k=16*S; PADX,PADY=14*k//1,12*k//1
def canvas(w,h): 
    im=Image.new("RGB",(w*S,h*S),PAPER); return im,ImageDraw.Draw(im)
W,H=1300,820; im,d=canvas(W,H); k=11*S; ox,oy=(W*S-96*k)//2,(H*S-60*k)//2-20*S
f=ImageFont.truetype(CB,14*S); fr=ImageFont.truetype(CR,13*S)
for i in range(0,97,4):    # grid every 4 units
    d.line((ox+i*k,oy-20*S,ox+i*k,oy+60*k+20*S),fill=(214,209,196),width=S)
for j in range(0,61,4): d.line((ox-20*S,oy+j*k,ox+96*k+20*S,oy+j*k),fill=(214,209,196),width=S)
m=mark(k,INK,VERM); im.paste(m,(ox,oy),m)
L=(229,65,45)
def circ(cx,cy,r,col=L,wd=2): d.ellipse((ox+(cx-r)*k,oy+(cy-r)*k,ox+(cx+r)*k,oy+(cy+r)*k),outline=col,width=wd*S)
circ(30,30,30); circ(30,30,22); circ(79,17,17); circ(79,43,17); circ(79,17,9); circ(79,43,9)
d.line((ox,oy+30*k,ox+96*k,oy+30*k),fill=L,width=2*S)
# dimension lines
def dim(x1,y1,x2,y2,txt,off=(0,0)):
    d.line((x1,y1,x2,y2),fill=STONE,width=2*S); 
    for p in ((x1,y1),(x2,y2)): d.ellipse((p[0]-4*S,p[1]-4*S,p[0]+4*S,p[1]+4*S),fill=STONE)
    mx,my=(x1+x2)/2+off[0],(y1+y2)/2+off[1]; d.text((mx,my),txt,font=f,fill=INK,anchor="mm")
dim(ox,oy-26*S,ox+96*k,oy-26*S,"96 u",(0,-18*S))
dim(ox-26*S,oy,ox-26*S,oy+60*k,"60 u",(-32*S,0))
dim(ox+67*k,oy+60*k+28*S,ox+75*k,oy+60*k+28*S,"w = 8 u",(0,22*S))
dim(ox,oy+60*k+28*S,ox+60*k,oy+60*k+28*S,"G Ø 60 u",(0,22*S))
d.text((ox,oy+60*k+80*S),"1 u = 1/60 of mark height.  Stroke 8 u.  G opening 45°.  B bowls overlap into one 8 u bar.",font=fr,fill=STONE)
im.resize((W,H),Image.LANCZOS).save(D+"Diagrams/construction.png",optimize=True)
# ---------- clear space + min sizes ----------
W,H=1300,980; im,d=canvas(W,H); k=8*S; C=15; ox,oy=(W*S-96*k)//2,C*k+30*S
d.rectangle((ox-C*k,oy-C*k,ox+(96+C)*k,oy+(60+C)*k),outline=VERM,width=3*S)
d.rectangle((ox,oy,ox+96*k,oy+60*k),outline=(200,195,182),width=2*S)
m=mark(k,INK,VERM); im.paste(m,(ox,oy),m)
for (x,y) in ((ox-C*k,oy-C*k),(ox+96*k,oy-C*k),(ox-C*k,oy+60*k),(ox+96*k,oy+60*k)):
    d.rectangle((x,y,x+C*k,y+C*k),fill=VERM+(0,) if False else (248,212,205))
d.text((ox-C*k/2,oy-C*k/2),"x",font=ImageFont.truetype(CB,26*S),fill=VERM,anchor="mm")
d.text((W*S/2,oy+(60+C)*k+34*S),"Clear space x = 15 u (a quarter of the mark height) on all four sides.",font=fr,fill=STONE,anchor="mm")
# min sizes
y0=oy+(60+C)*k+90*S; xs=ox
for h in (24,32,48,64):
    mm=mark(h*S/60,INK,VERM); im.paste(mm,(xs,y0+64*S-mm.height),mm); d.text((xs,y0+64*S+14*S),f"{h}px",font=fr,fill=STONE); xs+=mm.width+70*S
im.resize((W,H),Image.LANCZOS).save(D+"Diagrams/clear-space-and-sizes.png",optimize=True)
import shutil
shutil.copy("out/v4_paper_icono_512.png",D+"Google Play/developer-icon-512.png")
shutil.copy("out/v4_paper_encabezado_4096x2304.jpg",D+"Google Play/developer-header-4096x2304.jpg")
shutil.copy(CR,"/home/claude/ds/project/fonts/Carlito-Regular.ttf"); shutil.copy(CB,"/home/claude/ds/project/fonts/Carlito-Bold.ttf")
