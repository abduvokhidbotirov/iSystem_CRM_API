from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from . import views


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass



todo_api_router = NestedDefaultRouter()



# TodoView
projects_tasks = projects_router.register('tasks',
                                          views.TodoView,
                                          base_name='project-tasks',
                                          parents_query_lookups=['project'])
# parents_query_lookups = Task.objects.filter(task={task})


# ReminderView
projects_tasks.register('reminders',
                        views.ReminderView,
                        base_name='project-task-reminders',
                        parents_query_lookups=['task__project', 'task'])
# pare


tasks_router = todo_api_router.register('tasks', views.TodoView)

# ReminderView
tasks_router.register('reminders',
                      views.CommentView,
                      base_name='task-reminders',
                      parents_query_lookups=['task'])

todo_api_router.register('reminders', views.ReminderView)