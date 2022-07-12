import requests
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import TopForm, CasinoMainForm, CasinoDefaultForm, CCSForm, LinkForm, CurrencyForm, CountryForm, \
    PaymentForm, SoftwareForm, BadgeForm, TopFormWOColors, TopFormNewTop, TopFormBetting, TopFormTop3, TopFormTop4, \
    TopFormOldTop
from .models import NameTop, MailTop, Casino, Software, Payment, CountryCasinoSetting, TopPositionCasino, Source, Link, \
    MailSocial, Badge, TopPositionPayment
from geo.models import Country, Currency
from postbacks.models import Postback, Partner
import json
from datetime import datetime

from rest_framework.views import APIView
from rest_framework import viewsets

from .serializers import NameTopSerializer


class NameTopViewSet(viewsets.ModelViewSet):
    queryset = NameTop.objects.all()
    serializer_class = NameTopSerializer


class SocialMailAPI(APIView):
    def get(self, request):
        mail_req = request.query_params['mail']
        if mail_req == '':
            return JsonResponse('empty', safe=False)
        country_req = request.query_params['country']
        site_req = request.query_params['site']

        country = Country.objects.get(slug=country_req)

        new_mail = MailSocial(mail=mail_req, site=site_req, country=country)
        new_mail.save()

        return JsonResponse('ok', safe=False)


class SocialMailAPITest(APIView):
    def get(self, request):
        mail_req = request.query_params['mail']
        if mail_req == '':
            return JsonResponse('empty', safe=False)
        country_req = request.query_params['country']
        site_req = request.query_params['site']

        country = Country.objects.get(slug=country_req)

        new_mail = MailSocial(mail=mail_req, site=site_req, country=country)

        # new_mail.save()

        return JsonResponse('ok', safe=False)


def index(request):
    temp = "topnew/base.html"
    return render(request, temp)


def social_mail(request):
    if request.method == 'GET':
        mail_req = request.GET.get('mail')
        if mail_req == '':
            return JsonResponse('empty', safe=False)
        country_req = request.GET.get('country')
        site_req = request.GET.get('site')

        new_mail = MailSocial(mail=mail_req, site=site_req)
        new_mail.save()

        country = Country.objects.get(slug=country_req)
        new_mail.country = country
        new_mail.save()

        return JsonResponse('ok', safe=False)
    return Http404


