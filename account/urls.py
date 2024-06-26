# urls.py (development only)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# from .views import send_email
# from . import views
# from .views import pricing_estimate_view
# from .views import send_test_email
# from .views import PricingEstimateCreateView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from .views import admin_change_password
from rest_framework.routers import DefaultRouter
from .views import (
    # CategoryViewSet,
    # TechnologyViewSet,
    # TestimonialViewSet,
    # ProjectViewSet,
    # ServiceViewSet,
    # BlogPostViewSet,
    # CourseViewSet,
    # CommentViewSet,
    # CompanyInformationViewSet,
    # TeamMemberViewSet,
    # AuthorViewSet,
    # ContactInquiryViewSet,
    # SendPasswordResetEmailView,
    UserChangePasswordView,
    UserLoginView,
    UserProfileView,
    # EventViewSet,
    # CaseViewSet,
    # CareerViewSet,
    # UpdateViewSet,
    # PricingEstimateViewSet,
    UserPasswordResetView,
    # QuestionsAnswerViewSet,
    # IndustryViewSet,
    # IndustriesWeServeViewSet,
    # CustomTokenObtainPairView,
    # AdminCreateAPIView,
    # AdminChangePasswordAPIView,
    
)
app_name = 'account'

router = DefaultRouter()


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategorieViewSet, BlogPostViewSet, ProjectViewSet, ServiceViewSet, TeamMemberViewSet,AboutUsViewSet,ContactUViewSet,ProductViewSet,PrivacyPolicyViewSet,TermsAndConditionsViewSet

router = DefaultRouter()
router.register(r'categories', CategorieViewSet, basename='categorie')
router.register(r'blogposts', BlogPostViewSet, basename='blogpost')
router.register(r'projects', ProjectViewSet,'project')
router.register(r'services', ServiceViewSet, basename='service')
# router.register(r'courses', CourseViewSet, basename='course')
router.register(r'teammembers', TeamMemberViewSet, basename='team_member')
router.register(r'aboutus', AboutUsViewSet, basename='aboutus')
router.register(r'contact_us', ContactUViewSet,basename='contactus')
router.register(r'products', ProductViewSet,basename='product')
router.register(r'privacy-policy', PrivacyPolicyViewSet, basename='privacy-policy')
router.register(r'terms-and-conditions', TermsAndConditionsViewSet, basename='terms-and-conditions')


