from pymol import cmd

cmd.load("1vfb.pdb")
cmd.set("transparency", "0.3")
cmd.set("surface_quality", "1")

cmd.hide("lines", "all")
cmd.show("cartoon", "all")

cmd.set("cartoon_fancy_helices", 1)
cmd.set("two_sided_lighting", "on")
cmd.set("reflect", 0)
cmd.set("ambient", 0.5)
cmd.set("ray_trace_mode",  3)
cmd.set('''ray_opaque_background''', '''off''')

cmd.set("light_count", "8")
cmd.set("spec_count", "1")
cmd.set("shininess", "10")
cmd.set("specular", "0.25")
cmd.set("ambient", "0")
cmd.set("direct", "0")
cmd.set("reflect", "1.5")
cmd.set("ray_shadow_decay_factor", "0.1")
cmd.set("ray_shadow_decay_range", "2")
cmd.set("antialias", "2")
cmd.set("ray_trace_color", "black")

cmd.show("surface", "chain C")
cmd.color("gray90", "chain C")
cmd.color("blue", "chain B")
cmd.color("skyblue", "chain A")

cmd.select("H1", "chain B and resi 32")
cmd.select("L2", "chain A and resi 50")
cmd.select("H3", "chain B and resi 101")
cmd.select("L3", "chain A and resi 92")

cmd.label("H1 and name CA", '"%s%s" % (chain, resi)')
cmd.label("H3 and name CA", '"%s%s" % (chain, resi)')
cmd.label("L2 and name CA", '"%s%s" % (chain, resi)')
cmd.label("L3 and name CA", '"%s%s" % (chain, resi)')
cmd.set("label_size", "35")
cmd.set("label_color", "black")
cmd.set("label_position", "(0, 0, 40)")
cmd.set("ray_trace_color", "black")

cmd.color("magenta", "H1")
cmd.color("magenta", "L2")
cmd.color("magenta", "H3")
cmd.color("magenta", "L3")

cmd.show("sticks", "H1")
cmd.show("sticks", "H3")
cmd.show("sticks", "L2")
cmd.show("sticks", "L3")

cmd.set_view (\
     '''-0.106774643,    0.854861915,    0.507715821,\
    -0.593984485,   -0.464347214,    0.656918108,\
     0.797331810,   -0.231436923,    0.557359278,\
     0.000078667,   -0.000750449, -164.308609009,\
    40.990982056,   35.819225311,   16.685676575,\
    54.912658691,  272.817779541,  -20.000000000''' )

# cmd.set_view ('''-0.106774643,    0.854861915,    0.507715821,-0.593984485,   -0.464347214,    0.656918108, 0.797331810,   -0.231436923,    0.557359278, 0.000078667,   -0.000750449, -164.308609009, 40.990982056,   35.819225311,   16.685676575, 54.912658691,  272.817779541,  -20.000000000''')

# cmd.png("pre_figs.png", width=400, height=400, dpi=100, ray=3)
# cmd.png("pre_figs.png", width=800, height=800, dpi=600, ray=3)
