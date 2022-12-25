from django.shortcuts import render,redirect
from .models import TinyVideo
from django.contrib import messages

# Create your views here.
def Home(request):
    tinyvideos = TinyVideo.objects.all().order_by('-Time')
    return render(request, 'index.html', {'tinyvideos':tinyvideos})

def AddVideo(request):
    if request.method == 'POST':
        TinyVideo_Tittle = request.POST.get('TinyVideo_Tittle')
        TinyVideo_Video = request.FILES.get('TinyVideo_Video')

        SavingVideo = TinyVideo(TinyVideo_Tittle=TinyVideo_Tittle, TinyVideo_Video = TinyVideo_Video)

        SavingVideo.save()

        messages.success(request, 'Your Video has been uploaded successfully')

        return redirect('home')

    return render(request, 'addvideo.html')
