from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context)

def p1(request):
    return HttpResponse("Test for the poll number 1")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
    
def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

def owner(request: HttpRequest) -> HttpResponse:
        return HttpResponse(f"Hello, world. 87ddea98 is the polls index.")