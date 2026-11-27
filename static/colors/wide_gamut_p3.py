"""A figure in Display P3: every RGB number below is a Display P3 coordinate."""
import numpy as np
import matplotlib

matplotlib.use("module://umbruch_matplotlib")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import umbruch_matplotlib as hb

hb.config.color_space = "display-p3"
hb.config.math_font = "Latin Modern Math"


def clipped_to_srgb(rgb):
    """The same color as the best sRGB can do, written as Display P3 numbers."""
    srgb = hb.convert_color(rgb, "display-p3", "srgb")          # clips to the sRGB gamut
    return hb.convert_color(srgb, "srgb", "display-p3")[:3]


fig, axs = plt.subplots(2, 2, figsize=(11, 7.5), layout="constrained")
fig.suptitle("Display P3 figure: numbers are P3 coordinates", fontsize=15)
fig.set_facecolor((1, 1, 1))

# 1. swatches: the P3 color on top, what sRGB can show of it below -------------------
ax = axs[0, 0]
swatches = {
    "P3 green": (0.0, 1.0, 0.0),
    "P3 red": (1.0, 0.0, 0.0),
    "P3 cyan": (0.0, 0.9, 1.0),
    "P3 magenta": (1.0, 0.0, 0.9),
    "P3 orange": (1.0, 0.45, 0.0),
    "P3 lime": (0.65, 1.0, 0.0),
}
for i, (name, rgb) in enumerate(swatches.items()):
    ax.add_patch(Rectangle((i, 1.05), 0.9, 0.9, color=rgb))
    ax.add_patch(Rectangle((i, 0.05), 0.9, 0.9, color=clipped_to_srgb(rgb)))
    ax.text(i + 0.45, 2.05, name.replace("P3 ", ""), ha="center", fontsize=9)
ax.text(-0.1, 1.5, "P3", ha="right", va="center", fontsize=10)
ax.text(-0.1, 0.5, "sRGB\nclip", ha="right", va="center", fontsize=10)
ax.set_xlim(-0.9, 6)
ax.set_ylim(0, 2.4)
ax.axis("off")
ax.set_title("P3 colors, and their sRGB clip below")

# 2. lines in P3 colors ---------------------------------------------------------------
ax = axs[0, 1]
x = np.linspace(0, 2 * np.pi, 400)
cycle = [(0.0, 1.0, 0.0), (1.0, 0.0, 0.9), (0.0, 0.9, 1.0), (1.0, 0.45, 0.0)]
for k, c in enumerate(cycle):
    ax.plot(x, np.sin(x + k * np.pi / 4), color=c, lw=3,
            label=rf"$\sin(x+{k}\pi/4)$")
ax.set_xlabel(hb.rich("phase <i>x</i> (rad)"))
ax.set_ylabel(hb.rich("<i>y</i>"))
ax.set_title(r"Lines with $P3$ colors", color=(0.1, 0.1, 0.45))
ax.set_ylim(-1.15, 1.95)
ax.legend(frameon=False, loc="upper center", ncols=4, fontsize=8, columnspacing=1.0, handlelength=1.4)
ax.margins(x=0)

# 3. and 4. color wheels: hsv numbers read as P3, and converted from sRGB -------------
yy, xx = np.mgrid[-1:1:600j, -1:1:600j]
hue = (np.arctan2(yy, xx) / (2 * np.pi)) % 1
inside = np.hypot(xx, yy) <= 1
wheel = {"hsv numbers read as P3 (wide)": matplotlib.colormaps["hsv"],
         "the same hsv converted from sRGB": hb.convert_cmap("hsv", "srgb", "display-p3")}
for ax, (title, cmap) in zip(axs[1], wheel.items()):
    rgba = cmap(hue)
    rgba[~inside] = (1, 1, 1, 1)
    ax.imshow(rgba, extent=(-1, 1, -1, 1), interpolation="bilinear")
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")

fig.savefig("wide_gamut_p3.pdf")
