from django.shortcuts import render

students_db = ['오지윤', '이한결', '박찬경', '박찬종', '김주형']
# Create your views here.
def index(request):
    return render(request, 'index.html')

def verify(request):
    if request.method =='POST':
        username = request.POST['username']
        input_time = request.POST['time']
        context = {
                'username' : username,
                'time' : input_time,
                'verify' : False,
        }
        if username in students_db:
           context['verify'] = True
           
    return render(request, 'verify.html', context)