urlpatterns = [
    path('api/', include(router.urls)),  # Corrected path (empty string '')
    path('api/categories/<int:pk>/', CategorieViewSet.as_view({'get': 'retrieve'}), name='categorie-detail'),
    path('api/blogposts/<int:pk>/', BlogPostViewSet.as_view({'get': 'retrieve'}), name='blogpost-detail'),
    path('api/projects/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve'}), name='project-detail'),
    path('api/services/<int:pk>/', ServiceViewSet.as_view({'get': 'retrieve'}), name='service-detail'),
    # path('api/courses/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve'}), name='course-detail'),
    path('api/teammembers/<int:pk>/', TeamMemberViewSet.as_view({'get': 'retrieve'}), name='team_member-detail'),
    path('api/aboutus/<int:pk>/', AboutUsViewSet.as_view({'get': 'retrieve'}), name='aboutus-detail'),
    path('api/contact-us/<int:pk>/', ContactUViewSet.as_view({'get': 'retrieve'}), name='contact-detail'),
    path('api/products/<int:pk>/',ProductViewSet.as_view({'get': 'retrieve'}), name='product-detail'),
    path('api/privacy-policy/<int:pk>/', PrivacyPolicyViewSet.as_view({'get': 'retrieve'}), name='privacy-policy-details'),
    path('api/terms-and-conditions/<int:pk>/', TermsAndConditionsViewSet.as_view({'get': 'retrieve'}), name='terms-and-conditions-details'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    # path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    # path('api/custom-token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/admin/create/', AdminCreateAPIView.as_view(), name='admin-create'),
    # path('api/admin/change-password/', AdminChangePasswordAPIView.as_view(), name='admin-change-password'),
    # path('send-email/', send_email, name='send_email'),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





# router.register(r'categories', CategoryViewSet, basename='categorie')
# router.register(r'events', EventViewSet, basename='event')
# router.register(r'cases', CaseViewSet, basename='case')
# router.register(r'careers', CareerViewSet, basename='career')
# router.register(r'updates', UpdateViewSet)
# router.register(r'pricing', PricingEstimateViewSet, basename='pricing')
# router.register(r'technologies', TechnologyViewSet, basename='technologie')
# router.register(r'testimonials', TestimonialViewSet, basename='testimonial')
# router.register(r'projects', ProjectViewSet, basename='project')
# router.register(r'services', ServiceViewSet, basename='service')
# router.register(r'blogposts', BlogPostViewSet, basename='blogpost')
# router.register(r'courses', CourseViewSet, basename='course')
# router.register(r'comments', CommentViewSet, basename='comment')
# router.register(r'companyinformation', CompanyInformationViewSet, basename='companyinformation')
# router.register(r'teammembers', TeamMemberViewSet, basename='teammember')
# router.register(r'authors', AuthorViewSet, basename='author')
# router.register(r'contactinquiries', ContactInquiryViewSet, basename='contactinquirie')
# router.register(r'questionanswers', QuestionsAnswerViewSet, basename='questionanswer')  # New registration
# router.register(r'industries', IndustryViewSet, basename = 'industrie')
# router.register(r'companies', IndustriesWeServeViewSet, basename='companies_we_server')



# urlpatterns = [
#     path('api/', include(router.urls)),  # Corrected path (empty string '')
#     path('api/projects/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve'}), name='project-detail'),
#     path('api/categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'}), name='category-detail'),
#     path('api/events/<int:pk>/', EventViewSet.as_view({'get': 'retrieve'}), name='event-detail'),
#     path('api/cases/<int:pk>/', CaseViewSet.as_view({'get': 'retrieve'}), name='case-detail'),
#     path('api/updates/<int:pk>/', UpdateViewSet.as_view({'get': 'retrieve'}), name='update-detail'),
#     path('api/careers/<int:pk>/', CareerViewSet.as_view({'get': 'retrieve'}), name='career-detail'),
#     path('api/pricing-estimates/<int:pk>/', PricingEstimateViewSet.as_view({'get': 'retrieve'}), name='pricing-detail'),
#     path('api/technologies/<int:pk>/', TechnologyViewSet.as_view({'get': 'retrieve'}), name='technology-detail'),
#     path('api/testimonials/<int:pk>/', TestimonialViewSet.as_view({'get': 'retrieve'}), name='testimonial-detail'),
#     path('api/services/<int:pk>/', ServiceViewSet.as_view({'get': 'retrieve'}), name='service-detail'),
#     path('api/blogposts/<int:pk>/', BlogPostViewSet.as_view({'get': 'retrieve'}), name='blogpost-detail'),
#     path('api/courses/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve'}), name='courses-detail'),
#     path('api/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve'}), name='comment-detail'),
#     path('api/companyinformation/<int:pk>/', CompanyInformationViewSet.as_view({'get': 'retrieve'}), name='companyinformation-detail'),
#     path('api/teammembers/<int:pk>/', TeamMemberViewSet.as_view({'get': 'retrieve'}), name='teammember-detail'),
#     path('api/authors/<int:pk>/', AuthorViewSet.as_view({'get': 'retrieve'}), name='author-detail'),
#     path('api/contactinquiries/<int:pk>/', ContactInquiryViewSet.as_view({'get': 'retrieve'}), name='contactinquiry-detail'),
#     path('api/questionanswers/<int:pk>/', QuestionsAnswerViewSet.as_view({'get': 'retrieve'}), name='questionanswer-detail'),
#     path('api/industries/<int:pk>/', IndustryViewSet.as_view({'get': 'retrieve'}), name='industry-details'),
#     path('api/companies_we_server/<int:pk>', IndustriesWeServeViewSet.as_view({'get': 'retrieve'}), name='companies_we_served_all_details'),
#     # path('register/', UserRegistrationView.as_view(), name='register'),
#     path('login/', UserLoginView.as_view(), name='login'),
#     path('profile/', UserProfileView.as_view(), name='profile'),
#     path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
#     # path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
#     path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
#     # path('api/custom-token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
#     # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     # path('api/admin/create/', AdminCreateAPIView.as_view(), name='admin-create'),
#     # path('api/admin/change-password/', AdminChangePasswordAPIView.as_view(), name='admin-change-password'),
#     # path('send-email/', send_email, name='send_email'),



# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

