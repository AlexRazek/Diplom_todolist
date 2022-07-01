from django.contrib import admin

from goals.models import GoalCategory, Goal, GoalComment


# @admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")
    # readonly_fields = ("category", "updated")
    list_filter = ("is_deleted",)

admin.site.register(GoalCategory, GoalCategoryAdmin)


# @admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "priority", "due_date")
    search_fields = ("title", "user")
    # readonly_fields = ("category", "updated")
    list_filter = ("status", "priority")

admin.site.register(Goal, GoalAdmin)


# @admin.register(Goal)
class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ("goal_id", "text")
    list_display_links = ("text",)
    search_fields = ("text",)
    # readonly_fields = ("category", "updated")


admin.site.register(GoalComment, GoalCommentAdmin)


