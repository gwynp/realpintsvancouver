from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from sitegate.decorators import redirect_signedin, sitegate_view
#from sitegate.signup_flows.classic import ClassicSignup
#from django.generic.list import ListView
import core.models as coremodels
from django.conf import settings
from core.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.shortcuts import render_to_response
resp = {}
resp['MEDIA_URL'] = settings.MEDIA_URL

# Create your views here.

class LandingView(TemplateView):
    template_name = 'base/index.html'

class LocationListView(ListView):
    model = coremodels.Location
    template_name = 'location/list.html'
    paginate_by = 5

class LocationDetailView(DetailView):
    model = coremodels.Location
    template_name = 'location/detail.html'
    context_object_name = 'location'

class LocationCreateView(CreateView):
    model = coremodels.Location
    template_name = 'base/form.html'
    fields = "__all__"

class LocationUpdateView(UpdateView):
    model = coremodels.Location
    template_name = 'base/form.html'
    fields = "__all__"

class SearchListView(LocationListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.Location.objects.filter(title__icontains=incoming_query_string)

class ReviewCreateView(CreateView):
    model = coremodels.Review
    template_name = 'base/form.html'
    fields =['description', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.location = coremodels.Location.objects.get(id=self.kwargs['pk'])
        return super(ReviewCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.location.get_absolute_url()

class ReviewUpdateView(UpdateView):
    model = coremodels.Review
    template_name = 'base/form.html'
    fields =['description', 'rating']

    def get_object(self):
        return coremodels.Review.objects.get(location__id=self.kwargs['pk'], user=self.request.user)

    def get_success_url(self):
        return self.object.location.get_absolute_url

@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.

#@sitegate_view(flow=ClassicSignup)
def entrance(request):
    return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'base/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)