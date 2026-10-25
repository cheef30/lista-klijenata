"""Renderuje 'pre/posle' sliku nove naslovne za svaku firmu iz leads JSON-a.
Upotreba: python3 render.py ../danas.json  -> /mnt/user-data/outputs/mockups/<slug>.jpg
"""
import json, sys, os, re, unicodedata, html
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "/mnt/user-data/outputs/mockups"
os.makedirs(OUT, exist_ok=True)
TPL = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()

def slug(s):
    s = unicodedata.normalize("NFKD", s.replace("đ", "dj").replace("Đ", "Dj")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def fill(L, mode):
    e = lambda k: html.escape(str(L.get(k, "")))
    services = "".join(f"<div>{html.escape(s)}</div>" for s in L["services"])
    rep = {
        "__MODE__": mode, "__ACCENT__": L.get("accent", "#F2C230"), "__ON_ACCENT__": L.get("on_accent", "#1E262B"),
        "__STRIPE__": L.get("stripe", "var(--accent)"),
        "__LOGO__": L["logo"], "__NAVCTA__": e("navcta"), "__H1A__": e("h1a"), "__H1B__": e("h1b"),
        "__LEDE__": e("lede"), "__CTA__": e("cta"), "__CTA2__": e("cta2"), "__PHONE__": e("phone_fmt"),
        "__PLATECAP__": e("platecap"), "__RT__": e("rt"), "__REV__": e("rev"), "__QUOTE__": e("quote"),
        "__QBY__": e("qby"), "__SERVICES__": services, "__SIDE__": side(L),
    }
    out = TPL
    for k, v in rep.items():
        out = out.replace(k, v)
    assert "__" not in re.sub(r"<style>.*?</style>", "", out, flags=re.S), "nepopunjen placeholder"
    return out

def side(L):
    e = lambda k: html.escape(str(L.get(k, "")))
    k = L.get("kind", "auto")
    if k == "auto":
        return f'<div class="plate"><div class="eu"><i></i>SRB</div><div class="num">{e("phone_fmt")}</div></div><div class="platecap">{e("platecap")}</div>'
    if k == "pvc":
        return f'<div class="win"><div></div><div></div><i></i></div><div class="wincall">{e("phone_fmt")}<small>{e("platecap")}</small></div>'
    if k == "nekretnine":
        cols = ["#3C5A6E", "#7A6A55", "#5D7356", "#8A5A4E"]
        tiles = "".join(f'<div style="background:{c}">{html.escape(x)}</div>' for x, c in zip(L["tiles"], cols))
        return f'<div class="search"><div><small>Šta tražite</small>{e("s1")}</div><div><small>Lokacija</small>{e("s2")}</div><span>Pretraži</span></div><div class="tiles">{tiles}</div>'
    raise ValueError(k)

def font(sz, bold=True):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p, sz)

def compose(desk, mob, domain, path):
    W, H = 1960, 916
    bg = Image.new("RGB", (W, H), "#C9C6BE")
    # desktop u prozoru browsera
    dw = 1280
    d = desk.resize((dw, int(desk.height * dw / desk.width)), Image.LANCZOS)
    bar = 44
    win = Image.new("RGB", (dw, d.height + bar), "#F7F7F5")
    dr = ImageDraw.Draw(win)
    for i, c in enumerate(["#E26A5A", "#E8B84A", "#6BBF6A"]):
        dr.ellipse((18 + i * 22, 15, 32 + i * 22, 29), fill=c)
    dr.rounded_rectangle((110, 9, dw - 110, 35), 8, fill="#E7E6E2")
    dr.text((130, 14), domain, fill="#4A5258", font=font(15, False))
    win.paste(d, (0, bar))
    mask = Image.new("L", win.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, win.width, win.height), 14, fill=255)
    x0, y0 = (W - 1280 - 80 - 354) // 2, (H - win.height) // 2 - 10
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x0 + 6, y0 + 20, x0 + win.width + 6, y0 + win.height + 20), 16, fill=(40, 40, 40, 90))
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    bg.paste(sh, (0, 0), sh)
    bg.paste(win, (x0, y0), mask)
    # telefon
    mw = 330
    m = mob.resize((mw, int(mob.height * mw / mob.width)), Image.LANCZOS)
    pad = 12
    ph = Image.new("RGB", (mw + 2 * pad, m.height + 2 * pad), "#1E262B")
    pm = Image.new("L", ph.size, 0)
    ImageDraw.Draw(pm).rounded_rectangle((0, 0, ph.width, ph.height), 44, fill=255)
    sm = Image.new("L", m.size, 0)
    ImageDraw.Draw(sm).rounded_rectangle((0, 0, m.width, m.height), 34, fill=255)
    ph.paste(m, (pad, pad), sm)
    px, py = x0 + 1280 + 80, (H - ph.height) // 2 + 10
    sh2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh2).rounded_rectangle((px + 4, py + 18, px + ph.width + 4, py + ph.height + 18), 44, fill=(30, 30, 30, 110))
    sh2 = sh2.filter(ImageFilter.GaussianBlur(16))
    bg.paste(sh2, (0, 0), sh2)
    bg.paste(ph, (px, py), pm)
    bg.save(path, "JPEG", quality=88)

def main(src):
    leads = json.load(open(src, encoding="utf-8"))
    with sync_playwright() as p:
        b = p.chromium.launch()
        for L in leads:
            if not L.get("mock"):
                continue
            s = slug(L["n"])
            shots = {}
            for mode, vp in (("d", (1440, 820)), ("m", (390, 844))):
                f = os.path.join(HERE, f"_{s}_{mode}.html")
                open(f, "w", encoding="utf-8").write(fill(L["mock"], mode))
                pg = b.new_page(viewport={"width": vp[0], "height": vp[1]}, device_scale_factor=2)
                pg.goto("file://" + f)
                pg.wait_for_timeout(400)
                png = os.path.join(HERE, f"_{s}_{mode}.png")
                pg.screenshot(path=png)
                pg.close()
                shots[mode] = Image.open(png).convert("RGB")
            out = os.path.join(OUT, s + ".jpg")
            compose(shots["d"], shots["m"], L["domain"], out)
            L["img"] = out
            print("OK", out)
        b.close()
    json.dump(leads, open(src, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main(sys.argv[1])
