import alt
import veh_utils

def playerConnect(player):
    player.model = "mp_m_freemode_01"

    player.spawn(0, 2, 4, 0)
    veh = alt.Vehicle("krieger", 5, 5, 76, 0, 0, 0)
    veh.setMeta("name", "krieger")
    alt.log("Created vehicle")
    alt.log("Vehicle ID: {}".format(veh.id))

    alt.log("{}".format(player.entityAimingOffset))

    player.setClothes(2, 21, 4, 0)
    player.setClothes(8, 15, 0, 0)
    player.setClothes(11, 9, 0, 0)
    player.setClothes(4, 12, 0, 0)
    

    alt.log("Hair clothes: {}".format(player.getClothes(2)))
    player.giveWeapon("weapon_rpg", 999, True)

def playerEnterVehicle(player, vehicle, seat):
    alt.log("Player {0} entered vehicle {1}".format(player.name, vehicle.id))
    vehicle.customPrimaryColor = alt.RGBA(243, 255, 0, 255)
    veh_utils.maxVehicle(vehicle)
    vehicle.numberPlateText = player.name
    alt.log("Vehicle driver: {}".format(vehicle.driver.name))

def playerLeaveVehicle(player, vehicle, seat):
    alt.log("Player {0} left vehicle {1}".format(player.name, vehicle.id))
    vehicle.customPrimaryColor = alt.RGBA(0, 0, 0, 255)
    vehicle.numberPlateText = vehicle.getMeta("name")

alt.on("playerConnect", playerConnect)
alt.on("playerEnterVehicle", playerEnterVehicle)
alt.on("playerLeaveVehicle", playerLeaveVehicle)