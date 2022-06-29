from rest_framework import serializers

from core.serializers import UserSerializer
from goals.models import GoalCategory, GoalComment


class GoalCategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        read_only_fields = ("id", "created", "updated", "user", "is_deleted")
        fields = "__all__"


class GoalCategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = GoalCategory
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")


class GoalSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = GoalCategory
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("not allowed in deleted category")

        if value.user != self.context["request"].user:
            raise serializers.ValidationError("not owner of category")

        return value


class GoalCreateSerializer(GoalSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        models = GoalComment
        fields = "__all__"
        read_only_fields = ("id", "created", "updated")

    def validate_goal(self, value):
        if value.user != self.context['request'].user:
            raise ValueError('Not owner')
        return value


class CommentSerializer(CommentCreateSerializer):
    # goal = GoalSerializer(read_only=True)
    user = UserSerializer(read_only=True)           #sourse='goal.user' #sourse='goal.category.user'


# class CommentCreateSerializer(BaseGoalCommentSerializer):
#     pass
#     # user = serializers.ReadOnlyField(sourse='owner__id')  # sourse='owner'
