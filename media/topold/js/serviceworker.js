var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/pl/',
    '/en/',
    '/media/css/style.css',
    '/media/css/style_home.css',
    '/media/css/bootstrap.min.css',
    '/media/images/favicons/favicon.ico',
    '/media/images/favicons/apple-icon.png',
    '/media/images/favicons/ms-icon-70x70.png',
    '/media/images/favicons/ms-icon-144x144.png',
    '/media/images/favicons/ms-icon-150x150.png',
    '/media/images/favicons/ms-icon-310x310.png',
    '/media/images/favicons/android-icon-36x36.png',
    '/media/images/favicons/android-icon-48x48.png',
    '/media/images/favicons/android-icon-72x72.png',
    '/media/images/favicons/android-icon-96x96.png',
    '/media/images/favicons/android-icon-144x144.png',
    '/media/images/favicons/android-icon-192x192.png',
    '/media/images/favicons/maskable-icon-512x512.png',
    '/media/images/favicons/apple-icon-57x57.png',
    '/media/images/favicons/apple-icon-60x60.png',
    '/media/images/favicons/apple-icon-72x72.png',
    '/media/images/favicons/apple-icon-76x76.png',
    '/media/images/favicons/apple-icon-114x114.png',
    '/media/images/favicons/apple-icon-120x120.png',
    '/media/images/favicons/apple-icon-144x144.png',
    '/media/images/favicons/apple-icon-152x152.png',
    '/media/images/favicons/apple-icon-180x180.png',
    '/media/images/favicons/favicon-16x16.png',
    '/media/images/favicons/favicon-32x32.png',
    '/media/images/favicons/favicon-96x96.png',
	'/media/js/popper.min.js',
	'/media/js/bootstrap.min.js',
	'/media/js/main.js',
	'/media/upload/img/logos/boomerang_KLmEyMf.png.70x0_q85.png',
	'/media/images/stuck-gift.svg',
	'/media/img/logo.png',
	'/media/images/countries/pl.svg',
	'/media/upload/img/logos/boomerang_KLmEyMf.png.0x200_q85.png',
	'/media/img_home/star.svg',
	'/media/img_home/gift.svg',
	'/media/img_home/repeat.svg',
	'/media/img/license/1.png',
	'/media/upload/img/pay/astropay_iEIUraJ.png',
	'/media/upload/img/pay/ripple_LbAo6Yx.png',
	'/media/upload/img/pay/trustly_1vdOPRI.png',
	'/media/upload/img/pay/visa-mastercard-maestro_mJu6mMF.png',
	'/media/upload/img/pay/bitcoin_CGIetdJ.png',
	'/media/upload/img/pay/ecopayz_8yuIFtD.png',
	'/media/upload/img/pay/etherium_tMPPU2Z.png',
	'/media/upload/img/pay/litecoin_uJhOYfo.png',
	'/media/upload/img/pay/neosurf_2P1xDwx.png',
	'/media/upload/img/logos/light_rniCmFe.png.0x200_q85.png',
	'/media/img/license/2.png',
	'/media/upload/img/pay/klarna_BddsVyc.png',
	'/media/upload/img/logos/Casino-Buck-logo3-1.png.0x200_q85.png',
	'/media/upload/img/pay/paysafe-w_2QJmCHh.png',
	'/media/upload/img/pay/neteller_sNEUAJM.png',
	'/media/upload/img/pay/scrill_cJ4ipRv.png',
	'/media/upload/img/logos/4021_500x250_dark.png.0x200_q85.png',
	'/media/upload/img/pay/jeton_JYAYn4O.png',
	'/media/upload/img/pay/ezeewallet_VLngv3D.png',
	'/media/upload/img/logos/gslot.png.0x200_q85.png',
	'/media/upload/img/logos/20Bet-500x500_dark.png.0x200_q85.png',
	'/media/upload/img/pay/discover_85FUm36.png',
	'/media/upload/img/pay/interac.png',
	'/media/upload/img/pay/perfect-money_2CLEkQx.png',
	'/media/upload/img/logos/wazamba_1ungyWY.png.0x200_q85.png',
	'/media/upload/img/logos/zula.png.0x200_q85.png',
	'/media/upload/img/logos/22bet_YPZxgvA.png.0x200_q85.png',
	'/media/upload/img/logos/campobet.png.0x200_q85.png',
	'/media/upload/img/logos/cadoola_qvx9s9E.png.0x200_q85.png',
	'/media/upload/img/logos/alf_fzL6brP.png.0x200_q85.png',
	'/media/upload/img/logos/nomini2.png.0x200_q85.png',
	'/media/upload/img/logos/yoyo_14mcRgp.png.0x200_q85.png',
	'/media/upload/img/logos/casinia.png.0x200_q85.png',
	'/media/upload/img/logos/boaboa_exW90lp.png.0x200_q85.png',
	'/media/upload/img/pay/mifinity_pKLDBle.png',
	'/media/upload/img/logos/betinia-2222.png.0x200_q85.png',
	'/media/upload/img/pay/muchbetter_nlDxvsJ.png',
	'/media/upload/img/pay/rapid_4Oa96cD.png',
	'/media/upload/img/logos/malina_eaCrcdd.png.0x200_q85.png',
	'/media/upload/img/logos/burancasino.png.0x200_q85.png',
	'/media/upload/img/logos/rabona_w1jrZ7f.png.0x200_q85.png',
	'/media/upload/img/logos/librabet_pVuI8hx.png.0x200_q85.png',
	'/media/upload/img/logos/cadabrus.png.0x200_q85.png',
	'/media/upload/img/soft/ainswors.png',
	'/media/upload/img/soft/amatic.png',
	'/media/upload/img/soft/blueprint.png',
	'/media/upload/img/soft/castech.png',
	'/media/upload/img/soft/egt.png',
	'/media/upload/img/soft/microgaming.png',
	'/media/upload/img/soft/netent.png',
	'/media/upload/img/soft/playson.png',
	'/media/upload/img/soft/quickspin.png',
	'/media/upload/img/soft/pragmaticplay.png',
	'/media/upload/img/soft/spin.png',
	'/media/upload/img/soft/wazdan.png',
	'/media/upload/img/soft/ygg.png',
	'/media/upload/img/soft/softbet.png',
	'/media/upload/img/soft/pushgaming.png',
	'/media/upload/img/soft/evoplay.png',
	'/media/upload/img/soft/nolimitcity.png',
	'/media/upload/img/soft/bgaming.png',
	'/media/upload/img/soft/betsoft.png',
	'/media/upload/img/soft/spin_EapZh4c.png',
	'/media/upload/img/soft/felix.png',
	'/media/upload/img/soft/blablabla.png',
	'/media/upload/img/soft/nucleus.png',
	'/media/upload/img/soft/playngo.png',
	'/media/img_home/top.png',
	'/media/images/header1.svg',
	'/media/images/telka.png',
	'/media/images/1440_stick.svg',
	'/media/img_home/gold.png',
	'/media/img/bg/yellow_bg.jpg',
	'/media/img_home/like.svg',
	'/media/img_home/silver.png',
	'/media/img/bg/blue_bg.jpg',
	'/media/img_home/bronze.png',
	'/media/img/bg/azure_bg.jpg',
	'/media/img/bg/green_bg.jpg',
	'/media/img/bg/red_bg.jpg',
	'/media/img/bg/purple_bg.jpg',
	'/media/img/bg/orange_bg.jpg',
]


// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();

    event.waitUntil(
        caches.open(staticCacheName).then(cache => {
            return cache.addAll(filesToCache);
        })
    );
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('offline');
            })
    )
});