def get_objects(request):
    url = 'https://casino10top.site/json/'
    response = requests.get(url)
    objects = response.json()
    # casinos = casinos.replace('\\', '')
    objects = json.loads(objects)
    count = 0
    item_name = []
    source = get_object_or_404(Source, name='Palatka')
    for item in objects:
        try:
            casino = get_object_or_404(Casino, name=item['fields']['name'])
        except:
            count += 1
            new_item = Casino(name=item['fields']['name'])
            new_item.logo = item['fields']['logo']
            new_item.license = item['fields']['license']

            p = requests.get('https://casino10top.site/media/' + item['fields']['logo'])
            path = '/home/boss/www/all-tops/django/media/upload/img/logos/'
            file = path + item['fields']['name'] + '.png'
            out = open(file, "wb")
            out.write(p.content)
            out.close()
            new_item.logo = 'upload/img/logos/' + item['fields']['name'] + '.png'
            new_item.adv1 = item['fields']['adv1_gr']
            new_item.adv2 = item['fields']['adv2_gr']
            new_item.adv3 = item['fields']['adv3_gr']
            new_item.min_dep = item['fields']['min_dep']
            new_item.bonus = item['fields']['bonus']
            new_item.limit = item['fields']['limit']
            # new_item.cashback = item['fields']['cashback']
            new_item.fs = item['fields']['fs']
            new_item.save()
            new_link = Link(source=source, url=item['fields']['link_gr'])
            new_link.save()
            new_item.link.add(new_link)
            new_item.save()
            pay_name = []
            for pay_id in item['fields']['pay_gr']:
                url = 'https://casino10top.site/pay/slug/' + str(pay_id) + '/'
                response_pay = requests.get(url)
                pay_objects = response_pay.json()
                # casinos = casinos.replace('\\', '')
                pay_objects = json.loads(pay_objects)
                for pay in pay_objects:
                    try:
                        old_pay = get_object_or_404(Payment, name=pay['fields']['name'])
                        new_item.pay.add(old_pay)
                        new_item.save()
                        pay_name.append(str(pay['fields']['name']) + ' - old;')
                    except:
                        new_pay = Payment(name=pay['fields']['name'])
                        p = requests.get('https://casino10top.site/media/' + pay['fields']['logo'])
                        path = '/home/boss/www/all-tops/django/media/upload/img/pay/'
                        file = path + pay['fields']['name'] + '.png'
                        out = open(file, "wb")
                        out.write(p.content)
                        out.close()
                        new_pay.logo = 'upload/img/pay/' + pay['fields']['name'] + '.png'

                        # new_pay.logo = pay['fields']['logo']
                        new_pay.save()
                        new_item.pay.add(new_pay)
                        new_item.save()
                        pay_name.append(str(pay['fields']['name']) + ' - new;')
            item_name.append(str(count) + '. ' + str(item['fields']['name'] + str(pay_name)))
            australia = Country.objects.get(slug='gr')
            try:
                casino_ccs = get_object_or_404(CountryCasinoSetting, country=australia, casino_ccs=new_item)
            except:
                ccs_new = CountryCasinoSetting(country=australia)
                # ccs_new.link = item['fields']['link']
                ccs_new.adv1 = item['fields']['adv1_gr']
                ccs_new.adv2 = item['fields']['adv2_gr']
                ccs_new.adv3 = item['fields']['adv3_gr']
                ccs_new.min_dep = item['fields']['min_dep']
                ccs_new.bonus = item['fields']['bonus']
                ccs_new.limit = item['fields']['limit']
                # ccs_new.cashback = item['fields']['cashback']
                ccs_new.fs = item['fields']['fs']
                ccs_new.save()
                new_ccs_link = Link(source=source, url=item['fields']['link_gr'])
                new_ccs_link.save()
                ccs_new.link.add(new_ccs_link)
                ccs_new.save()
                pay_ccs_name = []
                for ccs_pay_id in item['fields']['pay_gr']:
                    url = 'https://casino10top.site/pay/slug/' + str(ccs_pay_id) + '/'
                    response_pay = requests.get(url)
                    pay_objects = response_pay.json()
                    # casinos = casinos.replace('\\', '')
                    pay_objects = json.loads(pay_objects)
                    for pay in pay_objects:
                        try:
                            old_pay = get_object_or_404(Payment, name=pay['fields']['name'])
                            ccs_new.pay.add(old_pay)
                            ccs_new.save()
                            pay_ccs_name.append(str(pay['fields']['name']) + ' - old;')
                        except:
                            new_ccs_pay = Payment(name=pay['fields']['name'])
                            p = requests.get('https://casino10top.site/media/' + pay['fields']['logo'])
                            path = '/home/boss/www/all-tops/django/media/upload/img/pay/'
                            file = path + pay['fields']['name'] + '.png'
                            out = open(file, "wb")
                            out.write(p.content)
                            out.close()
                            new_ccs_pay.logo = 'upload/img/pay/' + pay['fields']['name'] + '.png'

                            # new_pay.logo = pay['fields']['logo']
                            new_ccs_pay.save()
                            ccs_new.pay.add(new_ccs_pay)
                            ccs_new.save()
                            pay_ccs_name.append(str(pay['fields']['name']) + ' - new;')
                new_item.country.add(ccs_new)
                new_item.save()
        else:
            australia = Country.objects.get(slug='gr')
            try:
                casino_ccs = get_object_or_404(CountryCasinoSetting, country=australia, casino_ccs=casino)
            except:
                ccs_new = CountryCasinoSetting(country=australia)
                # ccs_new.link = item['fields']['link']
                ccs_new.adv1 = item['fields']['adv1_gr']
                ccs_new.adv2 = item['fields']['adv2_gr']
                ccs_new.adv3 = item['fields']['adv3_gr']
                ccs_new.min_dep = item['fields']['min_dep']
                ccs_new.bonus = item['fields']['bonus']
                ccs_new.limit = item['fields']['limit']
                # ccs_new.cashback = item['fields']['cashback']
                ccs_new.fs = item['fields']['fs']
                ccs_new.save()
                new_link = Link(source=source, url=item['fields']['link_gr'])
                new_link.save()
                ccs_new.link.add(new_link)
                ccs_new.save()
                pay_ccs_name = []
                for ccs_pay_id in item['fields']['pay_gr']:
                    url = 'https://casino10top.site/pay/slug/' + str(ccs_pay_id) + '/'
                    response_pay = requests.get(url)
                    pay_objects = response_pay.json()
                    # casinos = casinos.replace('\\', '')
                    pay_objects = json.loads(pay_objects)
                    for pay in pay_objects:
                        try:
                            old_pay = get_object_or_404(Payment, name=pay['fields']['name'])
                            ccs_new.pay.add(old_pay)
                            ccs_new.save()
                            pay_ccs_name.append(str(pay['fields']['name']) + ' - old;')
                        except:
                            new_ccs_pay = Payment(name=pay['fields']['name'])
                            p = requests.get('https://casino10top.site/media/' + pay['fields']['logo'])
                            path = '/home/boss/www/top10casino-no-com/django/media/upload/img/pay/'
                            file = path + pay['fields']['name'] + '.png'
                            out = open(file, "wb")
                            out.write(p.content)
                            out.close()
                            new_ccs_pay.logo = 'upload/img/pay/' + pay['fields']['name'] + '.png'

                            # new_pay.logo = pay['fields']['logo']
                            new_ccs_pay.save()
                            ccs_new.pay.add(new_ccs_pay)
                            ccs_new.save()
                            pay_ccs_name.append(str(pay['fields']['name']) + ' - new;')
                casino.country.add(ccs_new)
                casino.save()
    result = '- \n'.join(item_name)
    return HttpResponse(result)


# is_active name partner badge license logo position top_position link adv1 adv2 adv3 min_dep bonus limit cashback fs real_position click country pay

def go(request, pk):
    postbacks = Postback.objects.filter(is_active=True)
    gambler_id = {}
    if postbacks:
        for postback in postbacks:
            if postback.name in request.GET:
                gambler_id[postback.name] = request.GET[postback.name]
    params = ''
    for name in gambler_id:
        if params != '':
            params += '&'
        params += name + '=' + gambler_id[name]

    link = get_object_or_404(Link, id=pk)
    fulllink = linkbuilder(link.url, params)

    return redirect(fulllink, permanent=True)


