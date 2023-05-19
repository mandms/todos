from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from .models import Todos
from rest_framework.permissions import IsAuthenticated
from .serializers import TodosSerializer, TodosDetailSerializer, TodosCreateSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication


class TodosListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        todos = Todos.objects.filter(author=request.user.id).order_by('is_done', '-date')
        serializer = TodosSerializer(todos, many=True)
        return Response(serializer.data)

class TodosDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            todo = Todos.objects.get(id=pk, author=request.user)
        except:
            return Response({'error': "Not found"})
        serializer = TodosDetailSerializer(todo)
        return Response(serializer.data)

class TodosCreateView(generics.CreateAPIView):
    serializer_class = TodosCreateSerializer
    authenticattion_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class TodosDeleteView(APIView):
    def delete(self, request, pk, format=None):
        if Todos.objects.get(id=pk).author == request.user:
            try:
                todo = Todos.objects.get(id=pk)
                todo.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({'error': "Not found"})
        else:
            return Response({'error': "У вас нет прав доступа"})

class TodosUpdateView(generics.UpdateAPIView):
    def get_queryset(self):
        return Todos.objects.filter(author=self.request.user)
    serializer_class = TodosCreateSerializer
    authenticattion_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
