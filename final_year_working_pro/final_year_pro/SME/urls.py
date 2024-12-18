from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    BuyerSellerMatchListView, BuyerSellerMatchCreateView, 
    BuyerSellerMatchDetailView, BuyerSellerMatchUpdateView, 
    BuyerSellerMatchDeleteView, home_view
)
from .views import (
    signup_view, 
    profile_view, 
    login_view, 
    LogoutView
)
urlpatterns = [    path('', home_view, name='home'),

    path('signup/', signup_view, name='signup'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),  # Ensure this is correct

    # Profile Page
    path('profile/', profile_view, name='profile'),

    # Password Reset URLs (Django built-in views)
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'
         ), 
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ), 
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ), 
         name='password_reset_confirm'),
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ), 
         name='password_reset_complete'),

    path('matches/', BuyerSellerMatchListView.as_view(), name='buyer_seller_match_list'),
    path('matches/create/', BuyerSellerMatchCreateView.as_view(), name='buyer_seller_match_create'),
    path('matches/<int:pk>/', BuyerSellerMatchDetailView.as_view(), name='buyer_seller_match_detail'),
    path('matches/<int:pk>/update/', BuyerSellerMatchUpdateView.as_view(), name='buyer_seller_match_update'),
    path('matches/<int:pk>/delete/', BuyerSellerMatchDeleteView.as_view(), name='buyer_seller_match_delete'),
    # Dashboard
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    # Company URLs
    path('companies/', views.CompanyListView.as_view(), name='company_list'),
    path('companies/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('companies/create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('companies/<int:pk>/update/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('companies/<int:pk>/delete/', views.CompanyDeleteView.as_view(), name='company_delete'),

   path('seller-profile/', views.SellerProfileDetailView.as_view(), name='seller_profile'),
    path('seller-profile/update/', views.SellerProfileUpdateView.as_view(), name='seller_profile_update'),

    # Supplier Profile URLs
    path('supplier-profile/', views.SupplierProfileDetailView.as_view(), name='supplier_profile'),
    path('supplier-profile/update/', views.SupplierProfileUpdateView.as_view(), name='supplier_profile_update'),
    # Raw Material URLs
    path('raw-materials/', views.RawMaterialListView.as_view(), name='raw_material_list'),
    path('raw-materials/<int:pk>/', views.RawMaterialDetailView.as_view(), name='raw_material_detail'),
    path('raw-materials/create/', views.RawMaterialCreateView.as_view(), name='raw_material_create'),
    path('raw-materials/<int:pk>/update/', views.RawMaterialUpdateView.as_view(), name='raw_material_update'),
    path('raw-materials/<int:pk>/delete/', views.RawMaterialDeleteView.as_view(), name='raw_material_delete'),

    # Company Requirement URLs
    path('requirements/', views.CompanyRequirementListView.as_view(), name='company_requirement_list'),
    path('requirements/create/', views.CompanyRequirementCreateView.as_view(), name='company_requirement_create'),

    # Seller Product URLs
    path('seller-products/', views.SellerProductListView.as_view(), name='seller_product_list'),
    path('seller-products/create/', views.SellerProductCreateView.as_view(), name='seller_product_create'),

    # Supplier Product URLs
    path('supplier-products/', views.SupplierProductListView.as_view(), name='supplier_product_list'),
    path('supplier-products/create/', views.SupplierProductCreateView.as_view(), name='supplier_product_create'),

    # Order URLs
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/<uuid:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order_create'),

    # Review URLs
    path('reviews/create/', views.ReviewCreateView.as_view(), name='review_create'),

    # Supplier Review URLs
    path('supplier-reviews/create/', views.SupplierReviewCreateView.as_view(), name='supplier_review_create'),

    # Communication URLs
    path('whatsapp/send/', views.WhatsAppMessageCreateView.as_view(), name='whatsapp_send'),
    path('phone-call/log/', views.PhoneCallCreateView.as_view(), name='phone_call_log'),
    path('email/send/', views.EmailCommunicationCreateView.as_view(), name='email_send'),

    # User Communication Preference URLs
    path('communication-preferences/', views.UserCommunicationPreferenceUpdateView.as_view(), name='communication_preferences'),

    # Advanced Feature URLs
    path('product-search/', views.ProductSearchView.as_view(), name='product_search'),
    path('bulk-upload/', views.BulkRawMaterialUploadView.as_view(), name='bulk_raw_material_upload'),
    path('reports/', views.DateRangeReportView.as_view(), name='date_range_report'),

    # Cart URLs
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),

    # Wishlist URLs
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.AddToWishlistView.as_view(), name='add_to_wishlist'),
    path('wishlist/remove/<int:wishlist_item_id>/', views.RemoveFromWishlistView.as_view(), name='remove_from_wishlist'),

    # API URLs for AJAX requests
    path('api/product-autocomplete/', views.ProductAutocompleteView.as_view(), name='product_autocomplete'),
    path('api/order/<uuid:order_id>/update-status/', views.OrderStatusUpdateView.as_view(), name='order_status_update'),
]

handler404 = 'your_app_name.views.handler404'
handler500 = 'your_app_name.views.handler500'