from django.db import models
from django.utils.text import slugify
from colorfield.fields import ColorField
from easy_thumbnails.fields import ThumbnailerImageField
from django.contrib.auth.models import User
from geo.models import Country
from decor.models import Theme
from postbacks.models import Partner

DESIGN = (
    ('new', 'New'),
    ('old', 'Old'),
    ('betting', 'Betting'),
    ('top3', 'Top3'),
    ('top3-light', 'Top3-Light'),
    ('top4', 'Top4')
)

LICENSES = (
    ('1', 'Curacao'),
    ('2', 'Malta'),
    ('3', 'AAMS'),
)

TOPS = (
    ('1', 'First'),
    ('2', 'Second'),
)

COLORS = (
    ('blue-band.png', 'Blue'),
    ('darkblue-band.png', 'DarkBlue'),
    ('red-band.png', 'Red'),
    ('green-band.png', 'Green'),
    ('yellow-band.png', 'Yellow'),
    ('violet-band.png', 'Violet'),
    ('purple-band.png', 'Purple'),
    ('orange-band.png', 'Orange'),
)
BG = (
    ('blue_bg.jpg', 'Blue'),
    ('purple_bg.jpg', 'Purple'),
    ('red_bg.jpg', 'Red'),
    ('green_bg.jpg', 'Green'),
    ('yellow_bg.jpg', 'Yellow'),
    ('azure_bg.jpg', 'Azure'),
    ('orange_bg.jpg', 'Orange'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    permission = models.ManyToManyField('Source', related_name='profile_permission', default=None, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = u"Профиль"
        verbose_name_plural = u"Профили"


class Payment(models.Model):
    name = models.CharField(u'name', max_length=50, blank=False)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/pay/", blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Payment"
        verbose_name_plural = u"Payments"


class Software(models.Model):
    name = models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/soft/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Software"
        verbose_name_plural = u"Softwares"


class Badge(models.Model):
    name = models.CharField(u'Name', max_length=20)
    color = models.CharField(u'Color', max_length=50, choices=COLORS, blank=True, null=True)
    text = models.CharField(u'Text', max_length=10, blank=True, null=True)
    color_HEX = ColorField(u'Цвет фона #RRGGBB', max_length=7, blank=False, null=True, default='#000000')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Badge"
        verbose_name_plural = u"Badges"


class TopPositionPayment(models.Model):
    casino = models.ForeignKey('Casino', related_name='tpp_casino', blank=True, null=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='tpp_country', blank=True, null=True, on_delete=models.CASCADE)
    payment = models.ForeignKey('Payment', related_name='tpp_payment', blank=True, null=True, on_delete=models.CASCADE)
    position = models.IntegerField(u'Position', default=0, blank=True, null=True)
    date_modified = models.DateTimeField(u'Last change', auto_now=True)
    date_published = models.DateTimeField(u'Created', auto_now_add=True)

    class Meta:
        verbose_name = u"Top Position Payment"
        verbose_name_plural = u"Top Position Payments"


class Casino(models.Model):
    name = models.CharField(u'Title', max_length=50)
    partner = models.ForeignKey(Partner, related_name='aff', blank=True, null=True, on_delete=models.SET_NULL)
    badge = models.ForeignKey(Badge, related_name='casino_badge', blank=True, null=True, on_delete=models.SET_NULL,
                              help_text="для нового топа")
    bg = models.CharField(u'Фон у логотипа', max_length=50, choices=BG, default='azure_bg.jpg',
                          help_text="для старого топа")
    license = models.CharField(u'License', max_length=3, choices=LICENSES, default=2)
    logo = ThumbnailerImageField(u'Casino Logo', upload_to="upload/img/logos/")
    top3_bg = models.ImageField('Фон на карточке', upload_to="upload/img/top3_bg/",
                                default='upload/img/top3_bg/skycrown_bg.png', help_text="Фон для дизайна Top3")
    country = models.ManyToManyField('CountryCasinoSetting', default=None, related_name='casino_ccs', blank=True)
    pay = models.ManyToManyField(Payment, related_name='pays', blank=True)

    pay_left = models.ForeignKey(Payment, related_name='casino_pay1', null=True, blank=True,
                                  on_delete=models.SET_NULL, help_text="для нового топа и беттинга",
                                  verbose_name='выделить платежку слева')
    pay_right = models.ForeignKey(Payment, related_name='casino_pay2', null=True, blank=True,
                                   on_delete=models.SET_NULL, help_text="для нового топа и беттинга",
                                   verbose_name='выделить платежку справа')

    link = models.ManyToManyField('Link', related_name='casino_link', blank=True)
    adv1 = models.CharField(u'Promo1', max_length=50, blank=True, null=True)
    adv2 = models.CharField(u'Promo2', max_length=50, blank=True, null=True)
    adv3 = models.CharField(u'Promo3', max_length=50, blank=True, null=True)
    min_dep = models.IntegerField(u'Min deposit', blank=False, null=False, default=0)
    bonus = models.IntegerField(u'Welcome bonus', blank=False, null=False, default=0)
    limit = models.IntegerField(u'Bonus', null=False, blank=False, default=0)
    cashback = models.IntegerField(u'CashBack %', null=False, blank=False, default=0)
    fs = models.IntegerField(u'Free Spins', null=False, blank=False, default=0)
    click = models.IntegerField(u'Clicks', default=0, blank=True, null=True)
    date_modified = models.DateTimeField(u'Last change', auto_now=True)
    date_published = models.DateTimeField(u'Created', auto_now_add=True)

    def __str__(self):
        return self.name

    def bonus_limit(self):
        limit = self.limit
        short_limit = ''
        if limit >= 1000:
            if limit < 10000:
                limit = str(limit)
                short_limit = limit[0] + '.' + limit[1] + 'K'
            else:
                limit = str(limit)
                short_limit = limit[:-3] + 'K'
        else:
            limit = str(limit)
            short_limit = limit
        return short_limit

    class Meta:
        verbose_name = u"Casino"
        verbose_name_plural = u"Casinos"


class CountryCasinoSetting(models.Model):
    country = models.ForeignKey(Country, related_name='ccs_country', blank=True, null=True, on_delete=models.CASCADE)
    link = models.ManyToManyField('Link', related_name='ccs_link', blank=True)
    adv1 = models.CharField(u'Promo1', max_length=50, blank=True, null=True)
    adv2 = models.CharField(u'Promo2', max_length=50, blank=True, null=True)
    adv3 = models.CharField(u'Promo3', max_length=50, blank=True, null=True)

    pay_left = models.ForeignKey(Payment, related_name='payment_left', null=True, blank=True,
                                  on_delete=models.SET_NULL, help_text="для нового топа и беттинга",
                                  verbose_name='выделить платежку слева')
    pay_right = models.ForeignKey(Payment, related_name='payment_right', null=True, blank=True,
                                   on_delete=models.SET_NULL, help_text="для нового топа и беттинга",
                                   verbose_name='выделить платежку справа')

    min_dep = models.IntegerField(u'Min deposit', blank=False, null=False, default=0)
    bonus = models.IntegerField(u'Welcome bonus', blank=False, null=False, default=0)
    limit = models.IntegerField(u'Bonus', null=False, blank=False, default=0)
    cashback = models.IntegerField(u'CashBack %', null=False, blank=False, default=0)
    fs = models.IntegerField(u'Free Spins', null=False, blank=False, default=0)
    pay = models.ManyToManyField(Payment, related_name='ccs_pays', blank=True)
    date_modified = models.DateTimeField(u'Last change', auto_now=True)
    date_published = models.DateTimeField(u'Created', auto_now_add=True)

    def __str__(self):
        return self.country.name

    def bonus_limit(self):
        limit = self.limit
        short_limit = ''
        if limit >= 1000:
            if limit < 10000:
                limit = str(limit)
                short_limit = limit[0] + '.' + limit[1] + 'K'
            else:
                limit = str(limit)
                short_limit = limit[:-3] + 'K'
        else:
            limit = str(limit)
            short_limit = limit
        return short_limit

    class Meta:
        verbose_name = u"Country Casino Setting"
        verbose_name_plural = u"Country Casino Settings"


class Link(models.Model):
    source = models.ForeignKey('Source', related_name='link_source', blank=False, null=False, on_delete=models.CASCADE)
    top = models.ForeignKey('NameTop', related_name='link_top', blank=True, null=True, on_delete=models.CASCADE)
    url = models.CharField(u'Url', max_length=255, blank=False, null=True, default=None)

    def __str__(self):
        return str(self.id) + ' ' + str(self.url)

    class Meta:
        verbose_name = u"Ссылка"
        verbose_name_plural = u"Ссылки"


class TopPositionCasino(models.Model):
    nameTop = models.ForeignKey('NameTop', related_name='tpc_nametop', blank=True, null=True, on_delete=models.CASCADE)
    casino = models.ForeignKey(Casino, related_name='tpc_casino', blank=True, null=True, on_delete=models.CASCADE)
    position = models.IntegerField(u'Position', default=0, blank=True, null=True)
    date_modified = models.DateTimeField(u'Last change', auto_now=True)
    date_published = models.DateTimeField(u'Created', auto_now_add=True)


class NameTop(models.Model):
    name = models.CharField(u'name', max_length=50, blank=False, unique=True)
    favicon = ThumbnailerImageField(u'Значок в title', upload_to="upload/img/site_logos/", blank=True, null=True)

    slug = models.SlugField(u'URL-slug', max_length=255, unique=True, default="FILLED-IN-AUTOMATICALLY")
    source = models.ForeignKey('Source', related_name='nameTop_source', blank=False, null=True,
                               on_delete=models.SET_NULL)
    design = models.CharField(u'Design', choices=DESIGN, default='new', max_length=50)
    country = models.ForeignKey(Country, related_name='nametop_country', blank=True, null=True,
                                on_delete=models.SET_NULL)
    # theme = models.ForeignKey(Theme, related_name='country_theme', blank=True, null=True, default=None, on_delete=models.SET_NULL, help_text="для нового топа")
    header = models.CharField(u'Заголовок в шапке (desktop) и title', max_length=100, blank=True, null=True)
    top4_header = ThumbnailerImageField(u'Логотип в дизайне top4', upload_to="upload/img/site_logos/",
                                       blank=True, null=True)
    font_link = models.TextField(u'Ссылка на шрифт заголовка', blank=True, null=True, help_text="для беттинга")
    font_name = models.CharField(u'Название шрифта', max_length=100, blank=True, null=True, help_text="для беттинга")
    text = models.CharField(u'Текст (description)', max_length=300, blank=True, null=True)
    promo1 = models.CharField(u'Текст в шапке (верх)', max_length=300, blank=True, null=True,
                              help_text="для нового топа")
    promo2 = models.CharField(u'Текст в шапке (низ)', max_length=300, blank=True, null=True,
                              help_text="для нового топа")
    hide_link = models.BooleanField(u'Прикрытие ссылок', default=True, blank=True, null=False)

    # pay1_highlight = models.ForeignKey(Payment, related_name='nametop_pay1', null=True, blank=True,
    #                                    on_delete=models.SET_NULL, help_text="для нового топа и беттинга",
    #                                    verbose_name='выделить платежку слева')
    # pay2_highlight = models.ForeignKey(Payment, related_name='nametop_pay2', null=True, blank=True,
    #                                    on_delete=models.SET_NULL, help_text="для нового топа и беттинга",
    #                                    verbose_name='выделить платежку справа')

    image_1 = ThumbnailerImageField(u'Изображение 1', upload_to='uploads/img/site_logos/', blank=True, null=True)
    ico_1 = ThumbnailerImageField(u'Иконка 1', upload_to='uploads/img/site_logos/', blank=True, null=True)
    header_1 = models.CharField(max_length=200, blank=True, null=True)
    descript_1 = models.CharField(max_length=200, blank=True, null=True)

    image_2 = ThumbnailerImageField(u'Изображение 1', upload_to='uploads/img/site_logos/', blank=True, null=True)
    ico_2 = ThumbnailerImageField(u'Иконка 1', upload_to='uploads/img/site_logos/', blank=True, null=True)
    header_2 = models.CharField(max_length=200, blank=True, null=True)
    descript_2 = models.CharField(max_length=200, blank=True, null=True)

    image_3 = ThumbnailerImageField(u'Изображение 1', upload_to='uploads/img/site_logos/', blank=True, null=True)
    ico_3 = ThumbnailerImageField(u'Иконка 1', upload_to='uploads/img/site_logos/', blank=True, null=True)
    header_3 = models.CharField(max_length=200, blank=True, null=True)
    descript_3 = models.CharField(max_length=200, blank=True, null=True)

    tr_play = models.CharField(u'Текст на КНОПКЕ', max_length=24, blank=True, null=True)
    tr_bonus = models.CharField(u'Текст БОНУС', max_length=24, blank=True, null=True)
    tr_fs = models.CharField(u'Текст ФРИ СПИНЫ', max_length=24, blank=True, null=True)
    tr_cashback = models.CharField(u'Текст КЭШБЭК', max_length=24, blank=True, null=True)
    tr_info = models.CharField(u'Текст СИЛЬНЫЕ СТОРОНЫ', max_length=24, blank=True, null=True)
    tr_license = models.CharField(u'Текст ЛИЦЕНЗИЯ', max_length=12, blank=True, null=True)
    tr_md = models.CharField(u'Текст МИН ДЕПОЗИТ', max_length=24, blank=True, null=True)
    tr_pay = models.CharField(u'Текст ПЛАТЕЖКИ', max_length=36, blank=True, null=True)
    tr_score = models.CharField(u'Текст БАЛЛЫ', max_length=12, blank=True, null=True,
                                help_text="для нового топа и беттинга")
    tr_votes = models.CharField(u'Текст ГОЛОСА', max_length=12, blank=True, null=True,
                                help_text="для нового топа и беттинга")
    tr_bottom = models.TextField(u'Текст ВНИЗУ СТРАНИЦЫ', blank=True, null=True, help_text="для беттинга и top3")
    tr_bottom_2 = models.TextField(u'Текст ВНИЗУ СТРАНИЦЫ', blank=True, null=True,
                                   help_text="для беттинга и top3 2 Абзац")
    tr_copy = models.TextField(u'Текст Все права защищены', blank=True, null=True)
    tr_warning = models.TextField(u'Текст ПРЕДУПРЕЖДЕНИЕ В САМОМ НИЗУ', blank=True, null=True, help_text="для беттинга")

    page_views = models.IntegerField(u'Views', default=0, blank=True, null=True)
    click = models.IntegerField(u'Clicks', default=0, blank=True, null=True)
    mails = models.ManyToManyField('MailTop', related_name='nameTop_mails', blank=True)
    date_modified1 = models.DateTimeField(u'Дата и время', blank=True, null=True)
    date_modified2 = models.DateTimeField(u'Дата и время', blank=True, null=True)
    date_modified3 = models.DateTimeField(u'Дата и время', blank=True, null=True)
    date_modified4 = models.DateTimeField(u'Дата и время', blank=True, null=True)
    date_modified5 = models.DateTimeField(u'Дата и время', blank=True, null=True)
    thing_modified1 = models.TextField(u'Событие', blank=True, null=True)
    thing_modified2 = models.TextField(u'Событие', blank=True, null=True)
    thing_modified3 = models.TextField(u'Событие', blank=True, null=True)
    thing_modified4 = models.TextField(u'Событие', blank=True, null=True)
    thing_modified5 = models.TextField(u'Событие', blank=True, null=True)
    date_modified = models.DateTimeField(u'Last change', auto_now=True)
    date_published = models.DateTimeField(u'Created', auto_now_add=True)

    # Theme
    bg_color = ColorField(u'Цвет фона #RRGGBB', max_length=7, blank=False, null=True, default='#000000')
    color = ColorField(u'Основной цвет #RRGGBB', max_length=7, blank=False, null=True, default='#FFFFFF')
    h_color = ColorField(u'Цвет хедера #RRGGBB', max_length=7, blank=False, null=True, default='#FFF000')
    bg_img = ThumbnailerImageField(u'Фоновое изображение (desktop 1280px)', upload_to="upload/img/custom/", blank=False,
                                   null=True)
    bg_tab_img = ThumbnailerImageField(u'Фоновое изображение (tablet 992px)', upload_to="upload/img/custom/",
                                       blank=True, null=True)
    bg_mob_img = ThumbnailerImageField(u'Фоновое изображение (mobile 480px)', upload_to="upload/img/custom/",
                                       blank=True, null=True)
    logo = ThumbnailerImageField(u'Логотип', upload_to="upload/img/site_logos/", blank=True, null=True)
    badge = ThumbnailerImageField(u'Значок (справа от лого)', upload_to="upload/img/site_badges/", blank=True,
                                  null=True)
    icon_to_top = models.BooleanField(u'Иконка GO TO TOP', default=False, blank=True, null=False)
    button_color = ColorField(u'Цвет кнопки', max_length=7, blank=False, null=True, default='#FFFFFF')
    button_text_color = ColorField(u'Цвет текста кнопки', max_length=7, blank=False, null=True, default='#FFFFFF')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Top"
        verbose_name_plural = u"Tops"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(NameTop, self).save(*args, **kwargs)


class MailTop(models.Model):
    mail = models.CharField(u'Почта', max_length=255, blank=False)
    country = models.ForeignKey(Country, related_name='mailtop_country', blank=True, null=True,
                                on_delete=models.SET_NULL)

    def __str__(self):
        return self.mail

    class Meta:
        verbose_name = u"Почта"
        verbose_name_plural = u"Почты"


class MailSocial(models.Model):
    mail = models.CharField(u'Почта', max_length=255, blank=False)
    country = models.ForeignKey(Country, related_name='mailsocial_country', blank=True, null=True,
                                on_delete=models.SET_NULL)
    site = models.CharField(u'Сайт', max_length=255, blank=False)

    def __str__(self):
        return self.mail

    class Meta:
        verbose_name = u"Почта Социалки"
        verbose_name_plural = u"Почты Социалок"


class Source(models.Model):
    name = models.CharField(u'Источник', blank=False, max_length=255, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Источник"
        verbose_name_plural = u"Источники"
