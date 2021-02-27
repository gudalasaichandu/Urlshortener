from django.shortcuts import redirect
from rest_framework.response import Response
from .models import url
from .serializers import url_serializer
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
import random
import string
hash_set=set()

@api_view(['GET'])
def geturl(request):
    shorted = request.query_params.get('short_hash')
    #print(shorted, "shorted value")
    try:
        req_url = url.objects.get(short_hash=shorted)
        req_url.count = req_url.count + 1
        req_url.save()
        #serializer = url_serializer(req_url)
        ans = req_url.long_url
        print(ans)
        return redirect(ans)
    except Exception as e:
        print(e)
        return HttpResponse(e)
        #return JsonResponse({"message": "Requested URL not found"})

@api_view(['POST'])
def posturl(request):
    if request.method=='POST':
        long_url = request.POST.get('long_url')

        ## to check if url already exists in db
        l_url = url.objects.filter(long_url=long_url)
        if l_url:
            l_url = url.objects.get(long_url=long_url)
            a=l_url.short_hash
            print(a)
            ans1 = 'http://localhost:8000/a/?short_hash=' + a
            return Response(ans1)
        ##
        #short_hash = 'hacodd2eerf4343' # static hash to test
        letters = string.ascii_letters
        while True:
            short_hash = ''.join(random.choice(letters) for i in range(8))
            if short_hash not in hash_set: # to check hash is already present or not, if present regenerate new hash
                break
        hash_set.add(short_hash)

        count = 0
        myurl=url(long_url=long_url,short_hash=short_hash,count=count,)
        myurl.save()
        ans = 'http://localhost:8000/a/?short_hash=' + short_hash
        return Response(ans)


@api_view(['GET'])
def history(request):
    data1=url.objects.order_by('-created_at')[:5] # top 5 latest urls generated
    print(data1)
    serializer = url_serializer (data1,many=True)
    return Response(serializer.data)