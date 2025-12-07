from django.utils.deprecation import MiddlewareMixin
from .core import Moniv

moniv = Moniv()


class MonivMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        context = {
            "user": getattr(request, "user", None).username if getattr(request, "user", None) else None,
            "path": request.path,
            "method": request.method,
            "GET": request.GET.dict(),
            "POST": request.POST.dict(),
            "META": {k: v for k, v in request.META.items() if k.startswith("HTTP_")},
        }
        moniv.capture_exception(exception, context=context)
        return None
