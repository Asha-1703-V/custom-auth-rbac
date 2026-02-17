from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Role, Resource, Action, Permission
from .serializers import *
from .permissions import CustomRBACPermission


class RoleListCreateView(APIView):
    permission_classes = [CustomRBACPermission]
    admin_resource = 'role'  # для has_permission

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PermissionListCreateView(APIView):
    permission_classes = [CustomRBACPermission]
    admin_resource = 'permission'

    def get(self, request):
        permissions = Permission.objects.all()
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


MOCK_PROJECTS = [{'id': 1, 'name': 'Project Alpha'}, {'id': 2, 'name': 'Project Beta'}]
MOCK_TASKS = [{'id': 1, 'name': 'Task 1', 'project_id': 1}]


class ProjectListView(APIView):
    permission_classes = [CustomRBACPermission]
    resource = 'project'  # для проверки прав

    def get(self, request):
        return Response(MOCK_PROJECTS)

    def post(self, request):  # create
        return Response({'id': 3, 'name': request.data.get('name', 'New Project')}, status=status.HTTP_201_CREATED)


class ProjectDetailView(APIView):
    permission_classes = [CustomRBACPermission]
    resource = 'project'

    def get(self, request, pk):
        project = next((p for p in MOCK_PROJECTS if p['id'] == int(pk)), None)
        if not project: return Response({'error': 'Not found'}, status=404)
        return Response(project)

    def put(self, request, pk):  # update
        return Response({'id': int(pk), 'updated': True})
