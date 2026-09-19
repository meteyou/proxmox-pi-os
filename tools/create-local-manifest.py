#!/usr/bin/env python3
"""Create a Raspberry Pi Imager manifest pointing at the image in this folder.

Run this script next to the downloaded `*.img.xz` and `*.rpi-imager.json`:

    python3 create-local-manifest.py

It writes `*.rpi-imager-local.json` with the absolute path of the image in
this folder. Load that file in Raspberry Pi Imager via
App Options -> Content Repository -> EDIT -> Use custom file, or start Imager
with `rpi-imager --repo /path/to/<image>.rpi-imager-local.json`.
"""

import json
import pathlib
import sys
import urllib.parse

here = pathlib.Path(__file__).resolve().parent
manifests = sorted(here.glob("*.rpi-imager.json"))

if not manifests:
    sys.exit(f"no *.rpi-imager.json found in {here}")

for manifest in manifests:
    data = json.loads(manifest.read_text())

    for entry in data.get("os_list", []):
        image_name = urllib.parse.urlparse(entry["url"]).path.rsplit("/", 1)[-1]
        image = here / image_name
        if not image.is_file():
            print(f"skipping {manifest.name}: {image_name} not found in {here}")
            break
        entry["url"] = image.as_uri()
    else:
        out = manifest.with_name(manifest.name.replace(".rpi-imager.json", ".rpi-imager-local.json"))
        out.write_text(json.dumps(data, indent=2) + "\n")
        print(f"wrote {out}")
        print("Load it in Raspberry Pi Imager: App Options -> Content Repository -> EDIT -> Use custom file")
        print(f"or run: rpi-imager --repo \"{out}\"")