def topshow(request, slug):
    # Top
    tpc_list = get_list_or_404(TopPositionCasino.objects.order_by('position'), nameTop__slug=slug, )
    top = get_object_or_404(NameTop, slug=slug)
    country = top.country

    # POST
    responce_text = False
    if request.method == 'POST':
        request_mail = request.POST.get('mail')
        mail = MailTop(mail=request_mail, country=country)
        mail.save()
        top.mails.add(mail)
        top.save()
        responce_text = True

    # Postbacks
    postbacks = Postback.objects.filter(is_active=True)
    gambler_id = {}
    if postbacks:
        for postback in postbacks:
            if postback.name in request.GET:
                gambler_id[postback.name] = request.GET[postback.name]
    params = ''
    for name in gambler_id:
        if params != '':
            params += '&'
        params += name + '=' + gambler_id[name]
    # Casinos
    casino_list = []
    for tpc in tpc_list:
        casino = tpc.casino

        try:
            tpp_list = get_list_or_404(TopPositionPayment.objects.order_by('position'), casino=casino, country=country)
        except:
            tpp_list = None

        try:
            casino_ccs = get_object_or_404(CountryCasinoSetting, country=country, casino_ccs=casino)
            # casino ccs link + posback params
            try:
                # link = Link.objects.get(source=top.source, ccs_link=casino_ccs)

                link = get_list_or_404(Link, source=top.source, ccs_link=casino_ccs)[0]

                if top.hide_link:
                    casino_ccs.url = '/go/' + str(link.id) + '/' + '?' + params
                else:
                    if casino_ccs.link != None:
                        fulllink = linkbuilder(link.url, params)
                        casino_ccs.url = fulllink
            except:
                casino_ccs.url = '#'
            casino_and_ccs = [tpc.casino, casino_ccs, tpp_list]

        except:
            # casino link + posback params
            try:
                tpp_list = get_list_or_404(TopPositionPayment.objects.order_by('position'), casino=casino,
                                           country=country)
            except:
                tpp_list = None

            try:
                link = Link.objects.get(source=top.source, ccs_link=casino)
                if top.hide_link:
                    tpc.casino.url = '/go/' + str(link.id) + '/' + '?' + params
                else:
                    if tpc.casino.link != None:
                        fulllink = linkbuilder(link.url, params)
                        tpc.casino.url = fulllink
            except:
                tpc.casino.url = '#'

            casino_and_ccs = [tpc.casino, None, tpp_list]

        casino_list.append(casino_and_ccs)

    # Providers
    provider_list = Software.objects.all()[:24]

    # Template design
    if top.design == 'old':
        temp = 'topold/country.html'
    elif top.design == 'betting':
        temp = 'betting/country.html'
    elif top.design == 'new':
        temp = 'topnew/country.html'
    elif top.design == 'top3':
        temp = 'top3/country.html'
    elif top.design == 'top3-light':
        temp = 'top3-light/country.html'
    elif top.design == 'top4':
        temp = 'top4/country.html'

    # Context
    context = {'top': top, 'casino_list': casino_list, 'providers': provider_list, 'gambler_id': params,
               'responce_text': responce_text}
    return render(request, temp, context)


@login_required
def topadmin(request):
    if request.method == "POST":
        slug = request.POST.get('slug')
        clone_creator(NameTop, slug)
    temp = 'topadmin/topadmin.html'
    user = request.user
    tops = NameTop.objects.all().filter(source__in=user.profile.permission.all())
    casinos = Casino.objects.all()
    postbacks = Postback.objects.all()
    params = ''
    for postback in postbacks:
        if params != '':
            params += '&'
        if postback.name == 'utm_term':
            params += postback.name + '=' + '{keyword}'
        else:
            params += postback.name + '=' + '{subid}'

    context = {'tops': tops, 'casinos': casinos, 'params': params}
    return render(request, temp, context)


@login_required
def casinoadmin(request):
    if request.method == "POST":
        id = request.POST.get('id')
        casino_clone_creator(Casino, id)

    temp = 'topadmin/casinoadmin.html'
    casinos = Casino.objects.all().order_by('name')
    context = {'casinos': casinos, }
    return render(request, temp, context)


@login_required
def countryadmin(request):
    temp = 'topadmin/countryadmin.html'
    countries = Country.objects.all().order_by('name')
    context = {'countries': countries, }
    return render(request, temp, context)


@login_required
def currencyadmin(request):
    temp = 'topadmin/currencyadmin.html'
    currencies = Currency.objects.all().order_by('name')
    context = {'currencies': currencies, }
    return render(request, temp, context)


@login_required
def paymentadmin(request):
    temp = 'topadmin/paymentadmin.html'
    payments = Payment.objects.all().order_by('name')
    context = {'payments': payments, }
    return render(request, temp, context)


@login_required
def provideradmin(request):
    temp = 'topadmin/provideradmin.html'
    providers = Software.objects.all().order_by('name')
    context = {'providers': providers, }
    return render(request, temp, context)


@login_required
def badgeadmin(request):
    temp = 'topadmin/badgeadmin.html'
    badges = Badge.objects.all().order_by('name')
    context = {'badges': badges, }
    return render(request, temp, context)


