from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='home'),
    path('teacher/', views.Teacher, name='teacher'),
    path('about/', views.About, name='about'),
    path('courses/', views.Courses, name='courses'),
    path('Student/', views.Student, name='Student'),
    path('Studentdetails/', views.Studentdetails, name='Studentdetails'),
    path('SubjectFeedbackBiology/', views.SubjectFeedbackBiology, name='SubjectFeedbackBiology'),
    path('parent/', views.Parent, name='parent'),
    path('Sprofile/', views.Sprofile, name='Sprofile'),
    path('Assgnmnt_View/', views.Assgnmnt_View, name='Assgnmnt_View'),
    path('Course_materilals_view/', views.Course_materilals_view, name='Course_materilals_view'),
    path('Forgotpsswd/', views.Forgotpsswd, name='forgotpsswd'),
    path('Resetpsswd/', views.Resetpsswd, name='reset_psswd'),
    path('logout', views.logout_view , name='logout'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('download_pdf/<int:id>/', views.download_pdf, name='download_pdf'),
    path('download_pdf_CM/<int:id>/', views.download_pdf_CM, name='download_pdf_CM'),


]
