from PIL import Image, ImageDraw, ImageFont
from math import sin,cos,pi
from pathlib import Path
P=Path(__file__).parent/'assets';P.mkdir(exist_ok=True)
fontserif='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
fontsans='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
fontbold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(path,size): return ImageFont.truetype(path,size)

def canvas(w,h,og=False):
    im=Image.new('RGB',(w,h),'#fff6eb');d=ImageDraw.Draw(im)
    # layered shapes on the left; no avatar conflict on LinkedIn
    for rad,col,dx,dy in [(440,'#ffcb9d',-70,-110),(350,'#f5a688',10,-80),(260,'#ffd8a0',100,-50),(190,'#e3eecf',160,15)]:
        x=w*.15+dx;y=h*.52+dy
        d.ellipse((x-rad/2,y-rad/2,x+rad/2,y+rad/2),fill=col)
    for n in range(26):
        a=2*pi*n/26
        x=w*.16+220*cos(a);y=h*.5+142*sin(a)
        d.ellipse((x-3,y-3,x+3,y+3),fill='#ffffff')
    d.rounded_rectangle((round(w*.07),round(h*.42),round(w*.28),round(h*.60)),radius=30,fill='#fffaf3')
    d.text((round(w*.105),round(h*.45)),'MAKE IT WORK.',font=font(fontbold,20 if not og else 18),fill='#24574d')
    # accent angular marks
    for x,y,s,col in [(w*.32,h*.2,18,'#d86641'),(w*.41,h*.72,13,'#2c826d'),(w*.09,h*.85,14,'#ffffff')]:
        d.line((x-s,y,x+s,y),fill=col,width=4);d.line((x,y-s,x,y+s),fill=col,width=4)
    start=int(w*.43) if not og else int(w*.44)
    d.text((start,int(h*.20)),'MARKO DAKIĆ',font=font(fontserif,int(h*.19)),fill='#173d36')
    d.text((start,int(h*.53)),'PRODUCT  ·  DELIVERY  ·  eCOMMERCE',font=font(fontbold,int(h*.063)),fill='#b75d43')
    d.text((start,int(h*.72)),'Turning complexity into things that work.',font=font(fontsans,int(h*.050)),fill='#596c62')
    return im
canvas(1584,396).save(P/'linkedin-banner-v2.png',optimize=True)
canvas(1200,630,True).save(P/'og-card.png',optimize=True)
print('created graphics')
