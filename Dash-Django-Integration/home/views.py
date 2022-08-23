from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from  home.dash_apps.finished_apps.simpleexample import *
from  home.dash_apps.finished_apps.barchart import *

def home(request):
	return render(request, 'welcome.html')

def index(request):
	return render(request, 'HRDashboard.html')
