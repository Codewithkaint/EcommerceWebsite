from django.urls import path
from .import views

urlpatterns = [
    path("", views.index,name="shopHome"),
    # path("about/", views.about,name="shopAbout"),
    path("search/", views.searchBox,name="searchBox"),
    path("contact/", views.contact,name="shopConact"),
    path("tracker/", views.tracker,name="shopConact"),
    path("product/<int:myid>", views.prodView,name="shopProdView"),
    path("checkout/", views.checkOut,name="shopCheck"),
]
