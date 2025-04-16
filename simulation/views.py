from django.shortcuts import render
from .forms import SimulationForm
from .tasks import run_simulation_bg

def index(request):
    if request.method == 'POST':
        form = SimulationForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            count = form.cleaned_data['simulations']
            run_simulation_bg(url, count)
            return render(request, 'simulation/success.html')
    else:
        form = SimulationForm()
    return render(request, 'simulation/index.html', {'form': form})