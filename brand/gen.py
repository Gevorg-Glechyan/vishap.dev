"""Generate every vishap brand SVG into project/assets/. Regenerate, don't hand-edit.
Usage: python gen.py <SchibstedGrotesk[wght].ttf>   (needs fontTools; font is SIL OFL 1.1)
"""
import os, sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

INK, WHITE = "#1C1E26", "#FFFFFF"
# The carpet palette: madder field, indigo medallion, undyed wool, ochre detail.
MADDER, INDIGO, WOOL, OCHRE, ROSE = "#B0301F", "#1F2A5A", "#F4ECDD", "#D9A036", "#C9604B"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "project", "assets")

# The mark: a capital V that is a dragon, drawn the way vishap carpets draw theirs.
# Left arm = tail with a serrated spine, right arm = neck and horned head, slit eye.
# V sits on a 64 grid: arm tops at y=14, apex (baseline) at y=54, so cap height = 40.
# The outer edge of the tail is serrated with three notches, then runs straight to the pointed tip.
BODY = ("M3 11L21.5 18.2L30 32.3L41 14L34.5 3L46 10L61.5 13.2L62 19.2L50.6 19.7L30 54"
        "L26.87 49.01L26.97 41.28L23.41 43.51L20.75 39.26L20.85 31.53L17.29 33.76"
        "L14.63 29.52L14.73 21.79L11.17 24.02L8.53 19.75Z")
EYE = "M46.3 13.2L53 14.8L47.2 16.9Z"
MARK = BODY + EYE  # fill-rule evenodd cuts the eye out
CX, CY = 32.5, 28.5  # centre of the mark's bounds (x 3..62, y 3..54)


def write(group, name, body, viewbox):
    os.makedirs(os.path.join(OUT, group), exist_ok=True)
    with open(os.path.join(OUT, group, name), "w", encoding="utf-8") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}">{body}</svg>\n')


def mark(fill, transform=""):
    t = f' transform="{transform}"' if transform else ""
    return f'<path{t} fill="{fill}" fill-rule="evenodd" d="{MARK}"/>'


def tile(bg, fg, rx=14, scale=0.66, border=True):
    """App icon: a small rug. Field colour, the dragon, and one border line."""
    line = f'<rect x="4.5" y="4.5" width="55" height="55" rx="{max(rx - 4, 0)}" fill="none" stroke="{fg}" stroke-width="1.4"/>' if border else ""
    return (f'<rect width="64" height="64" rx="{rx}" fill="{bg}"/>' + line
            + mark(fg, f"translate(32 32.5) scale({scale}) translate({-CX} {-CY})"))


# ---- wordmark: the mark replaces the V, then ISHAP outlined from Schibsted Grotesk
def instance(path, wght):
    return instantiateVariableFont(TTFont(path), {"wght": wght})


def outline(font, text, x, baseline, cap, tracking=0.0):
    """Outlined text with its cap height scaled to `cap` units. Returns (path data, end x)."""
    gs, cmap = font.getGlyphSet(), font.getBestCmap()
    s = cap / font["OS/2"].sCapHeight
    d = ""
    for ch in text:
        g = gs[cmap[ord(ch)]]
        pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
        g.draw(TransformPen(pen, (s, 0, 0, -s, x, baseline)))
        d += pen.getCommands()
        x += g.width * s + tracking * font["head"].unitsPerEm * s
    return d, x - tracking * font["head"].unitsPerEm * s


def logos(font_path):
    heavy, medium = instance(font_path, 800), instance(font_path, 500)
    G, sq = "Logos", "0.5 -3.5 64 64"
    write(G, "vishap-mark.svg", mark(MADDER), sq)
    write(G, "vishap-mark-ink.svg", mark(INK), sq)
    write(G, "vishap-mark-wool.svg", mark(WOOL), sq)
    write(G, "vishap-icon.svg", tile(MADDER, WOOL), "0 0 64 64")
    write(G, "vishap-icon-indigo.svg", tile(INDIGO, WOOL), "0 0 64 64")
    write(G, "vishap-icon-square.svg", tile(MADDER, WOOL, rx=0, scale=0.56, border=False), "0 0 64 64")
    write(G, "vishap-favicon.svg", tile(MADDER, WOOL, scale=0.8, border=False), "0 0 64 64")

    letters, end = outline(heavy, "ISHAP", 66, 54, 40, tracking=0.06)
    word = lambda m, c: mark(m) + f'<path fill="{c}" d="{letters}"/>'
    vb = f"1 1 {end:.1f} 55"
    write(G, "vishap-wordmark.svg", word(MADDER, INK), vb)
    write(G, "vishap-wordmark-ink.svg", word(INK, INK), vb)
    write(G, "vishap-wordmark-wool.svg", word(WOOL, WOOL), vb)
    write(G, "vishap-wordmark-on-madder.svg",
          f'<rect x="-15" y="-15" width="{end + 32:.1f}" height="87" fill="{MADDER}"/>' + word(WOOL, WOOL),
          f"-15 -15 {end + 32:.1f} 87")

    full, w = outline(heavy, "VISHAP", 0, 0, 13, tracking=0.14)
    write(G, "vishap-stacked.svg",
          mark(MADDER, f"translate({w / 2 - CX:.2f} 0)") + f'<path transform="translate(0 78)" fill="{INK}" d="{full}"/>',
          f"-4 0 {w + 8:.1f} 82")

    by, bx = outline(medium, "by", 0, 54, 18)
    sig, send = outline(heavy, "ISHAP", bx + 9 + 66, 54, 40, tracking=0.06)
    write(G, "vishap-signature.svg",
          f'<path fill="#5B6172" d="{by}"/>' + mark(MADDER, f"translate({bx + 9:.2f} 0)") + f'<path fill="{INK}" d="{sig}"/>',
          f"-1 1 {send + 3:.1f} 62")


