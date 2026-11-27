---
title: "Color Schemes"
date: 2026-03-26
draft: false
---

## draw.io config

The color ramps in the custom-color grid are the nine `ok_*` colormaps, followed by viridis, cividis and twilight,
sampled at nine equally spaced points. The schemes use the colibri palette in sRGB, which is all draw.io knows: the colors
are gamut-mapped from Display P3, a pale scheme has fills at OKLab lightness 0.88 with 40% of the chroma, and the outlines
are the same hue at lightness 0.33 (0.22 for the dark partners).

```json
{"fontCss": "@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,400;0,700;1,400&display=swap');", "customFonts": [{"fontFamily": "Noto Sans", "fontUrl": "https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,400;0,700;1,400&display=swap"}], "defaultFonts": ["Noto Sans", "Helvetica", "Arial", "Times New Roman", "Georgia", "Courier New"], "defaultVertexStyle": {"fontFamily": "Noto Sans", "fontSize": "12", "fontColor": "#000000", "fillColor": "#BADDF5", "strokeColor": "#003A58", "strokeWidth": "1.5", "rounded": "1"}, "defaultEdgeStyle": {"fontFamily": "Noto Sans", "fontSize": "11", "fontColor": "#000000", "strokeColor": "#007CB4", "strokeWidth": "1.5", "edgeStyle": "orthogonalEdgeStyle", "rounded": "0", "jettySize": "auto", "orthogonalLoop": "1"}, "defaultTextStyle": "text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;fontFamily=Noto Sans;fontSize=12;", "presetColors": ["00A050", "E322C5", "4A36EE", "C76314", "007CB4", "B60042", "008177", "7D8C00", "05841C", "A54570", "212A8C", "844D1E", "0045D3", "6C1F1D", "005661", "404900", "B8E5C2", "FFC1EF", "CDD5FF", "F9CDB4", "BADDF5", "FFC7CC", "BCE0DB", "D4DDB3"], "defaultColorSchemes": [[{"title": "Transparent", "fill": "none", "stroke": "#AAAAAA", "font": "#000000"}, {"title": "Pale Emerald", "fill": "#B8E5C2", "stroke": "#00431E", "font": "#000000"}, {"title": "Pale Tourmaline", "fill": "#FFC1EF", "stroke": "#5A004D", "font": "#000000"}, {"title": "Pale Amethyst", "fill": "#CDD5FF", "stroke": "#250095", "font": "#000000"}, {"title": "Pale Amber", "fill": "#F9CDB4", "stroke": "#542400", "font": "#000000"}, {"title": "Pale Sapphire", "fill": "#BADDF5", "stroke": "#003A58", "font": "#000000"}, {"title": "Pale Ruby", "fill": "#FFC7CC", "stroke": "#630020", "font": "#000000"}, {"title": "Pale Grey", "fill": "#E2E2E2", "stroke": "#5F5F5F", "font": "#000000"}], [{"title": "Emerald", "fill": "#00A050", "stroke": "#00431E", "font": "#000000"}, {"title": "Tourmaline", "fill": "#E322C5", "stroke": "#5A004D", "font": "#000000"}, {"title": "Amethyst", "fill": "#4A36EE", "stroke": "#250095", "font": "#FFFFFF"}, {"title": "Amber", "fill": "#C76314", "stroke": "#542400", "font": "#000000"}, {"title": "Sapphire", "fill": "#007CB4", "stroke": "#003A58", "font": "#FFFFFF"}, {"title": "Ruby", "fill": "#B60042", "stroke": "#630020", "font": "#FFFFFF"}, {"title": "Jade", "fill": "#008177", "stroke": "#00403B", "font": "#FFFFFF"}, {"title": "Peridot", "fill": "#7D8C00", "stroke": "#333A00", "font": "#000000"}], [{"title": "Malachite", "fill": "#05841C", "stroke": "#002403", "font": "#FFFFFF"}, {"title": "Rhodolite", "fill": "#A54570", "stroke": "#34001B", "font": "#FFFFFF"}, {"title": "Iolite", "fill": "#212A8C", "stroke": "#080058", "font": "#FFFFFF"}, {"title": "Bronzite", "fill": "#844D1E", "stroke": "#2B1200", "font": "#FFFFFF"}, {"title": "Lapis", "fill": "#0045D3", "stroke": "#00124A", "font": "#FFFFFF"}, {"title": "Garnet", "fill": "#6C1F1D", "stroke": "#370003", "font": "#FFFFFF"}, {"title": "Apatite", "fill": "#005661", "stroke": "#002025", "font": "#FFFFFF"}, {"title": "Serpentine", "fill": "#404900", "stroke": "#191E00", "font": "#FFFFFF"}]], "defaultColors": ["none", "FFFFFF", "F3F3F3", "E2E2E2", "CECECE", "B5B5B5", "959595", "7A7A7A", "5F5F5F", "404040", "1D1D1D", "000000", "0C184E", "140C38", "02193C", "0A1E20", "0A2010", "2D1203", "380406", "240543", "330423", "440154", "00224E", "E2D9E2", "193868", "36186D", "08316A", "19393D", "193C22", "502708", "630D11", "430F76", "5C0C42", "472D7B", "1A386F", "95B5C7", "2C567C", "5E2691", "104997", "275459", "275834", "723C10", "8D171C", "621BA8", "831660", "3B528B", "434E6C", "6276BA", "44728C", "8E31A2", "1A61C3", "366F75", "367446", "935318", "B82128", "7F2ED5", "AB207E", "2C728E", "61656F", "592A8F", "5C8B91", "BB46A5", "337CE6", "478A92", "47915A", "B46A21", "DE393C", "9852EF", "D42F9D", "21918C", "7D7C78", "2F1436", "77A191", "D96CA5", "5D9AF5", "5CA7AF", "5DAE70", "D6842C", "F56560", "AC7DF5", "F057B9", "28AE80", "9B9476", "741E4F", "9BBB91", "EC96B0", "8EB9F8", "7CC4CC", "7CCC8E", "F1A452", "F99890", "C3A5F8", "F98FCD", "5EC962", "BCAE6C", "B25652", "C8D591", "F6C3C9", "BFD7FB", "A7E1E8", "A7E9B4", "FBCC9A", "FBC6C1", "DCCCFB", "FBC2E1", "ADDC30", "DEC958", "CCA389", "FBEF8D", "FEEEEB", "F0F6FE", "E5FAFC", "E6FCE9", "FEF3E7", "FEF2F1", "F6F3FE", "FEF1F8", "FDE725", "FEE838", "E2D9E2"], "colorNames": {"FFFFFF": "White", "F3F3F3": "Grey 10%", "E2E2E2": "Grey 20%", "CECECE": "Grey 30%", "B5B5B5": "Grey 40%", "959595": "Grey 50%", "7A7A7A": "Grey 60%", "5F5F5F": "Grey 70%", "404040": "Grey 80%", "1D1D1D": "Grey 90%", "440154": "viridis 0%", "472D7B": "viridis 12%", "3B528B": "viridis 25%", "2C728E": "viridis 38%", "21918C": "viridis 50%", "28AE80": "viridis 62%", "5EC962": "viridis 75%", "ADDC30": "viridis 88%", "FDE725": "viridis 100%", "00224E": "cividis 0%", "1A386F": "cividis 12%", "434E6C": "cividis 25%", "61656F": "cividis 38%", "7D7C78": "cividis 50%", "9B9476": "cividis 62%", "BCAE6C": "cividis 75%", "DEC958": "cividis 88%", "FEE838": "cividis 100%", "E2D9E2": "twilight 100%", "95B5C7": "twilight 12%", "6276BA": "twilight 25%", "592A8F": "twilight 38%", "2F1436": "twilight 50%", "741E4F": "twilight 62%", "B25652": "twilight 75%", "CCA389": "twilight 88%", "0C184E": "ok_dusk 0%", "193868": "ok_dusk 12%", "2C567C": "ok_dusk 25%", "44728C": "ok_dusk 38%", "5C8B91": "ok_dusk 50%", "77A191": "ok_dusk 62%", "9BBB91": "ok_dusk 75%", "C8D591": "ok_dusk 88%", "FBEF8D": "ok_dusk 100%", "140C38": "ok_orchid 0%", "36186D": "ok_orchid 12%", "5E2691": "ok_orchid 25%", "8E31A2": "ok_orchid 38%", "BB46A5": "ok_orchid 50%", "D96CA5": "ok_orchid 62%", "EC96B0": "ok_orchid 75%", "F6C3C9": "ok_orchid 88%", "FEEEEB": "ok_orchid 100%", "02193C": "ok_blue 0%", "08316A": "ok_blue 12%", "104997": "ok_blue 25%", "1A61C3": "ok_blue 38%", "337CE6": "ok_blue 50%", "5D9AF5": "ok_blue 62%", "8EB9F8": "ok_blue 75%", "BFD7FB": "ok_blue 88%", "F0F6FE": "ok_blue 100%", "0A1E20": "ok_teal 0%", "19393D": "ok_teal 12%", "275459": "ok_teal 25%", "366F75": "ok_teal 38%", "478A92": "ok_teal 50%", "5CA7AF": "ok_teal 62%", "7CC4CC": "ok_teal 75%", "A7E1E8": "ok_teal 88%", "E5FAFC": "ok_teal 100%", "0A2010": "ok_green 0%", "193C22": "ok_green 12%", "275834": "ok_green 25%", "367446": "ok_green 38%", "47915A": "ok_green 50%", "5DAE70": "ok_green 62%", "7CCC8E": "ok_green 75%", "A7E9B4": "ok_green 88%", "E6FCE9": "ok_green 100%", "2D1203": "ok_orange 0%", "502708": "ok_orange 12%", "723C10": "ok_orange 25%", "935318": "ok_orange 38%", "B46A21": "ok_orange 50%", "D6842C": "ok_orange 62%", "F1A452": "ok_orange 75%", "FBCC9A": "ok_orange 88%", "FEF3E7": "ok_orange 100%", "380406": "ok_red 0%", "630D11": "ok_red 12%", "8D171C": "ok_red 25%", "B82128": "ok_red 38%", "DE393C": "ok_red 50%", "F56560": "ok_red 62%", "F99890": "ok_red 75%", "FBC6C1": "ok_red 88%", "FEF2F1": "ok_red 100%", "240543": "ok_purple 0%", "430F76": "ok_purple 12%", "621BA8": "ok_purple 25%", "7F2ED5": "ok_purple 38%", "9852EF": "ok_purple 50%", "AC7DF5": "ok_purple 62%", "C3A5F8": "ok_purple 75%", "DCCCFB": "ok_purple 88%", "F6F3FE": "ok_purple 100%", "330423": "ok_pink 0%", "5C0C42": "ok_pink 12%", "831660": "ok_pink 25%", "AB207E": "ok_pink 38%", "D42F9D": "ok_pink 50%", "F057B9": "ok_pink 62%", "F98FCD": "ok_pink 75%", "FBC2E1": "ok_pink 88%", "FEF1F8": "ok_pink 100%", "1D5E85": "ok6 navy", "C8B222": "ok6 gold", "8B3E09": "ok6 brown", "F487C5": "ok6 pink", "469172": "ok6 green", "A351FB": "ok6 violet", "2A5B88": "ok8 navy", "D6AB1B": "ok8 gold", "8E3B1C": "ok8 rust", "A936FB": "ok8 violet", "4FBC90": "ok8 mint", "F87FD8": "ok8 pink", "228A8F": "ok8 teal", "D0603D": "ok8 coral", "00A050": "colibri emerald", "E322C5": "colibri tourmaline", "4A36EE": "colibri amethyst", "C76314": "colibri amber", "007CB4": "colibri sapphire", "B60042": "colibri ruby", "008177": "colibri jade", "7D8C00": "colibri peridot", "05841C": "colibri-dark malachite", "A54570": "colibri-dark rhodolite", "212A8C": "colibri-dark iolite", "844D1E": "colibri-dark bronzite", "0045D3": "colibri-dark lapis", "6C1F1D": "colibri-dark garnet", "005661": "colibri-dark apatite", "404900": "colibri-dark serpentine", "B8E5C2": "colibri emerald (pale)", "FFC1EF": "colibri tourmaline (pale)", "CDD5FF": "colibri amethyst (pale)", "F9CDB4": "colibri amber (pale)", "BADDF5": "colibri sapphire (pale)", "FFC7CC": "colibri ruby (pale)", "BCE0DB": "colibri jade (pale)", "D4DDB3": "colibri peridot (pale)"}, "defaultGridSize": 10, "defaultEdgeLength": 80, "compressXml": false, "version": "2.4"}
```

