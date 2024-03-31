from django.shortcuts import render

# Create your views here.

posts =[
        {
            'title': 'Post1',
            'Author': 'Sushma',
            'date_posted': '21-08-2023',
            'content':'Whatever'
            },
        {
            'title': 'Post2',
            'Author' : 'Gireesh',
            'date_posted':'30-03-2024',
            'content':'Belagavi'
            }
        ]
def home(request):
    context ={
            'posts':posts
            }

    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title': "ABOUT PAGE"})

