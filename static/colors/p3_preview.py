"""PNG previews of the PDFs, in Display P3 pixel values with the profile embedded:
poppler renders with the P3 profile as display profile, and the PNG is tagged so that a
color-managed viewer (any current browser) shows the wide-gamut colors on a P3 screen."""
import subprocess
import sys

import umbruch_matplotlib as hb
from PIL import Image

profile = hb._icc_profile("display-p3")
open("display-p3.icc", "wb").write(profile)
for name in sys.argv[1:]:
    subprocess.run(["pdftoppm", "-r", "110", "-displayprofile", "display-p3.icc", "-png",
                    "-singlefile", f"{name}.pdf", name], check=True)
    Image.open(f"{name}.png").convert("RGB").save(f"{name}.png", icc_profile=profile, optimize=True)
