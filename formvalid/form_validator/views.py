from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from form_validator.db_utils import get_db_handle
from form_validator.utils import ValidForm, find_forms


class GetFormView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        context = {'result': ''}
        if request.method == "POST":
            requests_post = request.POST.copy()
            requests_post.pop('csrfmiddlewaretoken', None)

            if requests_post:
                field_types = {key: ValidForm(value).type_form
                               for key, value in requests_post.items()}
                db = get_db_handle()
                result_forms = find_forms(db, field_types)

                if result_forms:
                    # Получаем имена подходящих форм из базы данных TinyDB
                    # Используйте актуальный ключ для идентификатора шаблона
                    template_names = result_forms[0]['name']

                    context['result'] = template_names
                else:
                    context = field_types
            else:
                context['result'] = 'Not None response'

        return JsonResponse(context)
