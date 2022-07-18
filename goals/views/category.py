from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


from goals.models import GoalCategory, Goal
from goals.permissionts import GoalCategoryPermissions
from goals.serializers import GoalCategoryCreateSerializer, GoalCategorySerializer


class GoalCategoryCreateView(CreateAPIView):
    model = GoalCategory
    permission_classes = [IsAuthenticated]
    serializer_class = GoalCategoryCreateSerializer


class GoalCategoryListView(ListAPIView):
    queryset = GoalCategory.objects.all()
    model = GoalCategory
    permission_classes = [GoalCategoryPermissions]
    serializer_class = GoalCategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        OrderingFilter,
        SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ['board']
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]

    def get_queryset(self):
        return GoalCategory.objects.filter(
            board__participants__user=self.request.user)     # is_deleted=False


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    queryset = GoalCategory.objects.all()
    model = GoalCategory
    serializer_class = GoalCategorySerializer
    permission_classes = [GoalCategoryPermissions]

    def get_queryset(self):
        return GoalCategory.objects.filter(
            board__participants__user=self.request.user)  # is_deleted = False

    def perform_destroy(self, instance):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.goals.update(status=Goal.Status.archived)
        return instance