from background_task import background
from .playwright_runner import run_simulation

@background(schedule=1)
def run_simulation_bg(url, simulations):
    run_simulation(url, simulations)