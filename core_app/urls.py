
from django.urls import path
from core_app.views import views, principal, student, staff 


urlpatterns = [
    #Authentication
    path('', views.home, name='home'),
    path('login/', views.loginPage, name="login"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', principal.admin_home, name="admin_home"),

    #Principal
    path('add_staff/', principal.add_staff, name="add_staff"),
    path('add_staff_save/', principal.add_staff_save, name="add_staff_save"),
    path('manage_staff/', principal.manage_staff, name="manage_staff"),
    path('edit_staff/<staff_id>/', principal.edit_staff, name="edit_staff"),
    path('edit_staff_save/', principal.edit_staff_save, name="edit_staff_save"),
    path('delete_staff/<staff_id>/', principal.delete_staff, name="delete_staff"),

    path('add_course/', principal.add_course, name="add_course"),
    path('add_course_save/', principal.add_course_save, name="add_course_save"),
    path('manage_course/', principal.manage_course, name="manage_course"),
    path('edit_course/<course_id>/', principal.edit_course, name="edit_course"),
    path('edit_course_save/', principal.edit_course_save, name="edit_course_save"),
    path('delete_course/<course_id>/', principal.delete_course, name="delete_course"),

    path('manage_session/', principal.manage_session, name="manage_session"),
    path('add_session/', principal.add_session, name="add_session"),
    path('add_session_save/', principal.add_session_save, name="add_session_save"),
    path('edit_session/<session_id>', principal.edit_session, name="edit_session"),
    path('edit_session_save/', principal.edit_session_save, name="edit_session_save"),
    path('delete_session/<session_id>/', principal.delete_session, name="delete_session"),

    path('add_student/', principal.add_student, name="add_student"),
    path('add_student_save/', principal.add_student_save, name="add_student_save"),
    path('edit_student/<student_id>', principal.edit_student, name="edit_student"),
    path('edit_student_save/', principal.edit_student_save, name="edit_student_save"),
    path('manage_student/', principal.manage_student, name="manage_student"),
    path('delete_student/<student_id>/', principal.delete_student, name="delete_student"),

    path('add_subject/', principal.add_subject, name="add_subject"),
    path('add_subject_save/', principal.add_subject_save, name="add_subject_save"),
    path('manage_subject/', principal.manage_subject, name="manage_subject"),
    path('edit_subject/<subject_id>/', principal.edit_subject, name="edit_subject"),
    path('edit_subject_save/', principal.edit_subject_save, name="edit_subject_save"),
    path('delete_subject/<subject_id>/', principal.delete_subject, name="delete_subject"),
    
    path('check_email_exist/', principal.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', principal.check_username_exist, name="check_username_exist"),
    path('student_feedback_message/', principal.student_feedback_message, name="student_feedback_message"),
    path('student_feedback_message_reply/', principal.student_feedback_message_reply, name="student_feedback_message_reply"),
    path('staff_feedback_message/', principal.staff_feedback_message, name="staff_feedback_message"),
    path('staff_feedback_message_reply/', principal.staff_feedback_message_reply, name="staff_feedback_message_reply"),
    path('student_leave_view/', principal.student_leave_view, name="student_leave_view"),
    path('student_leave_approve/<leave_id>/', principal.student_leave_approve, name="student_leave_approve"),
    path('student_leave_reject/<leave_id>/', principal.student_leave_reject, name="student_leave_reject"),
    path('staff_leave_view/', principal.staff_leave_view, name="staff_leave_view"),
    path('staff_leave_approve/<leave_id>/', principal.staff_leave_approve, name="staff_leave_approve"),
    path('staff_leave_reject/<leave_id>/', principal.staff_leave_reject, name="staff_leave_reject"),
    path('admin_view_attendance/', principal.admin_view_attendance, name="admin_view_attendance"),
    path('admin_get_attendance_dates/', principal.admin_get_attendance_dates, name="admin_get_attendance_dates"),
    path('admin_get_attendance_student/', principal.admin_get_attendance_student, name="admin_get_attendance_student"),
    path('admin_profile/', principal.admin_profile, name="admin_profile"),
    path('admin_profile_update/', principal.admin_profile_update, name="admin_profile_update"),
    


    # URLS for Staff
    path('staff_home/', staff.staff_home, name="staff_home"),
    path('staff_take_attendance/', staff.staff_take_attendance, name="staff_take_attendance"),
    path('get_students/', staff.get_students, name="get_students"),
    path('save_attendance_data/', staff.save_attendance_data, name="save_attendance_data"),
    path('staff_update_attendance/', staff.staff_update_attendance, name="staff_update_attendance"),
    path('get_attendance_dates/', staff.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student/', staff.get_attendance_student, name="get_attendance_student"),
    path('update_attendance_data/', staff.update_attendance_data, name="update_attendance_data"),
    path('staff_apply_leave/', staff.staff_apply_leave, name="staff_apply_leave"),
    path('staff_apply_leave_save/', staff.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_feedback/', staff.staff_feedback, name="staff_feedback"),
    path('staff_feedback_save/', staff.staff_feedback_save, name="staff_feedback_save"),
    path('staff_profile/', staff.staff_profile, name="staff_profile"),
    path('staff_profile_update/', staff.staff_profile_update, name="staff_profile_update"),
    path('staff_add_result/', staff.staff_add_result, name="staff_add_result"),
    path('staff_add_result_save/', staff.staff_add_result_save, name="staff_add_result_save"),

    # URSL for Student
    path('student_home/', student.student_home, name="student_home"),
    path('student_view_attendance/', student.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post/', student.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave/', student.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save/', student.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback/', student.student_feedback, name="student_feedback"),
    path('student_feedback_save/', student.student_feedback_save, name="student_feedback_save"),
    path('student_profile/', student.student_profile, name="student_profile"),
    path('student_profile_update/', student.student_profile_update, name="student_profile_update"),
    path('student_view_result/', student.student_view_result, name="student_view_result"),
]
