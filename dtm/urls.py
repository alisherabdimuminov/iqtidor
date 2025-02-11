from django.urls import path


from .views import (
    get_subjects,
    get_dtms,
    get_dtm,
    paticipate_dtm,
)


urlpatterns = [
    path("subjects/", get_subjects,),
    path("", get_dtms,),
    path("<int:dtm_id>/", get_dtm,),
    path("<int:dtm_id>/participate/", paticipate_dtm,),
]
