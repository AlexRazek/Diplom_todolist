from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from goals.filters import GoalDateFilter
from goals.models import Goal
from goals.permissionts import GoalPermissions
from goals.serializers import GoalCreateSerializer, GoalSerializer


class GoalCreateView(CreateAPIView):
    model = Goal
    permission_classes = [GoalPermissions]
    serializer_class = GoalCreateSerializer


class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [GoalPermissions]

    def get_queryset(self):
        return Goal.objects.filter(category__board__participants__user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        return instance

    # def perform_destroy(self, instance):
    #     instance.status = Goal.Status.archived
    #     instance.save()
    #     return instance


class GoalListView(ListAPIView):
    model = Goal
    permission_classes = [GoalPermissions]
    serializer_class = GoalSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]
    filterset_class = GoalDateFilter
    ordering_fields = ["due_date", "priority"]
    ordering = ["title"]
    search_fields = ["title", "description"]

    def get_queryset(self):
        return Goal.objects.filter(category__board__participants__user=self.request.user, is_deleted=False)
