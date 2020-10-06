from django.views.generic import TemplateView, FormView
from accounts.forms import UserDetails, HospitalForm
from accounts.models import User_Attributes, Hospital, Request
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class IndexPageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['user'] = self.request.user
        context['filled_form'] = User_Attributes.objects.filter(user=context['user'].id)
        return context

class HospitalPageView(LoginRequiredMixin,FormView):
    template_name = 'main/book.html'
    form_class = HospitalForm

    def get_context_data(self, **kwargs):
        context = super(HospitalPageView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['hospitals'] = Hospital.objects.all()
        return context

    def get_initial(self):
        initial = super(HospitalPageView, self).get_initial()
        initial['user'] = self.request.user.id
        return initial

    def form_valid(self, form):
        request = self.request
        user = self.request.user.id
        hospital = form.cleaned_data['hospital']
        Request.objects.create_data(user,hospital)
        messages.success(
            request, _('Thank You for filling the form.'))

        return redirect('index')


class FormPageView(FormView):
    template_name = 'main/register.html'
    form_class = UserDetails

    def get_initial(self):
        initial = super(FormPageView, self).get_initial()
        initial['user'] = self.request.user.id
        return initial

    def form_valid(self, form):
        request = self.request
        ud = User_Attributes()
        user = self.request.user.id
        details_filled = 1
        age = form.cleaned_data['age']
        gender = form.cleaned_data['gender']
        bmi = form.cleaned_data['bmi']
        fever = form.cleaned_data['fever']
        spo2 = form.cleaned_data['spo2']
        cough = form.cleaned_data['cough']
        breathing = form.cleaned_data['breathing']
        pregnant = form.cleaned_data['pregnant']
        smoker = form.cleaned_data['smoker']
        alcoholic = form.cleaned_data['alcoholic']
        diabetic = form.cleaned_data['diabetic']
        cancer = form.cleaned_data['cancer']
        ckd = form.cleaned_data['ckd']
        copd = form.cleaned_data['copd']
        autoimmune = form.cleaned_data['autoimmune']
        immunocompromised = form.cleaned_data['immunocompromised']
        heart = form.cleaned_data['heart']
        asthma = form.cleaned_data['asthma']
        blood = form.cleaned_data['blood']
        liver = form.cleaned_data['liver']
        User_Attributes.objects.create_data(user, details_filled, age, gender, bmi, fever, cough, spo2, breathing,
                                            pregnant, smoker, alcoholic,
                                            diabetic, cancer, ckd, copd, autoimmune, immunocompromised, heart, asthma,
                                            blood, liver)
        messages.success(
            request, _('Thank You for filling the form.'))

        return redirect('index')


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
