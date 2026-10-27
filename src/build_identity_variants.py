import numpy as np, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
PHI=(1+5**0.5)/2; U=64
FD="/usr/share/fonts/truetype/crosextra/"
CB=FD+"Carlito-Bold.ttf"; CR=FD+"Carlito-Regular.ttf"
DL="/usr/share/fonts/truetype/dejavu/DejaVuSans-ExtraLight.ttf"
gap,sx,R=7,4,30

def mark(k,ink,acc,w=8,ss=4):
    K=k*ss; W=int(round(96*K)); H=int(round(60*K))
    im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); u=lambda v:v*K
    d.arc((0,0,u(60)-1,u(60)-1),0,315,fill=ink,width=int(u(w)))
    d.rectangle((u(30),u(30),u(60)-1,u(30+w)),fill=acc)
    x0=60+gap; cx=x0+w+sx; ro=(R+w/2)/2
    d.rectangle((u(x0),0,u(x0+w),H),fill=ink)
    for y0 in (0,30-w/2,60-w): d.rectangle((u(x0),u(y0),u(cx),u(y0+w)),fill=ink)
    for a,b in ((0,2*ro),(60-2*ro,60)):
        d.arc((u(cx-ro),u(a),u(cx+ro)-1,u(b)-1),-90,90,fill=ink,width=int(u(w)))
    return im.resize((int(round(96*k)),int(round(60*k))),Image.LANCZOS)

def flat(W,H,c): return Image.new("RGBA",(W,H),c+(255,))
def fitfont(path,cap):
    f=ImageFont.truetype(path,100); b=f.getbbox("H"); return ImageFont.truetype(path,round(100*cap/(b[3]-b[1])))
def justified(d,txt,f,x,base,width,fill):
    adv=[f.getlength(c) for c in txt]; tr=(width-sum(adv))/(len(txt)-1)
    for c,a in zip(txt,adv): d.text((x,base),c,font=f,fill=fill,anchor="ls"); x+=a+tr
SAFE=0.80*512; K_ICON=SAFE/math.hypot(96,60)

