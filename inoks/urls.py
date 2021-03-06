from django.conf.urls import url
from django.urls import path

from inoks.Views import ProductViews, UserViews, OrderViews, ReportViews, EarningsViews, DashboardViews, SettingViews, \
    TreeViews, RefundViews, CityViews, APIViews, HomeViews, CouponViews, CheckoutViews, PaymentMethodViews, \
    DiscountViews, CommentViews, FavoriteViews, OptionViews

app_name = 'inoks'

urlpatterns = [
    # HOME

    path('', HomeViews.get_home_product, name='kullanici-urun-sayfasi'),
    url(r'product/(?P<slug>[-\w\d]+)/$', HomeViews.get_category_products, name='kategori-urunleri'),
    url(r'brand/(?P<slug>[-\w\d]+)/$', HomeViews.get_brand_products, name='markanin-urunleri'),
    url(r'detail/(?P<slug>[-\w\d]+)/$', HomeViews.get_product_detail, name='urun-detay'),
    url(r'search/$', HomeViews.search_category, name='search'),
    url(r'corporate/$', HomeViews.get_corporate, name='corporate'),

    # Dashboard
    url(r'dashboard/admin-dashboard/$', DashboardViews.return_admin_dashboard, name='admin-dashboard'),
    url(r'dashboard/user-dashboard/$', DashboardViews.return_user_dashboard, name='user-dashboard'),
    url(r'dashboard/admin-dashboard/sil/(?P<pk>\d+)$', DashboardViews.pending_profile_delete,
        name='bekleyen-kullanicilar-sil'),
    url(r'dashboard/admin-dashboard/(?P<pk>\d+)$', DashboardViews.getPendingProfile, name='getPendingProfile'),
    url(r'bayi-onayla/$', DashboardViews.profile_active_passive, name="bayi-onayla"),
    url(r'dashboard/admin-dashboard/bekleyen-siparis-sil/(?P<pk>\d+)$', DashboardViews.pending_order_delete,
        name='bekleyen-siparisler-sil'),
    url(r'dashboard/admin-dashboard/pending-order/(?P<pk>\d+)$', DashboardViews.getPendingOrder,
        name='getPendingOrder'),
    url(r'siparis-onayla/$', DashboardViews.pendingOrderActive, name="siparis-onayla"),
    url(r'dashboard/user-dashboard/(?P<pk>\d+)$', DashboardViews.getMyOrder, name='getMyOrder'),

    # Bayi-Kullanici
    url(r'kullanici/bayi-ekle/$', UserViews.return_add_users, name='bayi-ekle'),
    url(r'kullanici/bayiler/$', UserViews.return_users, name='bayiler'),
    url(r'kullanici/uyelerim/$', UserViews.return_my_users, name='uyelerim'),
    url(r'kullanici/bekleyen-kullanicilar/$', UserViews.return_pending_users, name='bekleyen-kullanicilar'),
    url(r'kullanici/iptal-edilen-kullanicilar/$', UserViews.return_deactive_users, name='iptal-edilen-kullanicilar'),
    url(r'kullanici/bekleyen-kullanicilar/sil/(?P<pk>\d+)$', UserViews.pending_profile_delete,
        name='bekleyen-kullanicilar-sil'),
    url(r'kullanici-onayla/$', UserViews.profile_active_passive, name="kullanici-onayla"),
    url(r'kullanici-iptal-et/$', UserViews.profile_passive, name="bayi-iptal-et"),
    url(r'kullanici/bekleyen-kullanicilar/(?P<pk>\d+)$', UserViews.getPendingProfile, name='getPendingProfile'),
    url(r'kullanici/bayiler/(?P<pk>\d+)$', UserViews.getAllProfile, name='getAllProfile'),
    url(r'kullanici/iptal-edilen-kullanicilar/(?P<pk>\d+)$', UserViews.getDeactiveProfile, name='getDeactiveProfile'),
    url(r'kullanici-aktif-et/$', UserViews.profile_reactive, name="bayi-aktif-et"),
    url(r'kullanici/bayi-ekle/duzenle/(?P<pk>\d+)$', UserViews.users_update, name='bayi-duzenle'),
    url(r'kullanici/bayi-ekle/bayi-bilgileri/(?P<pk>\d+)$', UserViews.users_information,
        name='bayi-bilgileri-getir'),
    url(r'kullanici/bayi-bilgi-gonder/(?P<pk>\d+)$', UserViews.send_information, name='bayi-bilgi-gonder'),
    url(r'kullanici/bayi-kart-ekle/(?P<pk>\d+)$', UserViews.return_add_user_creditcart,
        name='bayi-kart-ekle'),
    url(r'kullanici/bayi-kart-guncelle/(?P<pk>\d+)$', UserViews.credit_card_update,
        name='bayi-kart-guncelle'),
    url(r'kullanici/bayi-kart-sil/(?P<pk>\d+)$', UserViews.credit_card_delete,
        name='bayi-kart-sil'),

    # Kulllanici
    url(r'account-register/$', UserViews.user_register, name='kullanici-ekle'),
    url(r'account-login/$', UserViews.user_login, name='kullanici-giris'),
    url(r'account-logout/$', UserViews.user_logout, name='kullanici-logout'),
    url(r'profile/$', UserViews.user_profil, name='kullanici-profil'),
    url(r'change-password/$', UserViews.user_change_password, name='sifre-guncelle'),
    url(r'order/$', UserViews.user_my_orders, name='kullanici-siparisleri'),
    url(r'new-address/$', UserViews.add_user_address, name='kullanici-adres-ekle'),
    url(r'address/$', UserViews.get_address, name='kullanici-adres-bilgileri'),
    url(r'delete-address/(?P<pk>\d+)$', UserViews.user_delete_address, name='kullanici-adres-sil'),
    url(r'address-update/(?P<pk>\d+)$', UserViews.user_address_update, name='kullanici-adres-guncelle'),
    url(r'refund/$', RefundViews.return_add_refund, name='kullanici-urun-iade-olustur'),
    url(r'products/(?P<pk>\d+)$', UserViews.user_products, name='siparis-urunleri'),

    # Urunler
    url(r'urunler/urun-ekle/$', ProductViews.return_add_products, name='urun-ekle'),
    url(r'urunler/urunler/$', ProductViews.return_products, name='urunler'),
    url(r'urunler/urun-kategori-ekle/$', ProductViews.return_add_product_category, name='urun-kategori-ekle'),
    url(r'urunler/urun-listesi/$', ProductViews.return_product_list, name='urun-listesi'),
    url(r'urunler/urun-listesi/sil/(?P<pk>\d+)$', ProductViews.product_delete, name='product-sil'),
    url(r'urunler/urunler/delete-image/$', ProductViews.product_image_delete, name='imageDelete'),
    url(r'urunler/urun-ekle/duzenle/(?P<pk>\d+)$', ProductViews.product_update, name='urun-duzenle'),
    url(r'urunler/urun-kategori-ekle/sil/(?P<pk>\d+)$', ProductViews.productCategory_delete,
        name='productCategory-sil'),
    url(r'urunler/urun-kategori-ekle/duzenle/(?P<pk>\d+)$', ProductViews.productCategory_update,
        name='urun-kategori-ekle-duzenle'),
    url(r'urunler/urun-listesi/(?P<pk>\d+)$', ProductViews.getProduct, name='getProduct'),
    url(r'urunler/urunler/(?P<pk>\d+)$', ProductViews.getProducts, name='getProducts'),
    url(r'urunler/marka-ekle/$', ProductViews.return_add_brand, name='marka-ekle'),
    url(r'urunler/marka-sil/(?P<pk>\d+)$', ProductViews.brand_delete, name='marka-sil'),
    url(r'urunler/grupla/(?P<group_id>\d+)$', ProductViews.add_products_to_group, name='urun-grupla'),
    url(r'urunler/grup-urun-sil/(?P<group_id>\d+)/(?P<product_id>\d+)$', ProductViews.delete_product_from_group,
        name='urun-grup-sil'),

    # SEÇENEKLER
    url(r'option/$', OptionViews.add_option, name='seçenek ekle'),
    url(r'type-values/$', OptionViews.get_typeValues, name='type-value-getir'),
    url(r'option-price/$', OptionViews.get_price_of_option, name='secenegin-fiyatını-getir'),
    url(r'option-product/(?P<pk>\d+)$', OptionViews.add_option_to_product, name='urune seçenek ekle'),

    # İNDİRİM
    url(r'indirim-uygula/(?P<pk>\d+)$', DiscountViews.discount, name='indirim uygula'),
    url(r'indirimli-urun-listesi/$', DiscountViews.getDiscount_products, name='indirimli urun listesi'),
    url(r'urunler/indirim/sil/(?P<pk>\d+)$', DiscountViews.discount_product_delete, name='indirim-sil'),

    # Stok
    url(r'urunler/stok-guncelle/$', ProductViews.stock_update, name='stok-guncelle'),

    # Kargo
    url(r'urunler/kargo-metotlari/$', OrderViews.get_cargo, name='kargo-metotlari'),
    url(r'urunler/kargo-guncelle/(?P<pk>\d+)$', OrderViews.cargo_update, name='kargo-guncelle'),

    # Siparisler
    url(r'siparisler/siparis-ekle/$', OrderViews.return_add_orders, name='siparis-ekle'),
    url(r'siparisler/admin-siparis-ekle/$', OrderViews.return_add_orders_admin, name='admin-siparis-ekle'),
    url(r'siparisler/bekleyen-siparisler/$', OrderViews.return_pending_orders, name='bekleyen-siparisler'),
    url(r'siparisler/siparislerim/$', OrderViews.return_my_orders, name='siparislerim'),
    url(r'siparisler/siparislerim/(?P<pk>\d+)$', OrderViews.getMyOrder, name='getMyOrder'),
    url(r'siparisler/siparisler/$', OrderViews.return_orders, name='siparisler'),
    url(r'siparisler/siparis-durumlari/$', OrderViews.return_order_situations, name='siparis-durumlari'),
    url(r'siparisler/bekleyen-siparisler/sil/(?P<pk>\d+)$', OrderViews.pending_order_delete,
        name='bekleyen-siparisler-sil'),
    url(r'siparisler/bekleyen-siparisler/(?P<pk>\d+)$', OrderViews.getPendingOrder, name='getPendingOrder'),
    url(r'siparis-onayla/$', OrderViews.pendingOrderActive, name="siparis-onayla"),
    url(r'siparisler/siparisler/sil/(?P<pk>\d+)$', OrderViews.orders_delete,
        name='siparislersil'),
    url(r'siparisler/siparisler/uye-siparis-sil/(?P<pk>\d+)$', OrderViews.orders_delete_member,
        name='uye-siparis-sil'),
    url(r'siparisler/siparisler/(?P<pk>\d+)$', OrderViews.getOrder, name='getOrder'),
    url(r'siparisler/sepet-siparis-ekle/$', OrderViews.return_add_orders_from_cart, name='kart-siparis-ekle'),
    url(r'siparis-durumu-guncelle/$', OrderViews.siparis_durumu_guncelle, name="siparis-durumu-guncelle"),
    url(r'kargo-bilgi/(?P<pk>\d+)$', OrderViews.kargoBilgi, name='kargo-bilgi'),
    url(r'siparis-detay/(?P<pk>\d+)$', OrderViews.get_admin_order_detail, name='admin-siparis-detay'),

    # İadeler
    url(r'iadeler/iade-olustur/$', RefundViews.return_add_refund, name='iade-olustur'),
    url(r'iadeler/iadeler/$', RefundViews.return_refunds, name='iadeler'),
    url(r'iadeler/iadelerim/$', RefundViews.return_my_refunds, name='iadelerim'),
    url(r'iadeler/iade-durumlari/$', RefundViews.return_refund_situations, name='iade-durumlari'),
    url(r'iadeler/iade-durumlari/sil/(?P<pk>\d+)$', RefundViews.refund_situations_delete, name='iade-durum-sil'),
    url(r'iadeler/iade-durumlari/duzenle/(?P<pk>\d+)$', RefundViews.refund_situations_update,
        name='iade-durum-duzenle'),
    url(r'iade-onayla/$', RefundViews.pendingRefundActive, name="iade-onayla"),
    url(r'iade-reddet/$', RefundViews.pendingRefundPassive, name="iade-reddet"),
    url(r'iadeler/bekleyen-iadeler/$', RefundViews.return_pendings_refunds, name='bekleyen-iadeler'),

    # Kullanıcı-İade
    url(r'kullanici/iade-olustur/$', UserViews.user_add_refund, name='kullanici-iade-olustur'),
    url(r'guest-user-refunds/$', UserViews.guest_my_refunds, name='misafir-kullanici-iadeleri'),
    url(r'kullanici/iadelerim/$', UserViews.user_my_refunds, name='kullanici-iadelerim'),

    # degerlendirme
    url(r'rating/(?P<pk>\d+)$', CommentViews.make_comment, name='kullanici-yorum-yap'),

    # favori urunler
    url(r'favorite-products/$', FavoriteViews.favorites, name='favori-urunler'),
    url(r'add-favorite/$', FavoriteViews.add_favorite_product, name='favori-urun-ekle'),
    url(r'remove-favorite/(?P<pk>\d+)$', FavoriteViews.delete_favorite_product, name='favori-urun-sil'),

    # Raporlar
    url(r'raporlar/rapor-olustur/$', ReportViews.return_create_report, name='rapor-olustur'),

    # Kazançlar
    url(r'kazanclar/kazanclar/$', EarningsViews.return_all_earnings_report, name='kazanclar'),
    url(r'kazanclar/kazanclarim/$', EarningsViews.return_my_earnings_report, name='kazanclarim'),
    url(r'kazanclar/odenecekler/$', EarningsViews.return_odenecekler, name='odenecekler'),
    url(r'kazanclar/odenenler/$', EarningsViews.return_odenenler, name='odenenler'),
    url(r'odeme-yap/$', EarningsViews.make_pay, name="odeme-yap"),

    # Ayarlar
    url(r'ayarlar/profil-ayarlari/$', SettingViews.return_profil_settings, name='profil-ayarlari'),
    url(r'ayarlar/sistem-ayarlari/$', SettingViews.return_system_settings, name='sistem-ayarlari'),
    url(r'sponsor-dogrula/$', SettingViews.sponsor_isexist, name="sponsor-dogrula"),
    url(r'kurumsal/$', SettingViews.return_corporate, name="kurumsal"),
    url(r'sozlesme/$', SettingViews.return_contract, name="sozlesme"),

    # IletisimBilgileri
    url(r'adres-bilgisi/$', SettingViews.return_address, name="iletisim"),
    url(r'mail-bilgisi/$', SettingViews.return_mail, name="iletisim"),
    url(r'telefon-bilgisi/$', SettingViews.return_phone, name="iletisim"),
    url(r'contact/$', SettingViews.return_contact, name="iletisim-formu"),

    # SoyAgacı
    url(r'soyagaci/soy-agacim/$', TreeViews.return_my_tree, name='soy-agacim'),
    url(r'soyagaci/soy-agaclari/$', TreeViews.return_all_tree, name='soy-agaclari'),

    # api
    url(r'ilce-getir/$', CityViews.get_districts, name="ilce-getir"),
    url(r'adres-bilgi/$', APIViews.get_address_info, name="adres-bilgi"),
    url(r'siparis/urun-bilgi-getir/$', APIViews.get_order_products.as_view(), name="siparis-urun-getir"),

    # odeme
    url(r'odeme-modul/(?P<siparis>\d+)$', OrderViews.odemeYap, name='odeme-yap'),
    url(r'odeme-bildirim/$', OrderViews.odeme_sonuc, name='odeme-sonuc'),
    url(r'odeme-bildirim-iyzico/$', OrderViews.odeme_sonuc_iyzico, name='odeme-sonuc-iyzico'),
    url(r'odeme-basarili/$', OrderViews.basarili_odeme, name='odeme-basarili'),
    url(r'odeme-basarisiz/$', OrderViews.basarisiz_odeme, name='basarisiz-odeme'),
    url(r'havale-eft-bilgi/(?P<siparis>\d+)$', OrderViews.havale_eft, name='havale-eft-bilgi'),

    # Odeme Yontemleri

    url(r'payment-method/payTr/(?P<pk>\d+)$', PaymentMethodViews.UpdatePaytr, name='payTr'),
    url(r'payment-method/bakiyem/(?P<pk>\d+)$', PaymentMethodViews.UpdateBakiyem, name='bakiyem'),
    url(r'payment-method/iyzico/(?P<pk>\d+)$', PaymentMethodViews.UpdateIyzico, name='iyzico'),
    url(r'payment-method/$', PaymentMethodViews.paymentMethod, name='payment-method'),
    url(r'payment-method-status/(?P<pk>\d+)$', PaymentMethodViews.paymentMethod_activity,
        name='odeme-yontemi-aktiflestir'),

    # checkout
    url(r'checkout/$', CheckoutViews.order_checkout, name='kullanici-checkout'),
    url(r'user-products/$', CheckoutViews.get_payment_info_isUser, name='checkout-odeme'),
    url(r'checkout-user/$', CheckoutViews.payment_info_isUser, name='odeme-tamamla-kayitli-kullanici'),
    url(r'guest-user-products/(?P<pk>\d+)$', CheckoutViews.get_payment_info_isGuest, name='checkout-odeme-guest'),

    url(r'guest/(?P<c_code>[-\w\d]+)/(?P<subtotal>[-\w\d]+)$', CheckoutViews.add_guest,
        name='misafir-kullanıcı-ekle'),
    url(r'checkout-guest-user/(?P<pk>\d+)/(?P<discount>\d+\.\d{2})/$', CheckoutViews.payment_info_isGuest,
        name='odeme-bilgileri-guest-user'),

    url(r'paytr/(?P<siparis>\d+)$', CheckoutViews.payment_payTr, name='payTr-make-creditCard-payment'),
    url(r'iyzico/(?P<siparis>\d+)$', CheckoutViews.payment_iyzico, name='iyzipay-make-creditcard-payment'),
    url(r'checkout/address/$', CheckoutViews.new_address, name='odeme-tamamla-yeni-adres'),

    # kupon
    url(r'kupon-bilgileri/$', CouponViews.coupon_create, name='kupon'),
    url(r'ödeme-bilgileri/$', CouponViews.review_payments, name='odeme'),
    url(r'kupon-aktifligi/(?P<pk>\d+)$', CouponViews.coupon_activity, name='kupon-aktiflestir'),
    url(r'kupon-sil/(?P<pk>\d+)$', CouponViews.coupon_delete, name='kupon-sil'),
    url(r'kupon-guncelle/(?P<pk>\d+)$', CouponViews.coupon_update, name='kupon-guncelle'),
    url(r'kupon-kontrol/$', CouponViews.coupon_control, name='kupon-kontrol'),

]