@login_required
def topdelete(request, slug):
    top = NameTop.objects.get(slug=slug)
    tpc = TopPositionCasino.objects.all().filter(nameTop__slug=slug)
    for item in tpc:
        item.delete()
    top.delete()
    return redirect('topadmin')


@login_required
def ccsdelete(request, slug):
    ccs = CountryCasinoSetting.objects.get(id=slug)
    casino = Casino.objects.get(country=ccs)
    ccs.delete()
    return redirect('casinoedit', slug=casino.id)


@login_required
def linkdelete(request, slug):
    link = Link.objects.get(id=slug)
    try:
        casino = Casino.objects.get(link=link)
    except:
        casino = Casino.objects.get(country__link=link)
    link.delete()
    return redirect('casinoedit', slug=casino.id)


@login_required
def currencydelete(request, slug):
    currency = Currency.objects.get(id=slug)
    currency.delete()
    return redirect('currency_admin')


@login_required
def countrydelete(request, slug):
    country = Country.objects.get(id=slug)
    country.delete()
    return redirect('country_admin')


@login_required
def paymentdelete(request, slug):
    payment = Payment.objects.get(id=slug)
    payment.delete()
    return redirect('payment_admin')


@login_required
def providerdelete(request, slug):
    provider = Software.objects.get(id=slug)
    provider.delete()
    return redirect('provider_admin')


@login_required
def badgedelete(request, slug):
    badge = Badge.objects.get(id=slug)
    badge.delete()
    return redirect('badge_admin')


@login_required
def casinodelete(request, slug):
    casino = Casino.objects.get(id=slug)
    ccs_list = CountryCasinoSetting.objects.all().filter(casino_ccs__id=slug)
    tpc = TopPositionCasino.objects.all().filter(casino__id=slug)
    for item in ccs_list:
        item.delete()
    for item in tpc:
        item.delete()
    casino.delete()
    return redirect('casinoadmin')


@login_required
def currencyedit(request, slug):
    context = {}

    # Get Currency
    if slug == 'new':
        currency = Currency(name='New')

    else:
        currency = get_object_or_404(Currency, id=slug)

    # Template
    temp = 'topadmin/currencyedit.html'

    # Forms
    formMain = CurrencyForm(instance=currency)

    # POST request
    if request.method == "POST":
        if request.POST.get('form') == 'main':
            form = CurrencyForm(request.POST, request.FILES, instance=currency)
            if form.is_valid():
                currency = form.save()
                currency.save()
            else:
                context = {'currency': currency, 'formMain': form}
                return render(request, temp, context)

        return redirect('currency_edit', slug=currency.id)

    context.update({'currency': currency, 'formMain': formMain})
    return render(request, temp, context)


@login_required
def provideredit(request, slug):
    context = {}

    # Get Currency
    if slug == 'new':
        provider = Software(name='New')

    else:
        provider = get_object_or_404(Software, id=slug)

    # Template
    temp = 'topadmin/currencyedit.html'

    # Forms
    formMain = SoftwareForm(instance=provider)

    # POST request
    if request.method == "POST":
        if request.POST.get('form') == 'main':
            form = SoftwareForm(request.POST, request.FILES, instance=provider)
            if form.is_valid():
                provider = form.save()
                provider.save()
            else:
                context = {'provider': provider, 'formMain': form}
                return render(request, temp, context)

        return redirect('provider_edit', slug=provider.id)

    context.update({'provider': provider, 'formMain': formMain})
    return render(request, temp, context)


@login_required
def paymentedit(request, slug):
    context = {}

    # Get Currency
    if slug == 'new':
        payment = Payment(name='New')

    else:
        payment = get_object_or_404(Payment, id=slug)

    # Template
    temp = 'topadmin/paymentedit.html'

    # Forms
    formMain = PaymentForm(instance=payment)

    # POST request
    if request.method == "POST":
        if request.POST.get('form') == 'main':
            form = PaymentForm(request.POST, request.FILES, instance=payment)
            if form.is_valid():
                payment = form.save()
                payment.save()
            else:
                context = {'payment': payment, 'formMain': form}
                return render(request, temp, context)

        return redirect('payment_edit', slug=payment.id)

    context.update({'payment': payment, 'formMain': formMain})
    return render(request, temp, context)


@login_required
def countryedit(request, slug):
    context = {}

    # Get Currency
    if slug == 'new':
        country = Country(name='New')

    else:
        country = get_object_or_404(Country, id=slug)

    # Template
    temp = 'topadmin/countryedit.html'

    # Forms
    formMain = CountryForm(instance=country)

    # POST request
    if request.method == "POST":
        if request.POST.get('form') == 'main':
            form = CountryForm(request.POST, request.FILES, instance=country)
            if form.is_valid():
                country = form.save()
                country.save()
            else:
                context = {'country': country, 'formMain': form}
                return render(request, temp, context)

        return redirect('country_edit', slug=country.id)

    context.update({'country': country, 'formMain': formMain})
    return render(request, temp, context)


