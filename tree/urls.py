from django.urls import path
from .views import FamilyMemberListView, FamilyTreeView

urlpatterns = [
    path('members/', FamilyMemberListView.as_view(), name='family_member_list'),
    path('', FamilyTreeView.as_view(), name='family_tree'),
]
