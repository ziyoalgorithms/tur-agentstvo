from django.shortcuts import get_object_or_404, HttpResponseRedirect, render
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from mainapp.models import Accommodation, ListOfCountries
from authapp.models import TravelUser
from authapp.forms import TravelUserRegisterForm
from adminapp.forms import TravelUserAdminEditForm, AccomodationEditForm



class TraveUserListView(ListView):
    model = TravelUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = TravelUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = TravelUserRegisterForm()

    content = {
        'title': title,
        'update_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'user/update'

    edit_user = get_object_or_404(TravelUser, pk=pk)

    if request.method == 'POST':
        edit_form = TravelUserAdminEditForm(
                                            request.POST,
                                            request.FILES,
                                            instance=edit_user
                                        )
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = TravelUserAdminEditForm(instance=edit_user)

    content = {
        'title': title,
        'update_form': edit_form,
    }

    return render(request, 'adminapp/user_update.html', content)



@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'user/delete'

    user = get_object_or_404(TravelUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {
        'title': title,
        'user_to_delete': user,
    }

    return render(request, 'adminapp/user_to_delete.html', content)



@user_passes_test(lambda u: u.is_superuser)
def countries(request):
    title = 'админка/страны'

    countries_list = ListOfCountries.objects.all()

    content = {
        'title': title,
        'objects': countries_list,
    }

    return render(request, 'adminapp/countries.html', content)


class CountryCreateView(CreateView):
    model = ListOfCountries
    template_name = 'adminapp/country_update.html'
    success_url = reverse_lazy('admin:countries')
    fields = '__all__'


class CountryUpdateView(UpdateView):
    model = ListOfCountries
    template_name = 'adminapp/country_update.html'
    success_url = reverse_lazy('admin:countries')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'страны/редактирование'

        return context


class CountryDeleteView(DeleteView):
    model = ListOfCountries
    template_name = 'adminapp/country_delete.html'
    success_url = reverse_lazy('admin:countries')

    def form_valid(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())





@user_passes_test(lambda u: u.is_superuser)
def accomodations(request, pk):
    title = 'админка/размещение'

    country = get_object_or_404(ListOfCountries, pk=pk)
    accommodation_list = Accommodation.objects.filter(
        country__id=pk).order_by('name')

    content = {
        'title': title,
        'country': country,
        'objects': accommodation_list,
    }

    return render(request, 'adminapp/accommodations.html', content)


@user_passes_test(lambda u: u.is_superuser)
def accomodation_create(request, pk):
    title = 'размещение/создание'
    country = get_object_or_404(ListOfCountries, pk=pk)

    if request.method == 'POST':
        accomodation_form = AccomodationEditForm(request.POST, request.FILES)

        if accomodation_form.is_valid():
            accomodation_form.save()
            return HttpResponseRedirect(reverse('admin:accommodations', args=[pk]))
    else:
        accomodation_form = AccomodationEditForm(
            initial={'country': country}
        )

    content = {
        'title': title,
        'update_form': accomodation_form,
        'country': country,
    }

    return render(request, 'adminapp/accommodation_update.html', content)



@user_passes_test(lambda u: u.is_superuser)
def accomodation_update(request, pk):
    title = 'размещение/редактирование'

    edit_accommodation = get_object_or_404(Accommodation, pk=pk)

    if request.method == 'POST':
        accomodation_edit_form = AccomodationEditForm(
            request.POST, request.FILES, instance=edit_accommodation)
        if accomodation_edit_form.is_valid():
            accomodation_edit_form.save()
            return HttpResponseRedirect(reverse('admin:accommodation_read', args=[edit_accommodation.pk]))
    else:
        accomodation_edit_form = AccomodationEditForm(
            instance=edit_accommodation
        )
    
    content = {
        'title': title,
        'update_form': accomodation_edit_form,
        'country': edit_accommodation.country,
    }

    return render(request, 'adminapp/accommodation_update.html', content)



class AccomodationDetailView(DetailView):
    model = Accommodation
    template_name = 'adminapp/accommodation_read.html'



@user_passes_test(lambda u: u.is_superuser)
def accomodation_delete(request, pk):
    title = 'размещение/удаление'
    accommodation = get_object_or_404(Accommodation, pk=pk)

    if request.method == 'POST':
        accommodation.is_active = False
        accommodation.save()
        return HttpResponseRedirect(reverse('admin:accommodations', args=[accommodation.country.pk]))

    content = {
        'title': title,
        'accommodation_to_delete': accommodation,
    }

    return render(request, 'adminapp/accommodation_delete.html', content)

