from django.urls import path,include
from authsystem import views
urlpatterns = [
    path('',views.home,name='login'),
    path('logout',views.logout_session,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('voting/<int:id>',views.voting,name='voting'),
    path('vote/<int:id>/<int:per>',views.votesys,name="vote"),
    path('results',views.results,name="results"),
    path('removepost/<int:id>',views.removePost,name="removepost"),
    path('addpost',views.addPost,name="addpost"),
    path('addparticipant',views.addParticipant,name="addparticipant"),
    path('removeparticipant/<int:po>/<int:id>',views.removeParticipant,name="removeparticipant"),



]
