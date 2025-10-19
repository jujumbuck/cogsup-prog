from expyriment import design, control, stimuli, misc
from expyriment.misc.constants import C_WHITE, C_BLACK, K_r, K_b, K_g, K_o
import random

COLORS = ["red", "blue", "green", "orange"]
CUSTOM_COLORS = { "red": (255, 0, 0), "blue": (0, 0, 255),"green": (0, 180, 0),"orange": (255, 140, 0)}

KEYS = [K_r, K_b, K_g, K_o]
COLOR_KEY_MAPPING = {
    "red": K_r,
    "blue": K_b,
    "green": K_g,
    "orange": K_o
}

TRIAL_TYPES = ["match", "mismatch"]
N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16   

# permutations
PERMS = [
    ["blue", "green", "orange", "red"],
    ["green", "orange", "red", "blue"],
    ["orange", "red", "blue", "green"],
    ["red", "blue", "green", "orange"]
]

INSTR_START = """
In this task, name the COLOR the word is written in.
Press R for RED, B for BLUE, G for GREEN, O for ORANGE.

Press SPACE to begin.
"""
INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END =  """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """ correct """
FEEDBACK_INCORRECT = """ incorrect """

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

""" Global settings """
exp = design.Experiment(name="Stroop Balanced", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block', 'trial', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode() 
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

stims = {
    w: {c: stimuli.TextLine(w, text_colour=CUSTOM_COLORS[c]) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])
#feedback_correct = stimuli.TextLine("+", text_colour=(0, 200, 0))
#feedback_incorrect = stimuli.TextLine("x", text_colour=(200, 0, 0))
#load([feedback_correct, feedback_incorrect])

""" Experiment """
def subject_trials(subject_id):
    perm = PERMS[(subject_id - 1) % len(PERMS)]
    base = [{"word": w, "color": w} for w in COLORS] + \
           [{"word": w, "color": c} for w, c in zip(COLORS, perm)]
    block_reps = N_TRIALS_IN_BLOCK // len(base)
    trials = []
    for b_index in range(1, N_BLOCKS + 1):
        block = base * block_reps
        random.shuffle(block)
        for t_index, trial in enumerate(block, 1):
            trial_type = "match" if trial["word"] == trial["color"] else "mismatch"
            correct_key = COLOR_KEY_MAPPING[trial["color"]]
            trials.append({
                "block": b_index,
                "trial": t_index,
                "trial_type": trial_type,
                "word": trial["word"],
                "color": trial["color"],
                "correct_key": correct_key
            })
    return trials


control.start(subject_id=1)
present_instructions(INSTR_START)

trials = subject_trials(exp.subject)

for block_id in range(1, N_BLOCKS + 1):
    block_trials = [t for t in trials if t["block"] == block_id]
    for trial in block_trials:
        stim = stims[trial["word"]][trial["color"]]

        present_for(fixation, t=500)

        stim.present()
        key, rt = exp.keyboard.wait(KEYS)
        correct = key == trial["correct_key"]

        exp.data.add([
            block_id, trial["trial"], trial["trial_type"],
            trial["word"], trial["color"], rt, correct
        ])

        feedback = feedback_correct if correct else feedback_incorrect
        present_for(feedback, t=500)

    if block_id == N_BLOCKS // 2:
        present_instructions(INSTR_MID)

present_instructions(INSTR_END)
control.end()