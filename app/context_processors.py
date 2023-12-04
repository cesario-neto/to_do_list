from core.models import SiteSetup


def site_setup_processor(request):
    try:
        site_setup = SiteSetup.objects.all().first()
    except SiteSetup.DoesNotExist:
        site_setup = []

    return {'site_setup': site_setup}
