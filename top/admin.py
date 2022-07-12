from django.contrib import admin

from .models import NameTop, MailTop, Casino, Software, Country, Payment, CountryCasinoSetting, TopPositionCasino, \
    Badge, Source, Profile, Link, MailSocial, TopPositionPayment


class NameTopAdmin(admin.ModelAdmin):
    list_display = ("name", "id")


class LinkAdmin(admin.ModelAdmin):
    list_display = ('source', 'url', 'ccs_link', 'casino_link')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('permission',)


class TopPositionCasinoAdmin(admin.ModelAdmin):
    list_display = ('nameTop', 'casino', 'id', 'position')


class TopPositionPaymentAdmin(admin.ModelAdmin):
    list_display = ('payment', 'id', 'position', 'casino', 'country')


class CasinoAdmin(admin.ModelAdmin):
    list_display = ('name', 'click', 'id')
    filter_horizontal = ('country', 'pay', 'link')
    search_fields = ('name',)
    save_on_top = True
    readonly_fields = ('click',)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)


class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CountryCasinoSettingAdmin(admin.ModelAdmin):
    list_display = ('casino_ccs', 'country')
    filter_horizontal = ('pay', 'link')


class SourceAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MailTopAdmin(admin.ModelAdmin):
    list_display = ('mail', 'country')


class MailSocialAdmin(admin.ModelAdmin):
    list_display = ('mail', 'country', 'site')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(NameTop, NameTopAdmin)
admin.site.register(TopPositionCasino, TopPositionCasinoAdmin)
admin.site.register(TopPositionPayment, TopPositionPaymentAdmin)
admin.site.register(Casino, CasinoAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Badge, BadgeAdmin)
admin.site.register(CountryCasinoSetting, CountryCasinoSettingAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(MailTop, MailTopAdmin)
admin.site.register(MailSocial, MailSocialAdmin)
