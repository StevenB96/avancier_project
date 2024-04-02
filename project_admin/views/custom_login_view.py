from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'project_admin/login.html'

    def get_success_url(self):
        logged_in_user = self.request.user
        username = logged_in_user.username

        if (username == 'business_user'):
            return '/admin/main/'
        
        return '/admin/'
