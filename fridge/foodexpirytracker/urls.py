from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path as url
from django.contrib.auth import views as auth_views
from app1 import views as accounts_views
from app1 import views
from app1.views import list_item, meals, recipes, search, item_update, item_delete, profile, item_update_quantity
from app1 import views as app1_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_item, name='item_list'),
    path('edit/<int:pk>', item_update, name='item_update'),
    path('delete/<int:pk>', item_delete, name='item_delete'),
    path("update-quantity/<int:pk>/", item_update_quantity),
    path('search/', search, name='search'),
    # path('chart_test/',views.Chart, name = 'chart_test'),
    path('about/',views.about, name = 'about'),
    path('chart/',views.chart, name = 'chart'),
    path('chart_test1/',views.chart1, name = 'chart_test1'),
    # path('chart_test1/',views.Chart1, name = 'chart_test1'),


    # path('api', views.ChartData, name = 'chart_test'),
    path('recipes/', recipes, name = 'recipes'),
    path('meals/', meals, name = 'meals'),

    # account
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # for reset password
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    # for change by old password
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    # url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    path('profile/', profile, name='profile_update')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
