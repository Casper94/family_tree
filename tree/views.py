from django.views.generic import ListView, TemplateView, CreateView
from .models import FamilyMember
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FamilyMemberForm

class FamilyMemberListView(ListView):
    model = FamilyMember
    template_name = 'tree/family_member_list.html'
    context_object_name = 'members'


class FamilyTreeView(LoginRequiredMixin, TemplateView):
    template_name = 'tree/family_tree.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        members = FamilyMember.objects.select_related('parent').all()

        def build_tree(node):
            children = FamilyMember.objects.filter(parent=node).order_by('child_number')
            return {
                'name': node.name,
                'sex': node.sex,
                'child_number': node.child_number,
                'spouse': node.spouse.name if node.spouse else "None",
                'children': [build_tree(child) for child in children]
            }

        root_members = FamilyMember.objects.filter(parent__isnull=True).order_by('child_number')
        context['tree_data'] = [build_tree(member) for member in root_members]
        return context


class AddFamilyMemberView(LoginRequiredMixin, CreateView):
    model = FamilyMember
    form_class = FamilyMemberForm
    template_name = 'tree/add_family_member.html'
    success_url = 'add_member'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)