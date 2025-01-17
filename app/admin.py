from django.contrib import admin
from .models import Fleet, UberFleet, BoltFleet, UklonFleet
from .models import Driver, Vehicle, Fleets_drivers_vehicles_rate, User
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter


class FleetChildAdmin(PolymorphicChildModelAdmin):
    base_model = Fleet 
    show_in_index = False
@admin.register(UberFleet)
class UberFleetAdmin(FleetChildAdmin):
    base_model = UberFleet
    show_in_index = False
@admin.register(BoltFleet)
class BoltFleetAdmin(FleetChildAdmin):
    base_model = BoltFleet
    show_in_index = False
@admin.register(UklonFleet)
class UklonFleetAdmin(FleetChildAdmin):
    base_model = UklonFleet
    show_in_index = False

@admin.register(Fleet)
class FleetParentAdmin(PolymorphicParentModelAdmin):
    base_model = Fleet 
    child_models = (UberFleet, BoltFleet, UklonFleet,)
    list_filter = (PolymorphicChildModelFilter,)
    

admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Fleets_drivers_vehicles_rate)