# ---- product icons: colour tile, sharp white line glyph, solid triangles for the subject
PRODUCTS = {  # name: (colour, glyph lines, solid triangles)
    # a frame, and the view being captured: two peaks, Sis and Masis
    "screenshot-capture-studio": ("#0F6B63", "M16 27V16H27M37 16H48V27M48 37V48H37M27 48H16V37",
                                  "M19.5 40.5L25.5 33.5L28.6 37.1L35 26.5L44.5 40.5Z"),
    # a bar chart, and a pointer on the bar being inspected
    "posthog-debugger": ("#2447B8", "M20 46V37M32 46V29M44 46V34", "M26 14H38L32 20Z"),
    # a window, and the corner you drag
    "window-resize-manager": ("#5B2DB0", "M48 32V18H16V46H34M16 27H48", "M50.25 37V48.25H39Z"),
}


def glyph(name):
    _, lines, wedge = PRODUCTS[name]
    return (f'<path d="{lines}" fill="none" stroke="{WHITE}" stroke-width="4.5" stroke-linecap="square" stroke-linejoin="miter"/>'
            f'<path d="{wedge}" fill="{WHITE}"/>')


def products():
    for name, (color, _, _) in PRODUCTS.items():
        write("Product-icons", name + ".svg", f'<rect width="64" height="64" rx="14" fill="{color}"/>' + glyph(name), "0 0 64 64")


# ---- illustrations: flat 2D, in the vocabulary of vishap carpets.
# A coloured field with one border line, medallions, diamonds, stars and the dragon.
def poly(points, fill):
    return f'<path fill="{fill}" d="M' + "L".join(f"{x:.1f} {y:.1f}" for x, y in points) + 'Z"/>'


def rect(x, y, w, h, fill):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'


def diamond(cx, cy, r, fill, ry=None):
    ry = ry or r
    return poly([(cx, cy - ry), (cx + r, cy), (cx, cy + ry), (cx - r, cy)], fill)


def octagon(cx, cy, r, fill, stroke=None):
    k = r * 0.42
    pts = [(cx - k, cy - r), (cx + k, cy - r), (cx + r, cy - k), (cx + r, cy + k),
           (cx + k, cy + r), (cx - k, cy + r), (cx - r, cy + k), (cx - r, cy - k)]
    if stroke:
        return f'<path fill="none" stroke="{stroke}" stroke-width="2.5" d="M' + "L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + 'Z"/>'
    return poly(pts, fill)


def star(cx, cy, r, fill):
    """Eight points: a square over a diamond."""
    q = r * 0.72
    return rect(cx - q, cy - q, 2 * q, 2 * q, fill) + diamond(cx, cy, r, fill)


def dragon(cx, cy, s, fill=WOOL, flip=False):
    sx = -s if flip else s
    return mark(fill, f"translate({cx} {cy}) scale({sx} {s}) translate({-CX} {-CY})")


def water(x, y, w, fill=WOOL, step=16, amp=7):
    """Running water: one zigzag line, as in a rug border."""
    pts, i = [], 0
    while i * step <= w:
        pts.append(f"{x + i * step:.0f} {y + (amp if i % 2 else 0):.0f}"); i += 1
    return f'<path fill="none" stroke="{fill}" stroke-width="2.5" stroke-linejoin="miter" d="M' + "L".join(pts) + '"/>'


