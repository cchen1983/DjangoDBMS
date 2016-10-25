from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^init/', views.index, name="workflow"),
    url(r'^reg-form-view/', views.reg_form_view, name="reg-form-view"),
    url(r'^add-new-member/', views.add_new_member, name="add-new-member"),
    url(r'^member-recharge/', views.member_recharge, name="member-recharge"),
    url(r'^exp-product-reg/', views.exp_product_reg, name="exp-product-reg"),
    url(r'^exp-other-reg/', views.exp_other_reg, name="exp-other-reg"),
    url(r'^check-membership/', views.check_membership, name="check-membership"),
    url(r'^purc-reg/', views.purc_reg, name="purc-reg"),
    url(r'^act-promo-reg/', views.act_promo_reg, name="act-promo-reg"),
    url(r'^act-discount-reg/', views.act_discount_reg, name="act-discount-reg"),
    url(r'^act-info-get/', views.act_info_get, name="act-info-get"),
]
