
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


from goals.models import GoalComment
from goals.serializers import CommentCreateSerializer, CommentSerializer


class CommentCreateView(CreateAPIView):
    model = GoalComment
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer


class CommentView(RetrieveUpdateDestroyAPIView):
    model = GoalComment
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GoalComment.objects.filter(goal__user=self.request.user)

    # def perform_destroy(self, instance):
    #     instance.is_deleted = True
    #     instance.save()
    #     return instance


class CommentListView(ListAPIView):
    model = GoalComment
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        OrderingFilter,
        SearchFilter,
    ]
    filterset_fields = ['goal']
    ordering = ['-id']


    def get_queryset(self):
        return GoalComment.objects.filter(goal__user=self.request.user)
