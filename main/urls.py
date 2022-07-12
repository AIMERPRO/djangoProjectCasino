# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from top import views as topviews
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

router = routers.DefaultRouter()
router.register('nametop', topviews.NameTopViewSet, basename='user-list')

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url('', include('pwa.urls')),
]
urlpatterns += [
    path('admin/', admin.site.urls),
    path('', topviews.index, name='index'),
    path('json/', topviews.get_objects, name='get_objects'),
    path('social/mail/', topviews.social_mail, name='social_mail'),
    path('top/admin/', topviews.topadmin, name='topadmin'),
    path('top/casinoadmin/', topviews.casinoadmin, name='casinoadmin'),
    path('top/admin/topdelete/<slug:slug>/', topviews.topdelete, name='topdelete'),
    path('top/admin/casinodelete/<slug:slug>/', topviews.casinodelete, name='casinodelete'),
    path('top/admin/linkdelete/<slug:slug>/', topviews.linkdelete, name='linkdelete'),
    path('top/admin/ccsdelete/<slug:slug>/', topviews.ccsdelete, name='ccsdelete'),
    path('top/admin/position/<slug:slug>/', topviews.position, name='position'),
    path('top/admin/casino/<slug:slug>/', topviews.casinoedit, name='casinoedit'),
    path('top/admin/payment_position/<slug:slug>/', topviews.payment_position, name='payment_position'),
    path('top/admin/edit/<slug:slug>/', topviews.topedit, name='topedit'),
    path('go/<slug:pk>/', topviews.go, name='go'),
    path('top/admin/currencyedit/<slug:slug>/', topviews.currencyedit, name='currency_edit'),  # CurrencyEdit
    path('top/admin/countryedit/<slug:slug>/', topviews.countryedit, name='country_edit'),  # CountryEdit
    path('top/admin/paymentedit/<slug:slug>/', topviews.paymentedit, name='payment_edit'),  # PaymentEdit
    path('top/admin/provideredit/<slug:slug>/', topviews.provideredit, name='provider_edit'),  # ProviderEdit
    path('top/admin/badgeredit/<slug:slug>/', topviews.badgeedit, name='badge_edit'),  # BadgeEdit
    path('top/currencyadmin/', topviews.currencyadmin, name='currency_admin'),  # CurrencyAdmin
    path('top/admin/currencydelete/<slug:slug>/', topviews.currencydelete, name='currency_delete'),  # CurrencyDelete
    path('top/countryadmin/', topviews.countryadmin, name='country_admin'),  # CountryAdmin
    path('top/admin/countrydelete/<slug:slug>/', topviews.countrydelete, name='country_delete'),  # CountryDelete
    path('top/paymentadmin/', topviews.paymentadmin, name='payment_admin'),  # PaymentsAdmin
    path('top/admin/paymentdelete/<slug:slug>/', topviews.paymentdelete, name='payment_delete'),  # PaymentsDelete
    path('top/provideradmin/', topviews.provideradmin, name='provider_admin'),  # ProviderAdmin
    path('top/admin/providerdelete/<slug:slug>/', topviews.providerdelete, name='provider_delete'),  # ProviderDelete
    path('top/badgeadmin/', topviews.badgeadmin, name='badge_admin'),  # BadgeAdmin
    path('top/admin/badgedelete/<slug:slug>/', topviews.badgedelete, name='badge_delete'),  # BadgeDelete
    path('top/<slug:slug>/', topviews.topshow, name='topshow'),
    # path('top_add_tpp/add_tpp/', topviews.add_tpp, name='add_tpp'),
    path('api/v1/social/mail/', topviews.SocialMailAPI.as_view()),
    path('api/v1/social/mail_test/', topviews.SocialMailAPITest.as_view()),
    path('api/v1/', include(router.urls))
]

if settings.DEBUG==True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)