import yaml
from psychopy import visual, core, event


def show_instructions(win, instruction_text):
    text_stim = visual.TextStim(
        win=win,
        text=instruction_text,
        color='white',
        height=0.05,  # Wysokość liter
        wrapWidth=1.5  # Szerokość zawijania tekstu
    )

    text_stim.draw()
    win.flip()
    core.wait(4.0)
    event.clearEvents(eventType='keyboard')
    event.waitKeys(keyList=['space'])
