import yaml
import time
import random
from psychopy import visual, core, event

from show_instructions import show_instructions
from check_exit import check_for_escape
from procedure_io import save_data
from gui import collect_subject_info
from matrix_generator import create_global_machine_pool, setup_block_machines, get_valid_block_matrix


with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

subject_data = collect_subject_info()

win = visual.Window(fullscr=True, color='black', units='height')
show_instructions(win, config['instrukcja_powitalna'])


win.close()