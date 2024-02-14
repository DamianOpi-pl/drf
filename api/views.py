from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import generics

from api.serializers import BugSerializer
from bugs.models import Bug


class GetBugs(generics.ListAPIView):
    serializer_class = BugSerializer
    queryset = Bug.objects.all()


class BugFilterView(APIView):

    def get(self, *args, **kwargs):
        queryset = Bug.objects.all()

        user_filter = self.request.query_params.get('user_id', None)
        project_filter = self.request.query_params.get('project_id', None)

        if user_filter:
            queryset = queryset.filter(user=user_filter)
        if project_filter:
            queryset = queryset.filter(project=project_filter)

        if queryset:
            serializer = BugSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            raise NotFound()

