from django.shortcuts import render

def index(request):
  forums = Forum.object.all()
  context['forum'] = forums
  return render(request, 'movies/index.html')