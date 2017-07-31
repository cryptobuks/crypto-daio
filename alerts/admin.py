from django.contrib import admin

from alerts.models import (
    BalanceAlert,
    Connector
)


class ConnectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'base_url', 'api_user_name')
    search_fields = ('name', 'provider', 'base_url', 'api_user_name')

admin.site.register(Connector, ConnectorAdmin)


class BalanceAlertAdmin(admin.ModelAdmin):
    list_display = ('exchange', 'currency', 'alert_operator', 'alert_value')

admin.site.register(BalanceAlert, BalanceAlertAdmin)
