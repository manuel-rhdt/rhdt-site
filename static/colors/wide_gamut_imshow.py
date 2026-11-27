"""imshow in Display P3: a colormap defined in P3 coordinates, next to its sRGB clip."""
import numpy as np
import matplotlib

matplotlib.use("module://umbruch_matplotlib")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import umbruch_matplotlib as hb

hb.config.color_space = "display-p3"
hb.config.math_font = "Latin Modern Math"

# a colormap whose anchors are Display P3 coordinates (all inside [0, 1], many outside sRGB)
anchors = np.array([(0.00, 0.00, 0.35),    # deep blue
                    (0.00, 0.55, 1.00),    # vivid blue
                    (0.00, 1.00, 0.60),    # saturated green-cyan
                    (0.80, 1.00, 0.00),    # lime
                    (1.00, 0.55, 0.00),    # orange
                    (1.00, 0.00, 0.15)])   # red
t = np.linspace(0, 1, 256)
p3_cmap = ListedColormap(np.stack([np.interp(t, np.linspace(0, 1, len(anchors)), anchors[:, k])
                                   for k in range(3)], axis=1), name="p3_rainbow")
# the same colors as far as sRGB can show them, still written as P3 numbers
srgb_cmap = ListedColormap(
    hb.convert_color(hb.convert_color(p3_cmap.colors, "display-p3", "srgb"), "srgb", "display-p3")[:, :3],
    name="p3_rainbow_srgb_clip")

# data: interfering circular waves
y, x = np.mgrid[-3:3:500j, -4:4:667j]
z = np.cos(5 * np.hypot(x - 1.2, y)) * np.exp(-0.15 * np.hypot(x - 1.2, y) ** 2) \
    + np.cos(5 * np.hypot(x + 1.2, y)) * np.exp(-0.15 * np.hypot(x + 1.2, y) ** 2)

fig, axs = plt.subplots(1, 2, figsize=(11, 4.4), layout="constrained")
fig.suptitle(hb.rich("<b>imshow</b> in Display P3: the colormap is defined in P3 coordinates"), fontsize=13)
for ax, cmap, title in zip(axs, (p3_cmap, srgb_cmap), ("P3 colormap", "the same colormap clipped to sRGB")):
    im = ax.imshow(z, cmap=cmap, extent=(-4, 4, -3, 3), interpolation="bilinear")
    ax.set_title(title)
    ax.set_xlabel(hb.rich("<i>x</i>"))
    ax.set_ylabel(hb.rich("<i>y</i>"))
    cb = fig.colorbar(im, ax=ax, pad=0.02)
    cb.set_label(r"$\cos(5r_1)e^{-r_1^2/6.7}+\cos(5r_2)e^{-r_2^2/6.7}$", fontsize=8)
fig.savefig("wide_gamut_imshow.pdf")
