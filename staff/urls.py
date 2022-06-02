
from django.urls import path
from .views import *

urlpatterns = [

    path("dashboard", dashboard, name="dashboard"),
    path("categories", categories, name="categories"),
    path("articles", articles, name="articles"),
    path("delete/article/<id>", deleteArticle, name= "delete.article"),
    path("feedback", feedback, name="feedback"),
    path("feedback/reply/<id>", replyFeedback, name="feedback.reply")

]