@login_required
def badgeedit(request, slug):
    context = {}

    # Get Currency
    if slug == 'new':
        badge = Badge(name='New')

    else:
        badge = get_object_or_404(Badge, id=slug)

    # Template
    temp = 'topadmin/badgeedit.html'

    # Forms
    formMain = BadgeForm(instance=badge)

    # POST request
    if request.method == "POST":
        if request.POST.get('form') == 'main':
            form = BadgeForm(request.POST, request.FILES, instance=badge)
            if form.is_valid():
                badge = form.save()
                badge.save()
            else:
                context = {'badge': badge, 'formMain': form}
                return render(request, temp, context)

        return redirect('badge_edit', slug=badge.id)

    context.update({'badge': badge, 'formMain': formMain})
    return render(request, temp, context)


@login_required
def casinoedit(request, slug):
    context = {}
    # Casino, CCS get
    slug = slug
    if slug == 'new':
        casino = Casino(name='New')
        ccs_list = []
        links = {}
    else:
        casino = get_object_or_404(Casino, id=slug)
        linksDefault = casino.link.all().filter(source__in=request.user.profile.permission.all())
        ccs_list = CountryCasinoSetting.objects.all().filter(casino_ccs__id=slug)
        context.update({'linksDefault': linksDefault, })

    # Template
    temp = 'topadmin/casinoedit.html'

    # Forms
    formMain = CasinoMainForm(instance=casino)
    formDefault = CasinoDefaultForm(instance=casino)
    formNewCCS = CCSForm()
    formNewLink = LinkForm(request.user)
    formsAllCCS = []

    payment_all = []
    payment_top = []

    payment_top_default = Payment.objects.filter(tpp_payment__casino=casino,
                                                 tpp_payment__country__slug='Default').order_by(
        'tpp_payment__position')
    payment_all_default = Payment.objects.exclude(tpp_payment__casino=casino,
                                                  tpp_payment__country__slug='Default').order_by(
        'name')

    for ccs in ccs_list:
        payment_top_ccs = Payment.objects.filter(tpp_payment__casino=casino,
                                                 tpp_payment__country=ccs.country).order_by('tpp_payment__position')
        payment_top.append(payment_top_ccs)

        payment_all_ccs = Payment.objects.order_by('name')

        payment_all.append(payment_all_ccs)

        links = ccs.link.all().filter(source__in=request.user.profile.permission.all())
        ccs_box = [ccs, CCSForm(instance=ccs), links]
        formsAllCCS.append(ccs_box)

    # POST request
    if request.method == "POST":
        if slug != 'new':
            tpc_list = TopPositionCasino.objects.all().filter(casino__id=slug)
            top_names = []
            for tpc in tpc_list:
                new_historic_record(tpc.nameTop)
                tpc.nameTop.thing_modified1 = "Изменение в: %s (%s)" % (casino.name, request.user.username)
                tpc.nameTop.date_modified1 = datetime.now()
                tpc.nameTop.save()
        if request.POST.get('form') == 'main':
            form = CasinoMainForm(request.POST, request.FILES, instance=casino)
            if form.is_valid():
                casino = form.save()
                casino.save()
            else:
                context = {'casino': casino, 'linksDefault': linksDefault, 'payment_top_default': payment_top_default,
                           'payment_all_default': payment_all_default,
                           'payment_top': payment_top, 'payment_all': payment_all, 'ccs_list': ccs_list,
                           'formMain': form,
                           'formDefault': formDefault, 'formNewCCS': formNewCCS, 'formsAllCCS': formsAllCCS,
                           'formNewLink': formNewLink}
                return render(request, temp, context)
        if request.POST.get('form') == 'default-link':
            form = LinkForm(request.user, request.POST)
            source = request.POST.get('source')
            top = request.POST.get('top')
            link_quryset = Link.objects.all().filter(casino_link__id=slug, source=source, top=top)
            if link_quryset.exists():
                linkError = 'У источника уже есть ссылка в этом топе'
                context = {'casino': casino, 'linksDefault': linksDefault, 'payment_top_default': payment_top_default,
                           'payment_all_default': payment_all_default,
                           'payment_top': payment_top, 'payment_all': payment_all, 'ccs_list': ccs_list,
                           'formMain': formMain,
                           'formDefault': formDefault, 'formNewCCS': formNewCCS, 'formsAllCCS': formsAllCCS,
                           'formNewLink': form, 'linkError': linkError}
                return render(request, temp, context)
            if form.is_valid():
                link = form.save()
                link.save()
                casino.link.add(link)
                casino.save()
            else:
                context = {'casino': casino, 'linksDefault': linksDefault, 'payment_top_default': payment_top_default,
                           'payment_all_default': payment_all_default,
                           'payment_top': payment_top, 'payment_all': payment_all, 'ccs_list': ccs_list,
                           'formMain': formMain,
                           'formDefault': formDefault, 'formNewCCS': formNewCCS, 'formsAllCCS': formsAllCCS,
                           'formNewLink': form}
                return render(request, temp, context)
        if request.POST.get('form') == 'default':
            form = CasinoDefaultForm(request.POST, instance=casino)
            if form.is_valid():
                casino = form.save()
                casino.save()
            else:
                context = {'casino': casino, 'linksDefault': linksDefault, 'payment_top_default': payment_top_default,
                           'payment_all_default': payment_all_default,
                           'payment_top': payment_top, 'payment_all': payment_all, 'ccs_list': ccs_list,
                           'formMain': formMain,
                           'formDefault': form, 'formNewCCS': formNewCCS, 'formsAllCCS': formsAllCCS,
                           'formNewLink': formNewLink}
                return render(request, temp, context)
        if request.POST.get('form') == 'newCCS':
            form = CCSForm(request.POST)
            country = request.POST.get('country')
            ccs_quryset = CountryCasinoSetting.objects.all().filter(casino_ccs__id=slug, country=country)
            if ccs_quryset.exists():
                ccsError = 'Такое гео уже существует у этого казино'
                context = {'casino': casino, 'linksDefault': linksDefault, 'payment_top_default': payment_top_default,
                           'payment_all_default': payment_all_default,
                           'payment_top': payment_top, 'payment_all': payment_all, 'ccs_list': ccs_list,
                           'formMain': formMain,
                           'formDefault': formDefault, 'formNewCCS': form, 'formsAllCCS': formsAllCCS,
                           'formNewLink': formNewLink, 'ccsError': ccsError}
                return render(request, temp, context)
            elif form.is_valid():
                ccs = form.save()
                casino.country.add(ccs)
                casino.save()
            else:
                context = {'casino': casino, 'linksDefault': linksDefault, 'payment_top_default': payment_top_default,
                           'payment_all_default': payment_all_default,
                           'payment_top': payment_top, 'payment_all': payment_all, 'ccs_list': ccs_list,
                           'formMain': formMain,
                           'formDefault': formDefault, 'formNewCCS': form, 'formsAllCCS': formsAllCCS,
                           'formNewLink': formNewLink, 'ccsError': ccsError}
                return render(request, temp, context)
        if request.POST.get('form') == 'ccs':
            ccs_id = request.POST.get('ccs-id')
            ccs = CountryCasinoSetting.objects.get(id=ccs_id)
            form = CCSForm(request.POST, instance=ccs)
            if form.is_valid():
                ccs = form.save()
                ccs.save()
            else:
                context = {'casino': casino, 'linksDefault': linksDefault, 'payment_top_default': payment_top_default,
                           'payment_all_default': payment_all_default,
                           'payment_top': payment_top, 'payment_all': payment_all, 'ccs_list': ccs_list,
                           'formMain': formMain,
                           'formDefault': formDefault, 'formNewCCS': form, 'formsAllCCS': formsAllCCS,
                           'formNewLink': formNewLink}
                return render(request, temp, context)
        if request.POST.get('form') == 'ccs-link':
            ccs_id = request.POST.get('ccs-id')
            top = request.POST.get('top')
            ccs = CountryCasinoSetting.objects.get(id=ccs_id)
            form = LinkForm(request.user, request.POST)
            source = request.POST.get('source')
            link_quryset = Link.objects.all().filter(ccs_link__id=ccs.id, source=source, top=top)
            if link_quryset.exists():
                linkError = 'У источника уже есть ссылка на этом гео в этом топе'
                context = {'casino': casino, 'linksDefault': linksDefault, 'payment_top_default': payment_top_default,
                           'payment_all_default': payment_all_default,
                           'payment_top': payment_top, 'payment_all': payment_all, 'ccs_list': ccs_list,
                           'formMain': formMain,
                           'formDefault': formDefault, 'formNewCCS': formNewCCS, 'formsAllCCS': formsAllCCS,
                           'formNewLink': form, 'linkError': linkError}
                return render(request, temp, context)
            if form.is_valid():
                link = form.save()
                link.save()
                ccs.link.add(link)
                ccs.save()
            else:
                context = {'casino': casino, 'linksDefault': linksDefault, 'payment_top_default': payment_top_default,
                           'payment_all_default': payment_all_default,
                           'payment_top': payment_top, 'payment_all': payment_all, 'ccs_list': ccs_list,
                           'formMain': formMain,
                           'formDefault': formDefault, 'formNewCCS': formNewCCS, 'formsAllCCS': formsAllCCS,
                           'formNewLink': form}
                return render(request, temp, context)
        return redirect('casinoedit', slug=casino.id)

    # Context
    context.update(
        {'casino': casino, 'payment_top_default': payment_top_default, 'payment_all_default': payment_all_default,
         'payment_top': payment_top, 'payment_all': payment_all, 'ccs_list': ccs_list, 'formDefault': formDefault,
         'formMain': formMain, 'formNewCCS': formNewCCS, 'formsAllCCS': formsAllCCS, 'formNewLink': formNewLink, })
    return render(request, temp, context)


