#!/usr/bin/env python

from pathlib import Path
import re


if __name__ == "__main__":
    PATH_UI: Path = Path("/usr/local/lib/python3.12/site-packages/prefect/server/ui")

    # remove background image
    (PATH_UI / "decorative_iso-pixel-grid_dark.svg").write_text("")
    (PATH_UI / "decorative_iso-pixel-grid_light.svg").write_text("")

    # remove cloud ad on dashboard tab
    for f in (PATH_UI / "assets").rglob("index-*.css"):
        f.write_text(
            f.read_text().replace(
                ".marketing-banner{position",
                ".marketing-banner{visibility:hidden;position"
            )
        )

    # remove cloud ad in sidebar view (.js.map)
    for f in (PATH_UI / "assets").rglob("AppRouterView-*.map"):
        f.write_text(
            re.sub(
                r'\<a href=\\.{1}https\:\/\/www\.prefect\.io\/cloud\-vs\-oss\?.+?(?=\<p\-context\-nav\-item\ title\=\\.{1}Settings)',
                "",
                f.read_text(),
                re.MULTILINE
            )
        )

    # remove cloud ad in a sidebar (.js)
    for f in (PATH_UI / "assets").rglob("AppRouterView-*.js"):
        f.write_text(
            re.sub(
                r"footer:[^\(]*\(\(\)=\>\[(.+\[.{1}onClick.{1}\]\),)",
                re.findall(r"footer:[^\(]*\(\(\)=\>\[", f.read_text())[0],
                f.read_text(),
                re.MULTILINE
            )
        )
