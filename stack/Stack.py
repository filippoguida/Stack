
#Push interface
p = Push()

#snapshot
for i in range(1, 5):
    blink = random.choice([True, True, False]) # 1:3 chance
    if blink:
        p.fill_screen(char=29)
    else:
        p.fill_screen(rnd=True)
    time.sleep(1/60)

#Clear
p.clear_screen()

#Title
p.print_text("PUSH EXPERIMENTS #1", 0)
p.print_text("- random patterns generator", 1)
p.print_text("click REC to generate new patterns ...", 3)


#Generation
b = Sequence(p)
b.print()
b.get_pattern(1)
#t = Timeline(b)
#t.play()
#p.sendSysex([71, 127, 21, 4, 0, 8, 1, 0, 127, 127, 100, 0, 0, 0])

input()
