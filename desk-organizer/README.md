# Desk organizer — Rev R

Parametric desktop organizer for FDM printing (Creality K1).

- Envelope: **200 × 184 × 146.7 mm** (X × Y × Z).
- Seven identical **vertical** dividers, six clear slots of **20 mm** each.
- Divider height above base: **140 mm**; thickness: **5.333 mm**.
- Two pen cups: **24 mm inner / 32 mm outer diameter**, height above base **86.667 mm**.
- Base thickness **6.667 mm**. Phone holder removed.
- Print orientation: flat base on bed, Z up.

## Build

```bash
pip install cadquery
python desk-organizer/src/build.py
```

Edit `parameters.json` to change dimensions. Outputs are `models/organizer_rev_r.stl` and `models/organizer_rev_r.step`. STEP contains named parts; STL is one connected solid.

**Caution:** Dimensions are design assumptions, not physical fit tests. Preview in Creality Print and check adhesion and clearances before printing. The base footprint fits a nominal 220 × 220 mm bed.