def field(w, h, color, line=WOOL, inset=12):
    """The ground of every picture: one flat colour and one border line."""
    return rect(0, 0, w, h, color) + (f'<rect x="{inset}" y="{inset}" width="{w - 2 * inset}" height="{h - 2 * inset}" '
                                      f'fill="none" stroke="{line}" stroke-width="2.5"/>')


def corners(w, h, fill=OCHRE, d=30, r=6):
    return "".join(diamond(x, y, r, fill) for x in (d, w - d) for y in (d, h - d))


def medallion(name, cx=160, cy=172, r=88):
    """A product as a medallion: its colour, with its icon glyph at double size."""
    return (octagon(cx, cy, r, PRODUCTS[name][0]) + octagon(cx, cy, r - 9, None, WOOL)
            + f'<g transform="translate({cx - 64} {cy - 64}) scale(2)">{glyph(name)}</g>')


def illustrations():
    G, V = "Illustrations", "0 0 320 320"

    # hero: two dragons guard a star, the classic dragon-carpet arrangement
    h = field(960, 400, MADDER, inset=16)
    h += "".join(diamond(x, y, 5, OCHRE) for y in (36, 364) for x in range(56, 920, 44))
    h += octagon(480, 196, 128, INDIGO) + octagon(480, 196, 116, None, WOOL) + star(480, 196, 56, OCHRE) + diamond(480, 196, 16, INDIGO)
    h += dragon(232, 200, 3.1) + dragon(728, 200, 3.1, flip=True)
    h += "".join(diamond(x, y, 9, INDIGO) + diamond(x, y, 3.5, WOOL) for x in (92, 868) for y in (112, 288))
    h += water(360, 348, 240)
    write(G, "hero-dragons.svg", h, "0 0 960 400")

    # principles
    one = field(320, 320, INDIGO) + corners(320, 320) + octagon(160, 160, 92, MADDER) + octagon(160, 160, 82, None, WOOL)
    one += star(160, 160, 36, OCHRE) + diamond(160, 160, 9, MADDER)
    write(G, "one-job.svg", one, V)

    hid = field(320, 320, MADDER) + corners(320, 320) + dragon(160, 102, 2.1)
    hid += f'<g transform="translate(0 320) scale(1 -1)">{dragon(160, 102, 2.1, ROSE)}</g>' + water(48, 156, 224)
    write(G, "nothing-hidden.svg", hid, V)

    kept = field(320, 320, INDIGO) + corners(320, 320) + octagon(160, 186, 76, None, WOOL) + diamond(160, 186, 30, OCHRE) + diamond(160, 186, 10, INDIGO)
    kept += dragon(110, 66, 1.3) + dragon(210, 66, 1.3, flip=True)
    write(G, "kept-inside.svg", kept, V)

    # one per product: the tool as the medallion, the dragon above it
    for name in PRODUCTS:
        pic = field(320, 320, INDIGO) + corners(320, 320) + dragon(160, 50, 1.05) + medallion(name)
        pic += diamond(40, 172, 7, OCHRE) + diamond(280, 172, 7, OCHRE) + water(104, 280, 112)
        write(G, f"product-{name}.svg", pic, V)

    # states
    empty = field(320, 320, MADDER) + corners(320, 320) + octagon(160, 160, 84, None, ROSE) + diamond(160, 160, 8, WOOL)
    write(G, "state-empty.svg", empty, V)

    lost = field(320, 320, INDIGO) + corners(320, 320) + dragon(160, 118, 2.1, flip=True)
    lost += "".join(diamond(x, 236, 12, OCHRE) for x in (64, 112, 160, 256))
    lost += f'<path fill="none" stroke="{OCHRE}" stroke-width="2.5" d="M208 224L220 236L208 248L196 236Z"/>'
    write(G, "state-not-found.svg", lost, V)

    done = field(320, 320, MADDER) + corners(320, 320) + star(160, 112, 44, OCHRE) + diamond(160, 112, 12, MADDER)
    done += dragon(160, 222, 1.9) + diamond(56, 112, 7, WOOL) + diamond(264, 112, 7, WOOL)
    write(G, "state-done.svg", done, V)

    # store promo tile, 440 x 280: the product colour as the field
    name = "window-resize-manager"
    promo = field(440, 280, PRODUCTS[name][0]) + corners(440, 280, WOOL)
    promo += f'<g transform="translate(52 44) scale(3)">{glyph(name)}</g>' + dragon(336, 150, 1.9)
    write(G, "store-tile-window-resize-manager.svg", promo, "0 0 440 280")


if __name__ == "__main__":
    logos(sys.argv[1]); products(); illustrations()
    for root, _, files in os.walk(OUT):
        for f in sorted(files):
            p = os.path.join(root, f)
            print(f"{os.path.getsize(p):6d}  {os.path.relpath(p, OUT)}")
