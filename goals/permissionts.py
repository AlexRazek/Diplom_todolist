from rest_framework import permissions

from goals.models import BoardParticipant
from rest_framework.permissions import IsAuthenticated


class BoardPermissions(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return BoardParticipant.objects.filter(
                user=request.user,
                board=obj
            ).exists()
        return BoardParticipant.objects.filter(
            user=request.user, board=obj, role=BoardParticipant.Role.owner
        ).exists()


class GoalCategoryPermissions(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        filters: dict = {'user': request.user, 'board': obj.board}
        if request.method not in permissions.SAFE_METHODS:
            filters['role__in'] = [BoardParticipant.Role.owner, BoardParticipant.Role.writer]
            return BoardParticipant.objects.filter(**filters).exists()


class GoalPermissions(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        filters: dict = {'user': request.user, 'board': obj.category.board}
        if request.method not in permissions.SAFE_METHODS:
            filters['role__in'] = [BoardParticipant.Role.owner, BoardParticipant.Role.writer]
            return BoardParticipant.objects.filter(**filters).exists()


class CommentsPermissions(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user