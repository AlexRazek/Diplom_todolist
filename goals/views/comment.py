from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination


from goals.models import GoalComment
from goals.permissionts import CommentsPermissions
from goals.serializers import CommentCreateSerializer, CommentSerializer


class CommentCreateView(CreateAPIView):
    model = GoalComment
    permission_classes = [CommentsPermissions]
    serializer_class = CommentCreateSerializer


class CommentView(RetrieveUpdateDestroyAPIView):
    # queryset = GoalComment.objects.all()
    model = GoalComment
    serializer_class = CommentSerializer
    permission_classes = [CommentsPermissions]

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)


class CommentListView(ListAPIView):
    # queryset = GoalComment.objects.all()
    model = GoalComment
    permission_classes = [CommentsPermissions]
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ['goal']
    ordering = '-id'

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)
