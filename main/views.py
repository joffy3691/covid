from django.views.generic import TemplateView, FormView
from accounts.forms import UserDetails, HospitalForm
from accounts.models import User_Attributes, Hospital, Request
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from ML import covid_priority
import datetime


class AllotmentPageView(TemplateView):
    template_name = 'main/allotment.html'


    def get_context_data(self, **kwargs):
        context = {}
        context['user'] = self.request.user
        try:
            context['filled_form'] = User_Attributes.objects.filter(user=context['user'].id)
            context['booked_hospital'] = Request.objects.filter(user=context['user'].id)
            av = Hospital.objects.filter(id=context['booked_hospital'][0].hospital)[0]
            avb = Hospital.objects.filter(id=context['booked_hospital'][0].hospital)[0].available_beds
            while avb>0:
                pending = Request.objects.filter(hospital=context['booked_hospital'][0].hospital).filter(fulfilled=0).order_by('priority')[0]
                pending.fulfilled=1
                pending.confirmtime=datetime.datetime.now()
                pending.save()
                avb-=1
                av.available_beds -=1
                av.save()
            context['queue'] = Request.objects.filter(fulfilled=0).filter(hospital=context['booked_hospital'][0].hospital).count()
            context['index'] = Request.objects.filter(fulfilled=0).filter(hospital=context['booked_hospital'][0].hospital).filter(priority__lt=context['booked_hospital'][0].priority).count()
        except:
            pass
        context['hospitals'] = Hospital.objects.all()
        return context

class IndexPageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['user'] = self.request.user
        context['filled_form'] = User_Attributes.objects.filter(user=context['user'].id)
        context['booked_hospital'] = Request.objects.filter(user=context['user'].id)
        context['users'] = User.objects.count()
        context['hospitals'] = Hospital.objects.count()
        context['bed_alloted'] = Request.objects.filter(fulfilled=1).count()
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
        fulfilled = 0
        pref_hospital = Hospital.objects.filter(id=hospital)[0]
        confirmtime="NA"
        if pref_hospital.available_beds>0:
            pref_hospital.available_beds -=1
            pref_hospital.save()
            fulfilled = 1
            confirmtime=datetime.datetime.now()
        det = User_Attributes.objects.filter(user=self.request.user.id).latest('id')
        breathing = det.breathing
        pneumonia = det.pneumonia
        age = det.age
        pregnant = det.pregnant
        diabetes = det.diabetic
        copd = det.copd
        asthma = det.asthma
        immsupr = det.immunocompromised
        hypertension = det.blood
        other = det.others
        cardio = det.heart
        obesity = det.obesity
        renal = det.ckd
        smoker = det.smoker
        priority = covid_priority.priority(breathing, pneumonia, age, pregnant, diabetes, copd, asthma, immsupr, hypertension,
                                  other, cardio, obesity, renal, smoker)
        Request.objects.create_data(user,hospital,priority,fulfilled,confirmtime)
        messages.success(
            request, _('Your request for bed has been confirmed.'))

        return redirect('index')


class FormPageView(FormView):
    template_name = 'main/register.html'
    form_class = UserDetails
    form = UserDetails

    def form_valid(self, form):
        if self.request.method == 'POST':
            form = UserDetails(self.request.POST, self.request.FILES)

            if form.is_valid():
                newform = form.save(commit=False)
                newform.user = self.request.user.id
                newform.date= datetime.datetime.now()
                newform.details_filled = 1

                newform.save()
                messages.success(
                    self.request, _('Your details have been stored.'))
                return redirect('index')
        else:
            form = UserDetails()
            return render(request, 'main/register.html', {'form': form})



class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
