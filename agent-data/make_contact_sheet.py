from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

frames_dir = Path('/home/ubuntu/x_jarvis_analysis/frames')
paths = sorted(frames_dir.glob('frame_*.jpg'))
thumb_w, thumb_h = 180, 320
cols = 4
rows = (len(paths) + cols - 1) // cols
sheet = Image.new('RGB', (cols * thumb_w, rows * (thumb_h + 28)), 'white')
draw = ImageDraw.Draw(sheet)
for idx, p in enumerate(paths):
    img = Image.open(p).convert('RGB')
    img.thumbnail((thumb_w, thumb_h))
    x = (idx % cols) * thumb_w + (thumb_w - img.width) // 2
    y = (idx // cols) * (thumb_h + 28)
    sheet.paste(img, (x, y))
    draw.text(((idx % cols) * thumb_w + 6, y + img.height + 4), p.name, fill=(0,0,0))
out = Path('/home/ubuntu/x_jarvis_analysis/contact_sheet.jpg')
sheet.save(out, quality=95)
print(out)