@login_required
def topedit(request, slug):
    slug = slug
    if slug == 'new':
        nameTop = NameTop()
    else:
        nameTop = get_object_or_404(NameTop, slug=slug)

    temp = 'topadmin/topedit.html'

    # POST request
    if request.method == "POST":
        if nameTop.design == 'new':
            form = TopFormNewTop(request.user, request.POST, request.FILES, instance=nameTop)

        elif nameTop.design == 'betting':
            form = TopFormBetting(request.user, request.POST, request.FILES, instance=nameTop)

        elif nameTop.design == 'top4':
            form = TopFormTop4(request.user, request.POST, request.FILES, instance=nameTop)

        elif nameTop.design == 'top3' or nameTop.design == 'top3-light':
            form = TopFormTop3(request.user, request.POST, request.FILES, instance=nameTop)

        elif nameTop.design == 'old':
            form = TopFormOldTop(request.user, request.POST, request.FILES, instance=nameTop)

        if form.has_changed():
            new_historic_record(nameTop)
            nameTop.thing_modified1 = "Настройки: %s (%s)" % (
                ", ".join(historic_top_check(form.changed_data)), request.user.username)
            nameTop.date_modified1 = datetime.now()
        if form.is_valid():
            nameTop = form.save()
            nameTop.save()
        return redirect('topedit', slug=nameTop.slug)

    # Top Position Casinos get
    # tpc = get_list_or_404(TopPositionCasino.objects.order_by('position'), nameTop__slug = slug)
    tpc = TopPositionCasino.objects.all().filter(nameTop__slug=slug).order_by('position')

    # Casinos in top and all casinos get
    casinos_top = Casino.objects.all().filter(tpc_casino__nameTop__slug=slug).order_by('tpc_casino__position')
    casinos_all = Casino.objects.all().exclude(tpc_casino__nameTop__slug=slug).order_by('name')

    # Top Form
    if nameTop.design == 'new':
        form = TopFormNewTop(request.user, instance=nameTop)

    elif nameTop.design == 'betting':
        form = TopFormBetting(request.user, instance=nameTop)

    elif nameTop.design == 'top4':
        form = TopFormTop4(request.user, instance=nameTop)

    elif nameTop.design == 'top3' or nameTop.design == 'top3-light':
        form = TopFormTop3(request.user, instance=nameTop)

    elif nameTop.design == 'old':
        form = TopFormOldTop(request.user,  instance=nameTop)

    # postback params
    postbacks = Postback.objects.all()
    params = ''
    for postback in postbacks:
        if params != '':
            params += '&'
        if postback.name == 'utm_term':
            params += postback.name + '=' + '{keyword}'
        else:
            params += postback.name + '=' + '{subid}'

    # Context
    context = {'top': nameTop, 'casinos_top': casinos_top, 'casinos_all': casinos_all, 'form': form, 'params': params}
    return render(request, temp, context)


