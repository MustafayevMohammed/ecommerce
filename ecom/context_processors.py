from store import models

def context_for_all_templates(request):
    return {
        'categories': models.Category.objects.all()
    }
