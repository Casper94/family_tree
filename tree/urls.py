from django.urls import path
from .views import FamilyMemberListView, FamilyTreeView, AddFamilyMemberView

urlpatterns = [
    path('members/', FamilyMemberListView.as_view(), name='family_member_list'),
    path('', FamilyTreeView.as_view(), name='family_tree'),
    path('add-members/', AddFamilyMemberView.as_view(), name='add_member'),
]
