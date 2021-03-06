from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^init/', views.index, name="query"),
    url(r'^cond-query/', views.cond_query, name="cond-query"),
    url(r'^get-meta/', views.get_meta_fields, name="get-meta"), 
    url(r'^tuple-update/', views.tuple_update, name="tuple-update"),
    url(r'^restore-date/', views.restore_date, name="restore-date"),
    url(r'^backup-date/', views.backup_date, name="backup-date"),
]
