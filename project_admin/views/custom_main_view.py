from django.views import View
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse
from django.templatetags.static import static


class CustomMainView(View):
    template_name = 'main/model_list.html'

    def get(self, request, *args, **kwargs):
        app_list = []
        image_url = static('avancier_diagram.png')

        # Iterate over app configs
        for app_config in apps.get_app_configs():
            # Assuming 'main' is the label of the app you're interested in
            if app_config.label == 'main':
                app_models = []
                # Iterate over models in the app
                for model in app_config.get_models():
                    base_url = f'{model._meta.model_name}'
                    if (request.user.has_perm(f'main.view_{model._meta.model_name}')):
                        model_info = {
                            'object_name': model._meta.object_name,
                            'name': model._meta.verbose_name_plural,
                            'add_url': base_url + '/add',
                            'admin_url': base_url
                        }
                        app_models.append(model_info)

                app_list.append({
                    'label': app_config.label,
                    'name': app_config.verbose_name,
                    'models': app_models
                })

        if (app_list[0]['models'] == []):
            app_list = []
            image_url = None

        context = {
            'app_list': app_list,
            'image_url': image_url,
        }

        return render(request, self.template_name, context)
