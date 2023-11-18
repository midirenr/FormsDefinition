from django.http import JsonResponse, HttpResponse

from .models import DataBase
from .utilities.get_field_type import get_field_type
from .utilities.enums import EMPTY_GET_REQUEST_MESSAGE


def get_form(request):
    """
    Функия-обработчик для запроса по url: /get_form

    :param request: объект запроса
    :return: response
    """
    params = request.GET.lists()
    if len(list(params)) == 0:
        return HttpResponse(EMPTY_GET_REQUEST_MESSAGE)

    params = request.GET.lists()
    fields = {key: value[0] for (key, value) in dict(params).items()}
    for key, value in fields.items():
        fields[key] = get_field_type(value)

    db = DataBase()
    fields = db.get_form_by_example(fields)

    return JsonResponse(fields) if type(fields) == dict else HttpResponse(fields)
