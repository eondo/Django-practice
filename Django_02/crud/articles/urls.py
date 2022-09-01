from django.urls import path
from . import views # 이걸 추가해줘야 함

app_name = 'articles' # 다른 앱에도 index 등 똑같은 이름을 가질 수 있기 때문

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
