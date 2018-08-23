from django.conf import settings


def commit_info(request):
    return {
        'COMMIT_NUM': settings.COMMIT_NUM,
        'COMMIT_HASH': settings.COMMIT_HASH
    }