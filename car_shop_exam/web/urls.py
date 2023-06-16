from django.urls import path, include

from car_shop_exam.web.views import IndexView, CatalogView, ProfileCreateView, profile_details, profile_edit, \
    profile_delete, CreateCarView, CarDetailsView, CarEditView, car_delete

urlpatterns = [
    path('', IndexView.as_view(), name='home page'),
    path('catalogue/', CatalogView.as_view(), name='catalogue'),
    path('profile/', include([
        path('create/', ProfileCreateView.as_view(), name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('car/', include([
        path('create/', CreateCarView.as_view(), name='car create'),
        path('<int:pk>/details/', CarDetailsView.as_view(), name='car details'),
        path('<int:pk>/edit/', CarEditView.as_view(), name='car edit'),
        path('<int:pk>/delete/', car_delete, name='car delete'),
    ])),
]
