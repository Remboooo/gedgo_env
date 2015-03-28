from gedgo.models import Gedcom, Family
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

import django
django.setup()

gedcom = Gedcom.objects.get(id=1)
gedcom.title = "The Gedgo Family Tree"
gedcom.description = (
    "Ged-go is written in Django with d3.js visualizations, based on the idea "
    "that a genealogy website and gedcom viewer can be beautiful and "
    "intuitive.\n\n"
    "Most of the web-based genealogy software out there is pretty ugly and "
    "difficult to navigate in.  There are often silly little icons and "
    "information is presented in hard to read tables.  Instead, the "
    "philosophy of Ged-go is to have fewer features, but to present a gedcom "
    "in a clear and well designed way."
)

family = Family.objects.get(pointer="F1")
gedcom.key_families.add(family)
gedcom.save()

su = User.objects.create(
    username='devel',
    first_name='Johnny',
    last_name='Dev',
    email='devel@example.com',
    is_superuser=True,
    is_staff=True
)
su.set_password('devel')
su.save()

site = Site.objects.get()
site.name = 'The Gedgo Family Tree'
site.save()
