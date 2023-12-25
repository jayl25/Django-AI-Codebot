from django.shortcuts import render
from django.contrib import messages

from dotenv import load_dotenv
import os
from openai import OpenAI

from .models import Code
from django.contrib.auth.decorators import login_required
from django_ai_codebot.constants import programming_languages
# Create your views here.

load_dotenv()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


@login_required
def process_question(request, template_name):
    if request.method == "POST":
        title = request.POST['title']
        code = request.POST['code']
        lang = request.POST['lang']

        context = {
            "languages": programming_languages,
            "code": code,
            "lang": lang,
            "title": title,
        }

        if lang == "Select Programming Language":
            messages.warning(request, "Hey, you forgot to pick a programming language!")
            return render(request, template_name, context)
        else:
            client = OpenAI()
            try:
                completer = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "user", "content": f"Reply with {lang} code only: {code}. Fix this code. Add no comments"},
                    ]
                )
                context.update({"response": completer.choices[0].message.content})
                record = Code(title=title, question=code, code_answer=completer.choices[0].message.content, language=lang, user=request.user)
                record.save()
            except Exception as e:
                context.update({"response": f"Error: {str(e)}"})

        return render(request, template_name, context)
    else:
        context = {
            "languages": programming_languages
        }
        return render(request, template_name, context)

@login_required
def home(request):
    return process_question(request, "home.html")

@login_required
def ask(request):
    return process_question(request, "ask.html")

@login_required
def previously_asked(request):
    queries = Code.objects.filter(user_id=request.user.id)    
    return render(request, 'previously_asked.html', {"queries": queries})