"""Parametric organizer: pip install cadquery; python desk-organizer/src/build.py"""
import json
from pathlib import Path
import cadquery as cq
ROOT = Path(__file__).resolve().parent.parent
N = json.loads((ROOT / "parameters.json").read_text())["nominal"]
out = ROOT / "models"
out.mkdir(exist_ok=True)
w,d,b = (N[k] for k in ("base_width","base_depth","base_height"))
base = cq.Workplane("XY").box(w,d,b,centered=(False,False,False))
parts = [("Base",base)]
x0,x1=N["divider_x_start"],N["divider_x_end"]
t=N["divider_thickness"]
lean=N["divider_top_rear_offset"]
ys=N["divider_foot_y"]
hs=N["divider_heights_above_base"]
assert len(ys)==len(hs)==N["divider_count"]
assert all(abs(ys[i+1]-ys[i]-t-20)<0.001 for i in range(len(ys)-1))
for i,(y,h) in enumerate(zip(ys,hs),1):
    wall=(cq.Workplane("YZ",origin=(x0,0,0))
          .polyline([(y,b-0.25),(y+t,b-0.25),
                     (y+t+lean,b+h),(y+lean,b+h)])
          .close().extrude(x1-x0))
    parts.append((f"Divider_{i:02}",wall))
outer=N["pen_cup_outer_diameter"]
inner=N["pen_cup_inner_diameter"]
assert outer>inner>0
for i,(x,y) in enumerate(N["pen_cup_centers"],1):
    cup=(cq.Workplane("XY",origin=(x,y,b-0.25))
         .circle(outer/2).circle(inner/2)
         .extrude(N["pen_cup_height_above_base"]+0.25))
    parts.append((f"Pen_holder_{i:02}",cup))
model=base
for _,part in parts[1:]:
    model=model.union(part)
model=model.clean()
assert len(model.solids().vals())==1
cq.exporters.export(model,str(out/"organizer_rev_r.stl"),exportType="STL",tolerance=0.08,angularTolerance=0.12)
assembly=cq.Assembly(name="Organizer_Rev_R")
for name,part in parts:
    assembly.add(part,name=name)
assembly.save(str(out/"organizer_rev_r.step"))
bb=model.val().BoundingBox()
print(f"STL + STEP: {bb.xlen:.1f} x {bb.ylen:.1f} x {bb.zlen:.1f} mm")