# =============== V4  PAPER (light, editorial, ruler) ===============
PAPER=(243,239,230); INK=(16,19,26); VERM=(229,65,45)
ic=flat(512,512,PAPER); m=mark(K_ICON,INK,VERM); ic.alpha_composite(m,((512-m.width)//2,(512-m.height)//2))
ic.convert("RGB").save("out/v4_paper_icono_512.png",optimize=True)
W,H=4096,2304; hd=flat(W,H,PAPER); ov=Image.new("RGBA",(W*2,H*2),(0,0,0,0)); d=ImageDraw.Draw(ov)
cxr,cyr=3300,1152
for n in range(1,5):
    r=320*PHI**n*2; d.ellipse((cxr*2-r,cyr*2-r,cxr*2+r,cyr*2+r),outline=INK+(60,),width=5)
r=320*PHI**2*2; d.arc((cxr*2-r,cyr*2-r,cxr*2+r,cyr*2+r),235,290,fill=VERM+(255,),width=14)
d.ellipse((cxr*2-U*2,cyr*2-U*2,cxr*2+U*2,cyr*2+U*2),fill=VERM+(255,))
ovr=ov.resize((W,H),Image.LANCZOS)
ramp=np.clip((np.arange(W)-2950)/280,0,1).astype(np.float32)
a=np.array(ovr.getchannel("A"),np.float32)*ramp[None,:]
ovr.putalpha(Image.fromarray(a.astype(np.uint8)))
hd.alpha_composite(ovr); d=ImageDraw.Draw(hd)
for yy in (128,H-128):                       # ruler: tick every 1u, major every 8u
    for i,x in enumerate(range(128,W-127,U)):
        major=(i%8==0); L=44 if major else 16
        d.line((x,yy,x,yy+L if yy<H/2 else yy-L),fill=INK+(190 if major else 90,),width=3)
mk=mark(8,INK,VERM); mx,my=8*U,14*U; hd.alpha_composite(mk,(mx,my))
rx=mx+mk.width+2*U; d.rectangle((rx,my,rx+3,my+mk.height),fill=INK+(255,))
f1=fitfont(CB,180); f2=fitfont(CR,180); tx=rx+2*U
d.text((tx,my+180),"GUILLERMO",font=f1,fill=INK,anchor="ls")
d.text((tx,my+480),"BLANCO",font=f2,fill=VERM,anchor="ls")
hd.convert("RGB").save("out/v4_paper_encabezado_4096x2304.jpg",quality=92,subsampling=0,optimize=True)

# =============== V5  SIGNAL (dark green, generative ridge lines) ===============
BG=(6,18,14); EM=(31,209,139); MINT=(232,255,244); LIME=(200,245,96)
def ridges(W,H,pitch,amp,sc,box,feather,col,seed=3,cx=None):
    ss=2; im=Image.new("RGBA",(W*ss,H*ss),BG+(255,)); d=ImageDraw.Draw(im)
    cx=cx or W/2; xs=np.arange(0,W+1,2.0)
    env=0.18+0.82*(np.abs(xs-cx)/cx)**1.4
    for j,yb in enumerate(np.arange(pitch*1.5,H-pitch,pitch)):
        n=(0.5*np.sin(xs/(180*sc)+j*0.7+seed)+0.3*np.sin(xs/(71*sc)+j*1.9)+0.2*np.sin(xs/(331*sc)+j*0.3))
        ys=yb-amp*env*n
        pts=[(x*ss,y*ss) for x,y in zip(xs,ys)]
        d.polygon(pts+[(W*ss,H*ss),(0,H*ss)],fill=BG+(255,))
        d.line(pts,fill=col+(215,),width=max(2,int(2.2*ss*sc)))
    im=im.resize((W,H),Image.LANCZOS)
    mask=Image.new("L",(W,H),255); ImageDraw.Draw(mask).rectangle(box,fill=0)
    mask=mask.filter(ImageFilter.GaussianBlur(feather))
    base=flat(W,H,BG); base.paste(im,(0,0),mask); return base
ic=ridges(512,512,22,16,0.25,(70,150,442,360),26,EM,cx=256)
m=mark(K_ICON*0.9,MINT,LIME,w=6); ic.alpha_composite(m,((512-m.width)//2,(512-m.height)//2))
ic.convert("RGB").save("out/v5_signal_icono_512.png",optimize=True)
hd=ridges(W,H,36,170,1.0,(1330,600,2766,1700),90,EM)
mk=mark(U*16/96,MINT,LIME,w=5); mx=(W-mk.width)//2; my=11*U; hd.alpha_composite(mk,(mx,my))
d=ImageDraw.Draw(hd); f=fitfont(DL,U)
justified(d,"GUILLERMO BLANCO",f,mx,my+mk.height+3*U,mk.width,MINT+(255,))
hd.convert("RGB").save("out/v5_signal_encabezado_4096x2304.jpg",quality=84,optimize=True)

# =============== V6  TILES (cobalt, modular quarter-circles) ===============
COB=(35,56,245); NAVY=(10,12,36); WHT=(245,243,238); AMB=(255,176,46); SKY=(143,162,255)
ic=flat(512,512,COB); m=mark(K_ICON,WHT,AMB); ic.alpha_composite(m,((512-m.width)//2,(512-m.height)//2))
ic.convert("RGB").save("out/v6_tiles_icono_512.png",optimize=True)
hd=flat(W,H,COB); ss=2; ov=Image.new("RGBA",(W*ss,H*ss),(0,0,0,0)); d=ImageDraw.Draw(ov)
rng=np.random.default_rng(11); s=4*U; cols=W//s; rows=H//s
pal=[NAVY,WHT,AMB,SKY,NAVY,SKY]
for r_ in range(rows):
    for c_ in range(cols):
        e=min(c_,cols-1-c_)
        if e>=5: continue
        if rng.random()>0.97-0.13*e: continue
        col=pal[rng.integers(len(pal))]; x=c_*s*ss; y=r_*s*ss; S=s*ss; t=rng.integers(0,6)
        if t<4:
            cx_,cy_=[(x,y),(x+S,y),(x+S,y+S),(x,y+S)][t]
            d.pieslice((cx_-S,cy_-S,cx_+S,cy_+S),[0,90,180,270][t],[90,180,270,360][t],fill=col+(255,))
        elif t==4: d.ellipse((x+S*0.12,y+S*0.12,x+S*0.88,y+S*0.88),fill=col+(255,))
        else: d.rectangle((x,y,x+S-1,y+S-1),fill=col+(255,))
hd.alpha_composite(ov.resize((W,H),Image.LANCZOS))
mk=mark(U*16/96,WHT,AMB); mx=(W-mk.width)//2; my=11*U
d=ImageDraw.Draw(hd); d.rectangle((mx-2*U,my-2*U,mx+mk.width+2*U,my+mk.height+8*U),fill=COB)
hd.alpha_composite(mk,(mx,my))
f=fitfont(CB,U); justified(d,"GUILLERMO BLANCO",f,mx,my+mk.height+3*U,mk.width,WHT+(255,))
hd.convert("RGB").save("out/v6_tiles_encabezado_4096x2304.jpg",quality=92,subsampling=0,optimize=True)
