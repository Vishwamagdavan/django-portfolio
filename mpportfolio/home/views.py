from django.shortcuts import render
from home.models import Works

import requests


url = 'https://quotes.rest/qod?category=management'
api_token = "X-TheySaidSo-Api-Secret"
headers = {'content-type': 'application/json',
	   'X-TheySaidSo-Api-Secret': format(api_token)}

# response = requests.get(url, headers=headers)
# #print(response)
# quotes=response.json()['contents']['quotes'][0]
# print(quotes)

# Create your views here.
def works(request):
    works_list=Works.objects.all()
    context={
        'works':works_list,
        # 'quote':quotes['quote'],
        # 'author':quotes['author']
        
    }
    return render(request,'home/index.html',context)
def work_details(request,pk):
    works_list=Works.objects.get(pk=pk)
    context={
        'works':works_list
    }
    return render(request,'home/workdetails.html',context)
def work_list(request):
    works_list=Works.objects.all()
    context={
        'works':works_list,
        # 'quote':quotes['quote'],
        # 'author':quotes['author']
        
    }
    return render(request,'home/work_list.html',context)