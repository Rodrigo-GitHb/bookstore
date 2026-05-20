from django.http import JsonResponse


def home(request):
    return JsonResponse(
        {
            "name": "bookstore-api",
            "status": "ok",
            "endpoints": {
                "admin": "/admin/",
                "auth_token": "/api-token-auth/",
                "bookstore_v1": "/bookstore/v1/",
                "bookstore_v2": "/bookstore/v2/",
            },
        }
    )
