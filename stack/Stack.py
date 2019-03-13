from core import Push
from core import Sequence

if __name__ == '__main__':
    #Push interface
    p = Push()
    p.snapshot();

    #Clear
    p.clear_screen()

    #Title
    p.print_text("PUSH EXPERIMENTS #1", 0)
    p.print_text("- random patterns generator", 1)
    p.print_text("click REC to generate new patterns ...", 3)


    #Generation
    b = Sequence(p)
    b.print()
    #b.get_pattern(1)
    #t = Timeline(b)
    #t.play()
    #p.sendSysex([71, 127, 21, 4, 0, 8, 1, 0, 127, 127, 100, 0, 0, 0])

    input()
