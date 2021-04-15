from arvore_avl import Leaf

expected_three = [
    '                                                      ______________________________________________________________63_______________________________                                         ',
    '                                                     /                                                                                               \\                                        ',
    '                      ______________________________31_______________________________                                                 ______________79_______________                         ',
    '                     /                                                               \\                                               /                               \\                        ',
    '        ____________15_______________                                 ______________47_______________                         ______71_______                 ______87_______________         ',
    '       /                             \\                               /                               \\                       /               \\               /                       \\        ',
    '    ___7_____                 ______23_______                 ______39_______                 ______55_______             __67___         __75___         __83___             ______95___     ',
    '   /         \\               /               \\               /               \\               /               \\           /       \\       /       \\       /       \\           /           \\    ',
    '  _3_     __11___         __19___         __27___         __35___         __43___         __51___         __59___       65_     69_     73_     77_     81_     85_       __91___       97_   ',
    ' /   \\   /       \\       /       \\       /       \\       /       \\       /       \\       /       \\       /       \\     /   \\   /   \\   /   \\   /   \\   /   \\   /   \\     /       \\     /   \\  ',
    ' 1   5   9_     13_     17_     21_     25_     29_     33_     37_     41_     45_     49_     53_     57_     61_   64  66  68  70  72  74  76  78  80  82  84  86    89_     93_   96  98_ ',
    '/ \\ / \\ /  \\   /   \\   /   \\   /   \\   /   \\   /   \\   /   \\   /   \\   /   \\   /   \\   /   \\   /   \\   /   \\   /   \\                                                   /   \\   /   \\         \\',
    '0 2 4 6 8 10  12  14  16  18  20  22  24  26  28  30  32  34  36  38  40  42  44  46  48  50  52  54  56  58  60  62                                                  88  90  92  94        99'
]

three = Leaf(1)

for i in range(100):
    three.insert(i)

three.display_three()

assert three.get_displayed_three() == expected_three