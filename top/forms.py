from colorfield.widgets import ColorWidget
from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import TopPositionCasino, NameTop, Casino, Software, Badge, Country, Payment, CountryCasinoSetting, Source, \
    Link
from postbacks.models import Postback, Partner
from geo.models import Country, Currency


# TOP

class TopForm(ModelForm):
    class Meta:
        model = NameTop
        # exclude = ('slug', 'page_views', 'click', 'date_modified', 'date_published', 'thing_modified1',
        # 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified1',
        # 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5', 'mails')

        fields = (
        'name', 'favicon', 'source', 'design', 'country', 'header', 'top4_header', 'font_link', 'font_name', 'text',
        'promo1', 'promo2', 'hide_link', 'tr_play', 'tr_bonus', 'tr_fs',
        'tr_cashback', 'tr_info', 'tr_license', 'tr_md', 'tr_pay', 'tr_score', 'tr_votes',
        'tr_bottom', 'tr_bottom_2', 'tr_copy', 'tr_warning',
        'color', 'bg_color', 'h_color',
        'bg_img',
        'bg_tab_img', 'bg_mob_img',
        'logo', 'badge', 'icon_to_top',
        'button_color', 'button_text_color'
        )
        widgets = {
            'color': ColorWidget,
            'bg_color': ColorWidget,
            'h_color': ColorWidget,
            'button_color': ColorWidget,
        }

    def __init__(self, user, *args, **kwargs):
        super(TopForm, self).__init__(*args, **kwargs)
        self.fields['source'].queryset = user.profile.permission.all()


class TopFormWOColors(ModelForm):
    class Meta:
        model = NameTop
        # exclude = ('slug', 'page_views', 'click', 'date_modified', 'date_published', 'thing_modified1',
        # 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified1',
        # 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5', 'mails')

        fields = (
        'name', 'favicon', 'logo', 'source', 'design', 'country', 'header', 'top4_header', 'font_link', 'font_name',
        'text',
        'promo1', 'promo2', 'hide_link', 'tr_play', 'tr_bonus', 'tr_fs',
        'tr_cashback', 'tr_info', 'tr_license', 'tr_md', 'tr_pay', 'tr_score', 'tr_votes', 'tr_bottom', 'tr_bottom_2',
        'tr_copy', 'tr_warning')

        widgets = {
            'color': ColorWidget,
            'bg_color': ColorWidget,
            'h_color': ColorWidget,
            'button_color': ColorWidget,
        }

    def __init__(self, user, *args, **kwargs):
        super(TopFormWOColors, self).__init__(*args, **kwargs)
        self.fields['source'].queryset = user.profile.permission.all()


class TopFormTop4(ModelForm):
    class Meta:
        model = NameTop
        # exclude = ('slug', 'page_views', 'click', 'date_modified', 'date_published', 'thing_modified1',
        # 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified1',
        # 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5', 'mails')

        exclude = ('color', 'bg_color', 'h_color', 'bg_img', 'bg_tab_img', 'bg_mob_img', 'logo', 'badge', 'icon_to_top',
                   'button_color', 'button_text_color', 'font_link', 'font_name', 'promo1', 'promo2', 'image_1',
                   'ico_1', 'header_1', 'descript_1', 'image_2', 'ico_2', 'header_2', 'descript_2', 'image_3', 'ico_3',
                   'header_3', 'descript_3', 'tr_cashback', 'tr_info', 'tr_license', 'tr_bottom', 'tr_bottom_2', 'tr_md', 'tr_votes', 'tr_score',
                   'tr_warning', 'logo', 'date_modified1', 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5',
                   'thing_modified1', 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified',
                   'date_published', 'mails', 'click', 'page_views', 'slug')

    def __init__(self, user, *args, **kwargs):
        super(TopFormTop4, self).__init__(*args, **kwargs)
        self.fields['source'].queryset = user.profile.permission.all()


class TopFormTop3(ModelForm):
    class Meta:
        model = NameTop
        # exclude = ('slug', 'page_views', 'click', 'date_modified', 'date_published', 'thing_modified1',
        # 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified1',
        # 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5', 'mails')

        exclude = ('color', 'bg_color', 'h_color', 'bg_img', 'bg_tab_img', 'bg_mob_img', 'logo', 'badge', 'icon_to_top',
                   'button_color', 'button_text_color', 'font_link', 'font_name', 'promo1', 'promo2', 'image_1',
                   'ico_1', 'header_1', 'descript_1', 'image_2', 'ico_2', 'header_2', 'descript_2', 'image_3', 'ico_3',
                   'header_3', 'descript_3', 'tr_cashback', 'tr_info', 'tr_license', 'tr_md', 'tr_votes', 'tr_score', 'tr_bottom',
                   'tr_bottom_2', 'tr_warning', 'logo', 'tr_pay', 'date_modified1', 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5',
                   'thing_modified1', 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified',
                   'date_published', 'mails', 'click', 'page_views', 'slug')

    def __init__(self, user, *args, **kwargs):
        super(TopFormTop3, self).__init__(*args, **kwargs)
        self.fields['source'].queryset = user.profile.permission.all()


