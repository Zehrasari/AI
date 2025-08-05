from django.shortcuts import render
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


@csrf_exempt
def gemini_chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            prompt = data.get("prompt", "")
            
            if not prompt:
                return JsonResponse({"error": "Prompt is required"}, status=400)
            
            # Google Gemini API çağrısı
            genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
            model = genai.GenerativeModel("gemini-2.0-flash")    # Daha yetenekli
            response = model.generate_content(prompt)
            
            if response and hasattr(response, 'text'):
                return JsonResponse({"response": response.text})
            return JsonResponse({"error": "Invalid API response"}, status=500)
            
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
    
    return JsonResponse({"error": "POST method required"}, status=400)


def anasayfa(request):
    return render(request, 'home/anasayfa.html')


def giris(request):
    ctx= {
        'message': 'This is a test page.',
        'title': 'Giriş Page'
    }
    return render(request, 'home/giris.html', ctx)

def baslat(request):
    ctx = {
        'title': 'Başlat',
        'description': 'Bu sayfa uygulamayı başlatmak için kullanılır.'
    }
    return render(request, 'home/baslat.html', ctx)



def elektrik(request):
    ctx = {'title': 'Elektrik', 'description': 'Elektrik mühendisliği içerikleri'}
    return render(request, 'home/elektrik.html', ctx)

def makine(request):
    ctx = {'title': 'Makine', 'description': 'Makine mühendisliği içerikleri'}
    return render(request, 'home/makine.html', ctx)

def bilgisayar(request):
    ctx = {'title': 'Bilgisayar', 'description': 'Bilgisayar mühendisliği içerikleri'} 
    return render(request, 'home/bilgisayar.html', ctx)

def endustri(request):  # Eksikse ekleyin
    ctx = {'title': 'endustri', 'description': 'Endustri mühendisliği içerikleri'}
    return render(request, 'home/endustri.html', ctx)


def hakkimizda(request):
    ctx = {
        'title': 'Hakkımızda',
        'description': 'Bu sayfa hakkında bilgi vermek için kullanılır.'
    }
    import time
    time.sleep(2)  # Simulating a delay for demonstration purposes
    return render(request, 'home/hakkimizda.html', ctx)