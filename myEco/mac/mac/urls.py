
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('shop.url')),
    # path("",views.index,name="HomePage"),
    
    path("blog/",include('blog.urls'))
   

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
