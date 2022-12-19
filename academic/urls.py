from django.urls import path
from academic import views

urlpatterns = [
    path('student-data/add/', views.student_data_add, name='student_data_add'),
    path('student-data/list/', views.student_list, name='student_list'),
    # path('content-edit/<int:content_id>/', views.content_edit, name='content_edit'),
    # path('content-delete/<int:content_id>/', views.content_delete, name='content_delete'),
    # path('content_get_api/', views.content_get_api, name='content_json'),
    path('student-data/edit/<int:student_id>/', views.student_data_edit, name='student_data_edit'),

]