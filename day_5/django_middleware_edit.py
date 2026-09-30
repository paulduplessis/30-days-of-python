MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

Common_Middleware_index = MIDDLEWARE.index("django.middleware.common.CommonMiddleware")

MIDDLEWARE.insert(Common_Middleware_index, "corsheaders.middleware.CorsMiddleware")

if "django.middleware.clickjacking.XFrameOptionsMiddleware" in MIDDLEWARE:
    MIDDLEWARE.remove("django.middleware.clickjacking.XFrameOptionsMiddleware")

first_entry, *between_entries, last_entry = MIDDLEWARE

MIDDLEWARE_copy = MIDDLEWARE.copy()

MIDDLEWARE_copy.sort()

print(MIDDLEWARE)
print(MIDDLEWARE_copy)