from django.shortcuts import render
from home.models import Team
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    user_name = request.user.username
    context = {
        'user_name': user_name
    }
    return render(request, 'home/dashboard.html', context)

def about(request):
    team = Team.objects.all()
    context = {
        'team': team
    }
    return render(request, 'home/about.html', context)