class TopFormOldTop(ModelForm):
    class Meta:
        model = NameTop
        # exclude = ('slug', 'page_views', 'click', 'date_modified', 'date_published', 'thing_modified1',
        # 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified1',
        # 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5', 'mails')

        exclude = ('color', 'bg_color', 'h_color', 'bg_img', 'bg_tab_img', 'bg_mob_img', 'logo', 'badge', 'icon_to_top',
                   'button_color', 'button_text_color', 'font_link', 'font_name', 'promo1', 'promo2', 'image_1',
                   'ico_1', 'header_1', 'descript_1', 'image_2', 'ico_2', 'header_2', 'descript_2', 'image_3', 'ico_3',
                   'header_3', 'descript_3', 'tr_votes', 'tr_score', 'tr_bottom',
                   'tr_bottom_2', 'tr_warning', 'logo', 'date_modified1', 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5',
                   'thing_modified1', 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified',
                   'date_published', 'mails', 'click', 'page_views', 'slug')

    def __init__(self, user, *args, **kwargs):
        super(TopFormOldTop, self).__init__(*args, **kwargs)
        self.fields['source'].queryset = user.profile.permission.all()


class TopFormWellBet(ModelForm):
    class Meta:
        model = NameTop
        # exclude = ('slug', 'page_views', 'click', 'date_modified', 'date_published', 'thing_modified1',
        # 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified1',
        # 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5', 'mails')

        exclude = ('color', 'bg_color', 'h_color', 'bg_img', 'bg_tab_img', 'bg_mob_img', 'logo', 'badge', 'icon_to_top',
                   'button_color', 'button_text_color', 'font_link', 'font_name', 'promo1', 'promo2',
                   'tr_votes', 'tr_score', 'tr_bottom', 'tr_fs', 'tr_bottom', 'tr_bottom_2'
                   'tr_bottom_2', 'tr_warning', 'logo', 'date_modified1', 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5',
                   'thing_modified1', 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified',
                   'date_published', 'mails', 'click', 'page_views', 'slug')

    def __init__(self, user, *args, **kwargs):
        super(TopFormWellBet, self).__init__(*args, **kwargs)
        self.fields['source'].queryset = user.profile.permission.all()


class TopFormNewTop(ModelForm):
    class Meta:
        model = NameTop
        # exclude = ('slug', 'page_views', 'click', 'date_modified', 'date_published', 'thing_modified1',
        # 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified1',
        # 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5', 'mails')

        exclude = ('image_1', 'ico_1', 'header_1', 'descript_1', 'image_2', 'ico_2', 'header_2', 'descript_2', 'image_3', 'ico_3',
                   'header_3', 'descript_3', 'font_link', 'font_name', 'tr_bottom', 'tr_bottom_2', 'tr_warning', 'date_modified1', 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5',
                   'thing_modified1', 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified',
                   'date_published', 'mails', 'click', 'page_views', 'slug')

    def __init__(self, user, *args, **kwargs):
        super(TopFormNewTop, self).__init__(*args, **kwargs)
        self.fields['source'].queryset = user.profile.permission.all()


class TopFormBetting(ModelForm):
    class Meta:
        model = NameTop
        # exclude = ('slug', 'page_views', 'click', 'date_modified', 'date_published', 'thing_modified1',
        # 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified1',
        # 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5', 'mails')

        exclude = ('image_1', 'ico_1', 'header_1', 'descript_1', 'image_2', 'ico_2', 'header_2', 'descript_2', 'image_3', 'ico_3',
                   'header_3', 'descript_3', 'promo2', 'promo2', 'tr_fs', 'date_modified1', 'date_modified2', 'date_modified3', 'date_modified4', 'date_modified5',
                   'thing_modified1', 'thing_modified2', 'thing_modified3', 'thing_modified4', 'thing_modified5', 'date_modified',
                   'date_published', 'mails', 'click', 'page_views', 'slug')

    def __init__(self, user, *args, **kwargs):
        super(TopFormBetting, self).__init__(*args, **kwargs)
        self.fields['source'].queryset = user.profile.permission.all()

# Casino


class CasinoMainForm(ModelForm):
    class Meta:
        model = Casino
        fields = ('name', 'logo', 'bg', 'partner', 'badge', 'license', 'top3_bg', 'pay_left', 'pay_right')


class CasinoDefaultForm(ModelForm):
    class Meta:
        model = Casino
        fields = ('adv1', 'adv2', 'adv3', 'min_dep', 'limit', 'cashback', 'fs')
        # widgets = {
        #     'pay': FilteredSelectMultiple(u'Pay', False),
        # }

    class Media:
        css = {
            'all': ['admin/css/widgets.css'],
        }
        js = ['/admin/jsi18n/']


class CCSForm(ModelForm):
    class Meta:
        model = CountryCasinoSetting
        exclude = ('date_modified', 'date_published', 'link', 'bonus', 'pay')
        selector = 'pay' + str(model.id)
        # widgets = {
        #     'pay': FilteredSelectMultiple(u'Pay', False),
        # }

    class Media:
        css = {
            'all': ['admin/css/widgets.css'],
        }
        js = ['/admin/jsi18n/']


# Link

class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ('source', 'url', 'top')

    def __init__(self, user, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['source'].queryset = user.profile.permission.all()


# Casino edition settings

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ('__all__')


class SoftwareForm(ModelForm):
    class Meta:
        model = Software
        fields = ('__all__')


class BadgeForm(ModelForm):
    class Meta:
        model = Badge
        fields = ('__all__')

        widgets = {
            'color_HEX': ColorWidget,
        }


class PostbackForm(ModelForm):
    class Meta:
        model = Postback
        fields = ('__all__')


class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = ('__all__')


# GEO

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ('__all__')


class CurrencyForm(ModelForm):
    class Meta:
        model = Currency
        fields = ('__all__')