@csrf_exempt
@login_required
def position(request, slug):
    nameTop = get_object_or_404(NameTop, slug=slug)
    if request.method == "POST":
        array_casino_id = request.POST.get('array_casino_id')
        array_casino_id = json.loads(array_casino_id)

        delete_casino_id = request.POST.get('delete_casino_id')
        if delete_casino_id:
            casino = get_object_or_404(Casino, id=int(delete_casino_id))
            new_historic_record(nameTop)
            nameTop.thing_modified1 = "Удаление из топа: %s (%s)" % (casino.name, request.user.username)
            nameTop.date_modified1 = datetime.now()
            nameTop.save()
            tcp = TopPositionCasino.objects.get(casino__id=int(delete_casino_id), nameTop__slug=slug)
            tcp.delete()
            return JsonResponse('ok', safe=False)
        else:
            new_historic_record(nameTop)
            nameTop.thing_modified1 = "Смена позиций (%s)" % request.user.username
            nameTop.date_modified1 = datetime.now()
            nameTop.save()
        for index, value in enumerate(array_casino_id):
            try:
                tcp = TopPositionCasino.objects.get(casino__id=int(value), nameTop__slug=slug)
                tcp.position = int(index)
                tcp.save()
            except:
                tcp_new = TopPositionCasino(position=index)
                tcp_new.casino = Casino.objects.get(id=int(value))
                tcp_new.nameTop = NameTop.objects.get(slug=slug)
                tcp_new.save()
        return JsonResponse('ok', safe=False)
    return redirect('topadmin')


@csrf_exempt
@login_required
def payment_position(request, slug):
    casino = get_object_or_404(Casino, id=slug)
    if request.method == "POST":
        array_payment_id = request.POST.get('array_payment_id')
        array_payment_id = json.loads(array_payment_id)

        delete_payment_id = request.POST.get('delete_payment_id')

        country_slug = request.POST.get('country_slug')
        if country_slug is None:
            country_slug = 'Default'

        if delete_payment_id:
            payment = get_object_or_404(Payment, id=int(delete_payment_id))
            tcp = TopPositionPayment.objects.get(payment=payment, casino=casino, country__slug=country_slug)
            tcp.delete()
            return JsonResponse('ok', safe=False)

        for index, value in enumerate(array_payment_id):
            try:
                tpp = TopPositionPayment.objects.get(casino=casino, payment__id=int(value), country__slug=country_slug)
                tpp.position = int(index)
                tpp.save()
            except:
                tpp_new = TopPositionPayment(position=index)
                tpp_new.payment = Payment.objects.get(id=int(value))
                print(tpp_new.payment)
                tpp_new.casino = get_object_or_404(Casino, id=slug)
                print(tpp_new.casino)
                tpp_new.country = get_object_or_404(Country, slug=country_slug)
                print(tpp_new.country)
                tpp_new.save()
                print(tpp_new)
        return JsonResponse('ok', safe=False)

    return redirect('topadmin')


# FUNCTIONS


