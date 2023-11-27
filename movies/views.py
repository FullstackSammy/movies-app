from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies': [
            'Lord of The Rings',
            'Gladiator',
            'Harry Potter and The Half Blood Prince',
            'Deadpool',
            'The Silence of The Lambs',
            'Avatar: Way of Water',
            'The Internship',
        ],
        'tvseries': [
            'Friends',
            'TVD',
            'The walking dead',
            'Charmed',
        ]
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {})

#app/templates/app/index.html
#movies/templates/movies/index.html