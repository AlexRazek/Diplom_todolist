from django.contrib import admin
from django.db.models import Count

from goals.models import GoalCategory, Goal, GoalComment, BoardParticipant, Board


class GoalInline(admin.TabularInline):
    model = Goal
    extra = 0
    show_change_link = True

    def _get_form_for_get_fields(self, request, obj=None):
        return self.get_formset(request, obj, fields=("title", "status", "priority", "due_date")).form

    def has_change_permission(self, request, obj=None):
        return False


# @admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "goals_count", "created", "updated")
    search_fields = ("title", "user")
    # readonly_fields = ("category", "updated")
    list_filter = ("is_deleted",)
    inlines = (GoalInline,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_goals_count=Count('goal', distinct=True))
        return queryset

    def goals_count(self, obj):
        return obj._goals_count

    goals_count.short_description = 'Количество целей'


admin.site.register(GoalCategory, GoalCategoryAdmin)


# @admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "priority", "due_date", "comments_count")
    search_fields = ("title", "user")
    # readonly_fields = ("category", "updated")
    list_filter = ("status", "priority")

    # inlines = (GoalCommentInline,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_comments_count=Count('goal_comments', distinct=True))
        return queryset

    def comments_count(self, obj):
        return obj._comments_count

    comments_count.short_description = 'Количество комментариев'


admin.site.register(Goal, GoalAdmin)


# @admin.register(Goal)
class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ("goal_id", "text")
    list_display_links = ("text",)
    search_fields = ("text",)
    # readonly_fields = ("category", "updated")


admin.site.register(GoalComment, GoalCommentAdmin)


class BoardParticipantInline(admin.TabularInline):
    model = BoardParticipant
    extra = 0

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not self.has_view_or_change_permission(request):
            queryset = queryset.none()
        queryset = queryset.exclude(role=BoardParticipant.Role.owner)
        return queryset


class BoardAdmin(admin.ModelAdmin):
    list_display = ("title", "participants_count", "is_deleted", "owner")        # "owner",
    search_fields = ("title",)
    list_filter = ("is_deleted",)
    inlines = (BoardParticipantInline,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related("participants")
        return queryset

    def owner(self, obj):
        return obj.participants.filter(role=BoardParticipant.Role.owner).get().user

    def participants_count(self, obj):
        return obj.participants.count() - 1

    owner.short_description = 'Владелец'
    participants_count.short_description = 'Количество участников'


admin.site.register(Board, BoardAdmin)
