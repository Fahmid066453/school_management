from django.urls import path
from academic import views

urlpatterns = [
    path('student-data/add/', views.student_data_add, name='student_data_add'),
    path('student-data/list/', views.student_list, name='student_list'),
    # path('content-edit/<int:content_id>/', views.content_edit, name='content_edit'),
    # path('content_get_api/', views.content_get_api, name='content_json'),
    path('student-data/edit/<int:student_id>/', views.student_data_edit, name='student_data_edit'),
    path('student-data/delete/<int:student_id>/', views.student_data_delete, name='student_data_delete'),



    ############################################
     path('teacher-data/add/', views.teacher_data_add, name='teacher_data_add'),
     path('teacher-data/list/', views.teacher_list, name='teacher_list'),
    # # path('content-edit/<int:content_id>/', views.content_edit, name='content_edit'),
    # # path('content_get_api/', views.content_get_api, name='content_json'),
    # path('student-data/edit/<int:student_id>/', views.student_data_edit, name='student_data_edit'),
    # path('student-data/delete/<int:student_id>/', views.student_data_delete, name='student_data_delete'),

]