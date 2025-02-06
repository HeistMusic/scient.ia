from django.views.generic import TemplateView


class A_Inicio(TemplateView):
    template_name = 'A_Inicio/index.html'

    def get_context_data(self, escape=None, *args, **kwargs):
        context = {
        }
        return context
