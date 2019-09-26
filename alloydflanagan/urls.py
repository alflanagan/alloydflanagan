"""alloydflanagan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views
from django import forms
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext_lazy as _

from pages.views import home, about_me, contact

# Define two classes to add a CSS class to input fields for built-in login form
class MyAuthenticationForm(auth_views.AuthenticationForm):
    """A child of the built-in authentication form. Adds bootstrap form classes."""
    username = UsernameField(
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'form-control', }))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )


# pylint: disable=too-many-ancestors
class MyLoginView(auth_views.LoginView):
    """Customizes built-in login to to use MyAuthenticationForm."""
    form_class = MyAuthenticationForm


urlpatterns = [  # pylint: disable=invalid-name
    path('', home, name="home"),
    path('about_me/', about_me, name="about_me"),
    path('contact/', contact, name="contact"),
    path('admin/', admin.site.urls),
    path('blog/', include('blogs.urls')),
    path('portfolio/', include('portfolios.urls')),

    path('accounts/login/', MyLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('accounts/password_change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('accounts/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
