from core.models import UserProfile
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		#fields = ('website', 'picture')
		fields = ('website',)

def register(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
    		user.set_password(user.password)
    		user.save()

    		profile = profile_form.save(commit=False)
    		profile.user = user
    		profile.save()
    		registered = True
    	else:
			print user_form.errors, profile_form.errors


	return render_to_response(
		'base/register.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)