A personal reference of colors I use across figures and illustrations. The same palettes, cycles and colormaps are
built into [rhdt-mpl](https://github.com/manuel-rhdt/rhdt-mpl), my Matplotlib defaults. There, every color is
available as `"rhdt:<palette>:<name>"`, e.g. `color="rhdt:colibri:ruby"` or `"rhdt:okabe-ito:sky blue"`, and the
colors of the default palette, colibri, also as `"rhdt:ruby"`. The palette keys are shown next to each heading.

## Palettes and cycles

The default Matplotlib cycle is `colibri`: eight vivid colors named after gems (emerald, tourmaline, amethyst, amber,
sapphire, ruby, jade and peridot), each measured in the plumage of a Colombian hummingbird
([Beltran, Shultz & Parra](https://doi.org/10.5061/dryad.02v6wwq8w)). Every one has at least 3:1 contrast against white, so
they stay visible as thin lines, and the first six are the distinct ones. `colibri-dark` gives each of them a darker partner
of similar hue, for secondary or background series. The numbers of both palettes are Display P3 coordinates, since measured
plumage colors reach outside sRGB; three of them (emerald, sapphire and jade) lie slightly outside even Display P3, so the
hex shown is their nearest P3 color, and the swatches below use the exact color where the browser can show it (on an sRGB
screen they are gamut-mapped). `ok6` and `ok8` are cycles designed in OKLab, ordered so that the first *k* colors are the
most separated; `ok-print` pairs the `ok6`
colors one-to-one with the line styles `-`, `--`, `:`, `-.`, `(0,(5,1,1,1))`, `(0,(1,1))` so that lines remain
distinguishable in greyscale.

{{< color-palette >}}

## Colormaps

256-entry sRGB tables designed in OKLab, all running dark to light (append `_r` for light to dark, the usual direction for
single-hue maps on a white background). `ok_orchid` is the default `image.cmap` in rhdt-mpl. Each bar below interpolates
33 samples of the table; the label gives the OKLab lightness at both ends.

{{< colormaps >}}

## Wide-gamut figures (Display P3)

Everything above is sRGB. Current laptop and phone screens mostly show Display P3, a gamut that is about 25% larger
than sRGB in the CIE 1976 *u′v′* diagram (36% in *xy*), and the greens, cyans and oranges that sRGB cannot reach are
exactly where saturated colormaps live. PDF can hold colors in ICC-based spaces, but Matplotlib has no color
management: all of its colors are just three numbers in [0, 1] that every backend takes as sRGB.

[umbruch-matplotlib](https://github.com/manuel-rhdt/umbruch-matplotlib), my Matplotlib backend that renders figures
to PDF with [umbruch](https://github.com/manuel-rhdt/umbruch), lets a figure say what its numbers mean. The support
for color spaces is in a [pull request](https://github.com/manuel-rhdt/umbruch-matplotlib/pull/3) and not released yet.

```python
import matplotlib
matplotlib.use("module://umbruch_matplotlib")
import umbruch_matplotlib as hb

hb.config.color_space = "display-p3"  # or savefig(..., color_space=...)
ax.plot(x, y, color=(0.0, 1.0, 0.0))  # P3 coordinates: the greenest green
```

From then on every RGB value in the figure is a P3 coordinate. Fills, strokes, text and hatches are written to the PDF
as `color(display-p3 r g b)` straight from Matplotlib's floating-point values (not rounded to 1/255 through hex), and
the pixels of `imshow` get the P3 ICC profile, so a colormap defined in P3 coordinates works too. The other spaces of
CSS Color 4 (`a98-rgb`, `prophoto-rgb`, `rec2020`) are available the same way.

The catch is that everything Matplotlib hands out as sRGB (color names, hex codes, the default cycle, the built-in
colormaps, and the palettes on this page) is then misread as P3 numbers and comes out too saturated. Convert it:

```python
hb.convert_color("#EE7733", "srgb", "display-p3")  # an sRGB color as P3
cmap = hb.convert_cmap("viridis", "srgb", "display-p3")
```

### Examples

The first figure has six saturated P3 colors above the closest colors sRGB can show (the same colors clipped to the
sRGB gamut and written back as P3 numbers), four lines in P3 colors, and two hue wheels: the `hsv` colormap read as P3
numbers on the left, and `hsv` converted from sRGB on the right, which is what it looks like in an sRGB figure.

<img src="/colors/wide_gamut_p3.png" alt="Display P3 figure with swatches, lines and two hue wheels" style="max-width: 100%;">

The second is an `imshow` of the same data with a colormap whose anchors are P3 coordinates (255 of its 256 entries
lie outside sRGB), next to the same colormap clipped to sRGB.

<img src="/colors/wide_gamut_imshow.png" alt="imshow with a Display P3 colormap next to its sRGB clip" style="max-width: 100%;">

<!-- plain <img> from static/: the files are copied unchanged, which keeps the embedded ICC profile -->

These PNGs are previews of the PDFs with the Display P3 profile embedded. In a browser that color-manages images, on a
P3 screen, the left panels and the top rows are visibly more vivid than the right and bottom ones; on an sRGB screen
both look the same, because it clips. A viewer that ignores the profile shows the P3 numbers as sRGB, and the clipped
versions then look washed out. The PDFs are the actual output:
[wide_gamut_p3.pdf](/colors/wide_gamut_p3.pdf) ([script](/colors/wide_gamut_p3.py)) and
[wide_gamut_imshow.pdf](/colors/wide_gamut_imshow.pdf) ([script](/colors/wide_gamut_imshow.py)). The previews come
from [p3_preview.py](/colors/p3_preview.py): poppler renders with the P3 profile as the display profile and the PNG is
tagged with it.

### Limits

- Raster images are 8 bits per channel, as Matplotlib makes them; flat colors are written with five decimals.
- `shading="gouraud"` is not supported in a wide color space yet (umbruch paints meshes in sRGB), and raises.
- Only PDF output is color-managed. Matplotlib's other backends still treat the numbers as sRGB, and I have not
  looked at what happens when such a PDF is converted to CMYK for print.
