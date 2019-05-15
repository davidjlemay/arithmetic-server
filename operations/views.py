from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.parsers import JSONParser
from operations.models import Question
from serializers import QuestionSerializer

from operations.models import Question
from rest_framework import generics
from operations.serializers import QuestionSerializer

# Custom sign-up view

class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
'''
@ensure_csrf_cookie([''])
def public(request):
  """
  Get question, or create new question.
  """
  if request.method == 'GET':
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def question_save(request):
  if request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = QuestionSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
  return JsonResponse(serializer.errors, status=400)
  '''