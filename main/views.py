from django.shortcuts import render


from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/index.html' )


def services(request):
    return render(request,'main/services.html')


def about(request):
    return render(request,'main/about.html')

def vip(request):
    return render(request,'main/vip.html')