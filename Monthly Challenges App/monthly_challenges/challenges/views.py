from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from calendar import month_name

monthly_challenges = {}

challenges = ['eat', 'walk', 'run', 'dance', 
                      'eat', 'walk', 'run', 'dance', 
                      'eat', 'walk', 'run', None]

for month_count in range(0, len(month_name) - 1):
    monthly_challenges[month_name[month_count + 1].lower()] = challenges[month_count]


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    return render(request, 
                    'challenges/index.html',
                    context={
                        "months": months,
                    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month - 1]
        redirect_path = reverse('monthly-challenge', args=[month])
        return render(request, 'challenges/challenge.html')
    except:
        raise Http404()
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        response_data = render(request, 'challenges/challenge.html', 
                                            context={
                                                'challenge': challenge_text,
                                                'month': month,
                                            })
        return HttpResponse(response_data)
    except:
        raise Http404()
    