from .models import Type

def product_type_list(request):
    type_list = Type.objects.all()
    return {
        'product_type_list':type_list,
    }
