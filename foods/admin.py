from django.contrib import admin
from.models import MenuItem,Category,OrderItems,OrderStatus
# Register your models here.


admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(OrderStatus)
admin.site.register(OrderItems)