def clone_creator(obj, slug, count=1):
    clone = obj.objects.get(slug=slug)
    try:
        new_slug = slug + '-clone' + str(count)
        old_clone = obj.objects.get(slug=new_slug)
        count = count + 1
        clone_creator(obj, slug, count)
    except:
        clone.pk = None
        clone.name += ' clone' + str(count)
        clone.thing_modified5 = None
        clone.thing_modified4 = None
        clone.thing_modified3 = None
        clone.thing_modified2 = None
        clone.thing_modified1 = None
        clone.date_modified5 = None
        clone.date_modified4 = None
        clone.date_modified3 = None
        clone.date_modified2 = None
        clone.date_modified1 = None
        clone.save()
        clone.mails.clear()
        clone.save()
        tpc = TopPositionCasino.objects.all().filter(nameTop__slug=slug)
        for item in tpc:
            item.pk = None
            item.nameTop = clone
            item.save()


def casino_clone_creator(obj, id, count=1):
    clone = obj.objects.get(id=id)
    try:
        new_id = id + '-clone' + str(count)
        old_clone = obj.objects.get(id=new_id)
        count = count + 1
        casino_clone_creator(obj, id, count)
    except:
        clone.pk = None
        clone.name += ' clone' + str(count)
        clone.save()


def linkbuilder(link, postbacks):
    linkparams_tosharp_list = link.split('#')
    linkparams = linkparams_tosharp_list[0]
    if len(linkparams_tosharp_list) == 1:
        tosharp = ''
    elif len(linkparams_tosharp_list) == 2:
        tosharp = '#' + linkparams_tosharp_list[1]
    else:
        tosharp = '#' + '#'.join(linkparams_tosharp_list[1:])

    linkpure_params = linkparams.split('?')
    linkpure = linkpure_params[0]
    if link.endswith('/'):
        link = link
    else:
        link = link + '/'
    if len(linkpure_params) == 1:
        params = ''
        if postbacks == '':
            linkfull = linkpure + tosharp
        else:
            linkfull = linkpure + '?' + postbacks + tosharp
    elif len(linkpure_params) == 2:
        params = linkpure_params[1]
        if postbacks == '':
            linkfull = linkpure + '?' + params + tosharp
        else:
            linkfull = linkpure + '?' + params + '&' + postbacks + tosharp
    else:
        params = '&'.join(linkparams_tosharp_list[1:])
        linkfull = linkpure + '?' + params + '&' + postbacks + tosharp

    return linkfull


def historic_top_check(arr):
    verbose_names = []
    for field_name in arr:
        if field_name == 'name':
            verbose_names.append('Название')
        if field_name == 'design':
            verbose_names.append('Дизайн')
        if field_name == 'country':
            verbose_names.append('Гео')
        # if field_name == 'theme':
        # 	verbose_names.append('Тема')
        if field_name == 'header':
            verbose_names.append('Заголовок в шапке')
        if field_name == 'text':
            verbose_names.append('Текст (description)')
        if field_name == 'promo1':
            verbose_names.append('Текст в шапке (верх)')
        if field_name == 'promo2':
            verbose_names.append('Текст в шапке (низ)')
        if field_name == 'hide_link':
            verbose_names.append('Прикрытие ссылок')
        if field_name == 'tr_play':
            verbose_names.append('Текст на КНОПКЕ')
        if field_name == 'tr_bonus':
            verbose_names.append('Текст БОНУС')
        if field_name == 'tr_fs':
            verbose_names.append('Текст ФРИ СПИНЫ')
        if field_name == 'tr_cashback':
            verbose_names.append('Текст КЭШБЭК')
        if field_name == 'tr_info':
            verbose_names.append('Текст СИЛЬНЫЕ СТОРОНЫ')
        if field_name == 'tr_license':
            verbose_names.append('Текст ЛИЦЕНЗИЯ')
        if field_name == 'tr_md':
            verbose_names.append('Текст МИН ДЕПОЗИТ')
        if field_name == 'tr_pay':
            verbose_names.append('Текст ПЛАТЕЖКИ')
        if field_name == 'tr_score':
            verbose_names.append('Текст БАЛЛЫ')
        if field_name == 'tr_votes':
            verbose_names.append('Текст ГОЛОСА')
        if field_name == 'tr_bottom':
            verbose_names.append('Текст ВНИЗУ СТРАНИЦЫ')
        if field_name == 'tr_copy':
            verbose_names.append('Текст Все права защищены')
        if field_name == 'tr_warning':
            verbose_names.append('Текст ПРЕДУПРЕЖДЕНИЕ В САМОМ НИЗУ')
    return verbose_names


def new_historic_record(top):
    top.thing_modified5 = top.thing_modified4
    top.thing_modified4 = top.thing_modified3
    top.thing_modified3 = top.thing_modified2
    top.thing_modified2 = top.thing_modified1
    top.date_modified5 = top.date_modified4
    top.date_modified4 = top.date_modified3
    top.date_modified3 = top.date_modified2
    top.date_modified2 = top.date_modified1


# @login_required
# def add_tpp(request):
#     all_casinos = Casino.objects.all()
#
#     default_country = get_object_or_404(Country, slug='Default')
#
#     for casino in all_casinos:
#         # for country in casino.country.all():
#         for payment in enumerate(casino.pay.all()):
#             add_payments(casino, default_country, payment[1], payment[0])
#
#     return render(request)


def add_payments(casino, country, payment, position):
    tpp = TopPositionPayment(casino=casino, country=country, payment=payment, position=position)
    tpp.save()
