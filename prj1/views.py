from django.http import HttpResponse
from django.shortcuts import render
from .functions import perform_semantic_analysis  # Assuming your functions.py is in the same directory as views.py
from .functions import summarize_text

def homePage(request):
    data= {
        'title': 'Home Page',
        'testimonials':[
            {
                'name': 'John',
                'age': 20,
                'entered_text': "loremipsum",
                'summarized': 'li',
            },
            {
                'name': 'Doe',
                'age': 22,
                'entered_text': "loremipsum",
                'summarized': 'li',
            }
        ]
    }

    if request.method == 'POST':
        text = request.POST.get('text', '')
        summary = summarize_text(text)
        return render(request, 'index.html', {'summary': summary, **data})
    return render(request, 'index.html', data)

def aboutUs(request):
    return render(request, "about_us.html")

def summarize(request):
    summary = ""
    if request.method == 'POST':
        text = request.POST.get('text', '')
        summary = summarize_text(text)
    return render(request, 'summarize.html', {'summary': summary})

def semanticAnalysis(request):
    analysis_result = ""
    if request.method == 'POST':
        text = request.POST.get('text', '')
        analysis_result = perform_semantic_analysis(text)
    return render(request, 'semantic_analysis.html', {'analysis_result': analysis_result})



from django.conf import settings
from gtts import gTTS
import os
import uuid

def convert_text_to_audio(text):
    # Generate a unique filename to avoid overwriting existing files
    unique_filename = f"output_audio_{uuid.uuid4().hex}.mp3"
    audio_file_path = os.path.join(settings.MEDIA_ROOT, unique_filename)  # Ensure output to MEDIA_ROOT

    # Check if the file already exists
    if os.path.exists(audio_file_path):
        # Generate a new unique filename
        unique_filename = f"output_audio_{uuid.uuid4().hex}.mp3"
        audio_file_path = os.path.join(settings.MEDIA_ROOT, unique_filename)

    # Perform text-to-speech conversion and save the audio file
    tts = gTTS(text=text, lang='en')
    tts.save(audio_file_path)

    return audio_file_path


# Example usage in a Django view
from django.shortcuts import render

def textToAudio(request):
    audio_file_url = ""
    if request.method == 'POST':
        text = request.POST.get('text', '')
        audio_file_path = convert_text_to_audio(text)
        audio_file_url = f"{settings.MEDIA_URL}output_audio.mp3"  
    return render(request, 'text_to_audio.html', {'audio_file_url': audio_file_url})


