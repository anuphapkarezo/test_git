from django.urls import path , include
from . import views

urlpatterns = [
    path('index_test',views.go_index),
    path('Page_add_member',views.Page_add_member),
    path('page_login',views.page_login),

    # Function for page1
    path('test_connect_database',views.test_connect_database),
    path('save_member_to_database',views.save_member_to_database),
    path('save_member_excel_to_database',views.save_member_excel_to_database),
    path('delete_member_in_datebase',views.delete_member_in_datebase),
    path('edit_member_in_datebase',views.edit_member_in_datebase),

    path('page_login_programming',views.page_login_programming),
    path('selection_values',views.selection_values),
]