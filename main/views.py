from django.views.generic import TemplateView,FormView
from accounts.forms import UserDetails
from accounts.models import User_Attributes
from django.shortcuts import redirect

class IndexPageView(FormView):
    template_name = 'main/index.html'
    form_class = UserDetails

    def get_initial(self):
        initial = super(IndexPageView, self).get_initial()
        initial['user'] = self.request.user.id
        return initial
    def form_valid(self, form):
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
        User_Attributes.objects.create_data(user,details_filled,age,gender,bmi,fever,cough,spo2,breathing,pregnant,smoker,alcoholic,
                    diabetic,cancer,ckd,copd,autoimmune,immunocompromised,heart,asthma,blood,liver)

        return redirect('index')


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
