from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


#Creating Router Object
router=DefaultRouter()

#Register StudentViewSet with Router
router.register('stucreate', views.StudentViewSet, basename='student') #(IP/stucreste/) is our path to run this API
#We can write anything in the place of //student//, //router//, //stucreate//

urlpatterns = [
    path('',include(router.urls)),
]




# urlpatterns = [
#     path('stucreate/', views.StudentListCreate.as_view()),
#     path('stucreate/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),

#     # path('stucreate/<int:pk>', views.StudentList.as_view()),
# ]