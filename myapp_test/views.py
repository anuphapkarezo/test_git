from django.shortcuts import render

# Create your views here.
def go_index(request):
    return render(request, 'index_test.html')