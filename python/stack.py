from stack import Push
from stack import Sequence
from stack import Timeline

if __name__ == '__main__':
    #Push interface
    push = Push()
    push.snapshot();
    push.clear_screen()

    #Title
    push.print_text("PUSH EXPERIMENTS #1", 0)
    push.print_text("- random patterns generator", 1)
    push.print_text("click REC to generate new patterns ...", 3)

    #Generation
    seq = Sequence(push)
    seq.print()
    t = Timeline(push, seq)
    #t.play()
    i = 0
    push.sendSysex([71, 127, 21, 4, 0, 8, 64+i, 0, 127, 127, 100, 0, 0, 0])

    input()
