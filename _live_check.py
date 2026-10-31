import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pcs_project.settings")
django.setup()
from importlib import import_module
from django.conf import settings
from django.contrib.auth import get_user_model, SESSION_KEY, BACKEND_SESSION_KEY, HASH_SESSION_KEY
import urllib.request

u = get_user_model().objects.filter(is_superuser=True).first()
engine = import_module(settings.SESSION_ENGINE)
s = engine.SessionStore()
s[SESSION_KEY] = str(u.pk)
s[BACKEND_SESSION_KEY] = "django.contrib.auth.backends.ModelBackend"
s[HASH_SESSION_KEY] = u.get_session_auth_hash()
s.set_expiry(3600)
s.save()
print("LIVE session_key:", s.session_key)

for p in ["/dashboard/", "/cases/", "/reception/"]:
    req = urllib.request.Request("http://127.0.0.1:8000" + p,
                                 headers={"Cookie": "sessionid=" + s.session_key})
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8", "replace")
            print(p, resp.status, "install_hits",
                  body.count("stch-install-btn") + body.count("data-install-app"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        print(p, e.code, "install_hits",
              body.count("stch-install-btn") + body.count("data-install-app"))
