from pymol import cmd

cmd.load("2DQE_LHY.pdb")
cmd.load("2DQF_LHY.pdb")
cmd.select("ye", "2DQE_LHY and chain Y")
cmd.select("yf", "2DQF_LHY and chain Y")
cmd.align("ye", "yf")
cmd.hide("everything", "yf")

cmd.set("transparency", "0.2")
#cmd.set("stick_transparency", "0.05")
#cmd.set("surface_quality", "1")

cmd.hide("lines", "all")
cmd.show("cartoon", "all")

cmd.set("cartoon_fancy_helices", 1)
cmd.set("two_sided_lighting", "on")
cmd.set("reflect", 0)
cmd.set("ambient", 0.5)
cmd.set("ray_trace_mode",  3)
cmd.set('''ray_opaque_background''', '''off''')

cmd.set("light_count", "2")
cmd.set("spec_count", "1")
cmd.set("shininess", "10")
cmd.set("specular", "0.25")
cmd.set("ambient", "0")
cmd.set("direct", "0")
cmd.set("reflect", "5")
cmd.set("ray_shadow_decay_factor", "0.1")
cmd.set("ray_shadow_decay_range", "2")
cmd.set("antialias", "2")
cmd.set("ray_trace_color", "black")

#cmd.show("surface", "chain Y")
#cmd.color("gray90", "chain Y")
cmd.color("salmon", "2DQE_LHY")
cmd.color("skyblue", "2DQF_LHY")

cmd.select("mut", "chain H and resi 33")
# cmd.select("H1", "chain H and resi 32 chain H and resi 33")
# cmd.select("L1", "chain L and resi 31 chain L and resi 32")
# cmd.select("H2", "chain H and resi 50 or chain H and resi 53 or chain H and resi 58")
# cmd.select("L2", "chain L and resi 50")
# cmd.select("H3", "chain H and resi 99 or chain H and resi 101")
# cmd.select("L3", "chain L and resi 91 or chain L and resi 92 or chain L and resi 93")

cmd.label("mut and name CA and 2DQE_LHY", '"%s%s" % (chain, resi)')
# cmd.label("H1 and name CA", '"%s%s" % (chain, resi)')
# cmd.label("H2 and name CA", '"%s%s" % (chain, resi)')
# cmd.label("H3 and name CA", '"%s%s" % (chain, resi)')
# cmd.label("L1 and name CA", '"%s%s" % (chain, resi)')
# cmd.label("L2 and name CA", '"%s%s" % (chain, resi)')
# cmd.label("L3 and name CA", '"%s%s" % (chain, resi)')
cmd.set("label_size", "26")
cmd.set("label_color", "black")
cmd.set("label_position", "(7, 1, 20)")
cmd.set("ray_trace_color", "black")

# cmd.color("magenta", "H1")
# cmd.color("magenta", "L1")
# cmd.color("magenta", "H2")
# cmd.color("magenta", "L2")
# cmd.color("magenta", "H3")
# cmd.color("magenta", "L3")

cmd.show("sticks", "mut")
# cmd.show("sticks", "H1")
# cmd.show("sticks", "H2")
# cmd.show("sticks", "H3")
# cmd.show("sticks", "L1")
# cmd.show("sticks", "L2")
# cmd.show("sticks", "L3")

cmd.set_view (\
     '''0.114236899,   -0.171103895,   -0.978586376,\
     0.767809093,   -0.609843850,    0.196264222,\
    -0.630365133,   -0.773798466,    0.061721008,\
    -0.000264835,    0.003553092, -137.779388428,\
    23.296474457,   63.338123322,   43.818073273,\
    97.323280334,  178.525177002,  -20.000000000''' )

#cmd.png("pre_fig5.png", width=800, height=800, dpi=600, ray=3)
#cmd.png("pre_fig5.png", width=800, height=800, dpi=100, ray=3)
