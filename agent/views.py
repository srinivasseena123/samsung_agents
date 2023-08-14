from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Agent
from .serializers import AgentSerializer

class AgentList(APIView):
    def get(self, request):
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
