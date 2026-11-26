# Genera los íconos de Cerón Fotos (rejilla de predios + cámara)
from PIL import Image, ImageDraw
import os
os.makedirs('assets', exist_ok=True); os.makedirs('www', exist_ok=True)
def icon(S):
    im = Image.new('RGBA', (S, S), '#13242e'); d = ImageDraw.Draw(im); u = S / 100
    for i in range(3):
        for j in range(3):
            x = 18 + i * 22; y = 20 + j * 22
            col = '#bfe3ee' if (i + j) % 2 == 0 else '#fbfbf2'
            if (i, j) == (2, 2): col = '#a8551b'
            d.rounded_rectangle([x*u, y*u, (x+18)*u, (y+18)*u], radius=3*u, fill=col)
    d.rounded_rectangle([46*u, 52*u, 90*u, 84*u], radius=6*u, fill='#d6127e')
    d.rounded_rectangle([54*u, 46*u, 68*u, 54*u], radius=2*u, fill='#d6127e')
    d.ellipse([58*u, 58*u, 78*u, 78*u], fill='#13242e'); d.ellipse([62*u, 62*u, 74*u, 74*u], fill='#fbfbf2')
    return im
base = icon(1024)
base.save('assets/icon-only.png')
Image.new('RGBA', (1024, 1024), '#13242e').save('assets/icon-background.png')
fg = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0)); fg.paste(icon(1024).resize((640, 640)), (192, 192)); fg.save('assets/icon-foreground.png')
for s in (192, 512): base.resize((s, s)).convert('RGB').save(f'www/icon-{s}.png')
sp = Image.new('RGB', (2732, 2732), '#13242e'); sp.paste(base.resize((700, 700)).convert('RGB'), (1016, 1016))
sp.save('assets/splash.png'); sp.save('assets/splash-dark.png')
print('íconos listos')
