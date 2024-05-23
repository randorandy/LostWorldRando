from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places. 
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    Varia, GravitySuit, Wave, SpeedBooster, Spazer, Ice,
    Plasma, Screw, Charge, Grapple, SpaceJump, Energy, Reserve, Xray
) = items_unpackable

energy200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 1
))

energy300 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 6
))
energy800 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 7
))
energy900 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 14
))
hellrun1 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy200 in loadout)
))
hellrun3 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy400 in loadout)
))
hellrun4 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy500 in loadout)
))
hellrun5 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))
hellrun7 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))


missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 4 >= 10
))
missile20 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 4 >= 20
))

super4 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 4
))
super6 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 6
))
super12 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 12
))
super30 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 30
))
powerBomb4 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 2
))
powerBomb6 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 3
))
powerBomb8 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 4
))
powerBomb10 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 5
))
powerBomb12 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 6
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (PowerBomb in loadout)
))
canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (canUseBombs in loadout) or
    (Screw in loadout)
))
pinkDoor = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (
        (Missile in loadout) or
        (Super in loadout)
        )
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canSBJ = LogicShortcut(lambda loadout: (
    (Springball in loadout) and
    (Morph in loadout)
))
canHighSBJ = LogicShortcut(lambda loadout: (
    (Springball in loadout) and
    (Morph in loadout) and
    (HiJump in loadout)
))
canFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout)
))
canSpeedOrFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout) or
    (SpeedBooster in loadout)
))
canCF = LogicShortcut(lambda loadout: (
    (missile10 in loadout) and
    (super12 in loadout) and
    (powerBomb12 in loadout)
))
canHop = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) or
    (
        (Morph in loadout) and
        (Springball in loadout)
    )
))

rockyFall = LogicShortcut(lambda loadout: (
    True

))
rockyFall2 = LogicShortcut(lambda loadout: (
    #central hilly return doesn't need HJB or gravity
    # ^ I don't think this is true
    #(
    #    (canUsePB in loadout) and
    #    (Grapple in loadout) and
    #    (canSpeedOrFly in loadout)
    #) or
    #go back up the normal way toward the ship
    (
        (HiJump in loadout) or
        (GravitySuit in loadout)
    ) and
    (
        (canUseBombs in loadout) or
        (
            (GravitySuit in loadout) and
            (canBreakBlocks in loadout)
        )
    )
))
warpZone = LogicShortcut(lambda loadout: (
    (rockyFall2 in loadout) and
    (pinkDoor in loadout)
))

btDoor = LogicShortcut(lambda loadout: (
    (
        (Bombs in loadout) and
        (rockyFall2 in loadout) and
        (Morph in loadout) and
        (canHop in loadout) and
        (pinkDoor in loadout)
    ) 
    
))

    # or
    #(
    #    (Grapple in loadout) and
    #    (Morph in loadout) and
    #    (hellrun3 in loadout) and
    #    (warpZone2 in loadout)
    #)

iceHellrun = LogicShortcut(lambda loadout: (
    (btDoor in loadout) and
    (hellrun1 in loadout) and
    (pinkDoor in loadout)
))
swampWestFall = LogicShortcut(lambda loadout: (
    (rockyFall2 in loadout) and
    (Morph in loadout) and
    (
        (GravitySuit in loadout) or
        (HiJump in loadout) or
        (SpeedBooster in loadout) or
        (SpaceJump in loadout)
    )
))
swampSuperWestFall = LogicShortcut(lambda loadout: (
    (swampWestFall in loadout) and
    (Super in loadout) and
    (
        (canIBJ in loadout) or
        (powerBomb4 in loadout)
    ) and
    (
        (powerBomb8 in loadout) or
        (canIBJ in loadout) or
        (Screw in loadout)
    )
))
spore = LogicShortcut(lambda loadout: (
    (rockyFall2 in loadout) and
    (pinkDoor in loadout) and
    # need morph to get any items after spo spo AND get out by falling
    (Morph in loadout) and
    # defeat spore spawn handily
    (
        (Missile in loadout) or
        (Charge in loadout)
    )
))
jungleGym = LogicShortcut(lambda loadout: (
    (
        (spore in loadout) and
        (
            (Grapple in loadout) or
            (SpaceJump in loadout) or
            (SpeedBooster in loadout)
        )
    ) or
    (
        (warpZone in loadout) and
        (
            (SpaceJump in loadout) or
            (SpeedBooster in loadout)
        )
    )
))
kraid = LogicShortcut(lambda loadout: (
    (rockyFall2 in loadout) and
    # too many bomb blocks
    (canIBJ in loadout) and
    # underwater hop
    (
        (GravitySuit in loadout) or
        (Springball in loadout)
    ) and
    # actually kill kraid
    (
        (Missile in loadout) or
        (Charge in loadout)
    )
))
cargo = LogicShortcut(lambda loadout: (
    (iceHellrun in loadout) and
    (hellrun5 in loadout) and 
    (pinkDoor in loadout) 
))
hoppergate = LogicShortcut(lambda loadout: (
    (cargo in loadout) and
    (Charge in loadout) and
    (Wave in loadout) and
    (
        (Morph in loadout) or
        (SpaceJump in loadout)
    )
))
antfarm = LogicShortcut(lambda loadout: (
    (cargo in loadout) and
    (Morph in loadout) and
    (
        
        (
            (Super in loadout) and
            (Varia in loadout)
        ) or
        (SpeedBooster in loadout)
    ) and
    (
        (canUsePB in loadout) or
        (Plasma in loadout)
    )
))
warpZone2 = LogicShortcut(lambda loadout: (
    (
        (
            #ability to cross the warp zone
            (Plasma in loadout) or
            (
                (canBreakBlocks in loadout) and
                (SpeedBooster in loadout) and
                (Morph in loadout) # cheesy magic
            )
        ) and
        (
            (rockyFall2 in loadout) or
            (
                (antfarm in loadout) and
                (Super in loadout) and
                (Varia in loadout)
            )
        )
    ) or
    (
        (swampSuperWestFall in loadout) and
        (SpeedBooster in loadout)
    )
))
southeastAtrium = LogicShortcut(lambda loadout: (
    (warpZone2 in loadout) and
    (Varia in loadout)
))
crocAtrium = LogicShortcut(lambda loadout: (
    (southeastAtrium in loadout) and
    (canBreakBlocks in loadout) and
    (pinkDoor in loadout) and
    (
        (Grapple in loadout) or
        (SpaceJump in loadout) or
        (HiJump in loadout)
    )
))
ridley = LogicShortcut(lambda loadout: (
    (crocAtrium in loadout) and
    (Super in loadout) and
    (canUsePB in loadout) and
    (
        (Grapple in loadout) or
        (canFly in loadout)
    ) and
    (energy700 in loadout) and
    (GravitySuit in loadout) and
    (Charge in loadout) and
    (Plasma in loadout)
))

crossroads = LogicShortcut(lambda loadout: (
    (
        (antfarm in loadout) and
        (Super in loadout) and
        (Varia in loadout)
    ) or
    (
        (southeastAtrium in loadout) and
        (
            (canFly in loadout) or
            (Grapple in loadout)
        )
    )
))
crossroadsWest = LogicShortcut(lambda loadout: (
    (
        (crossroads in loadout) and
        (canUsePB in loadout)
    ) or
    (
        (antfarm in loadout) and
        (canHop in loadout) and
        (canBreakBlocks in loadout) and
        (Varia in loadout)
    )
))

forestNorthwest = LogicShortcut(lambda loadout: (
    (
        (iceHellrun in loadout) and
        (canUsePB in loadout)
    ) or
    (  
        (warpZone2 in loadout) and
        (canUsePB in loadout)
    ) or
    (
        (jungleGym in loadout) and
        (kraid in loadout) and
        (SpeedBooster in loadout) and
        (Super in loadout) 
    )
    # not from mini-kraid
))
etecoons = LogicShortcut(lambda loadout: (
    (
        (iceHellrun in loadout) and
        (canUsePB in loadout)
    ) or
    (  
        (warpZone2 in loadout) and
        (canUsePB in loadout)
    ) or
    (jungleGym in loadout)
    # not from mini-kraid
))
rockyHurdles = LogicShortcut(lambda loadout: (
    (
        (rockyFall2 in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout)
    ) or
    (
        (btDoor in loadout) and
        (super6 in loadout) and
        (Wave in loadout) and
        (pinkDoor in loadout) and
        (Charge in loadout) and
        (
            (Grapple in loadout) or
            (SpeedBooster in loadout)
        )
    )
))
r3gate = LogicShortcut(lambda loadout: (
    (
        (rockyFall2 in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout) and
        (SpaceJump in loadout) and
        (Grapple in loadout) and
        (super6 in loadout)
    ) or
    (
        (btDoor in loadout) and
        (Super in loadout) and
        (Wave in loadout) and
        (pinkDoor in loadout) and
        (Charge in loadout)
    )
))
waveRoom = LogicShortcut(lambda loadout: (
    (
        (rockyFall2 in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout) and
        (SpaceJump in loadout) and
        (Grapple in loadout) and
        (super6 in loadout) and
        (btDoor in loadout)
    ) or
    (
        (btDoor in loadout) and
        (Super in loadout) and
        (Wave in loadout) and
        (pinkDoor in loadout)
    )
))
variaRoom = LogicShortcut(lambda loadout: (
    (
        (warpZone2 in loadout) and
        (canUsePB in loadout) and
        (
            (SpeedBooster in loadout) or
            (Grapple in loadout)
        )
    ) or
    (
        (swampSuperWestFall in loadout) and
        (SpeedBooster in loadout) and
        (Morph in loadout)
    )

))
swampSoutheast = LogicShortcut(lambda loadout: (
    (
        (warpZone2 in loadout) and
        (canUsePB in loadout)
    ) or
    (
        (swampSuperWestFall in loadout) and
        (SpeedBooster in loadout) and
        (Morph in loadout)
    )
))
spazerGate = LogicShortcut(lambda loadout: (
    (variaRoom in loadout) and
    (Wave in loadout)
))
draygonArea = LogicShortcut(lambda loadout: (
    (spazerGate in loadout) and
    (canUsePB in loadout)
))
draygonDead = LogicShortcut(lambda loadout: (
    (draygonArea in loadout) and
    (GravitySuit in loadout) and
    (
        (Charge in loadout) or
        (super30 in loadout)
    )
))


allItems = LogicShortcut(lambda loadout: (
    (Missile in loadout) and
    (super12 in loadout) and
    (PowerBomb in loadout) and
    (Morph in loadout) and
    (Springball in loadout) and
    (Grapple in loadout) and
    (Bombs in loadout) and
    (HiJump in loadout) and
    (GravitySuit in loadout) and
    (Varia in loadout) and
    (Wave in loadout) and
    (SpeedBooster in loadout) and
    (Spazer in loadout) and
    (Ice in loadout) and
    (Plasma in loadout) and
    (Screw in loadout) and
    (Charge in loadout) and
    (SpaceJump in loadout)
))


area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}


location_logic: LocationLogicType = {
    "Charge Beam": lambda loadout: (
        True
    ),
    "Crater Island Missile": lambda loadout: (
        (Morph in loadout) and
        (canSpeedOrFly in loadout)
    ),
    "Crater Speedlocked Missile": lambda loadout: (
        (Morph in loadout) and
        (SpeedBooster in loadout)
    ),
    "Crater Island Power Bomb": lambda loadout: (
        (canSpeedOrFly in loadout) and
        (canUsePB in loadout)
    ),
    "Crater Ship Power Bomb": lambda loadout: (
        (canUsePB in loadout)
    ),
    "West Parlor Crevice Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Parlor Sky Cage Missile": lambda loadout: (
        (SpeedBooster in loadout) and
        (Morph in loadout)
    ),
    "Parlor Floor Missile": lambda loadout: (
        (SpeedBooster in loadout) and
        (Morph in loadout)
    ),
    "Parlor Shelf Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Parlor Grapplelocked Missile": lambda loadout: (
        (Grapple in loadout) and
        (Morph in loadout)
    ),
    "Crater Jail Super Missile": lambda loadout: (
        (canHop in loadout) and
        (Super in loadout)
    ),
    "Parlor Speedlocked Super Missile": lambda loadout: (
        (Morph in loadout) and
        (Super in loadout) and
        (SpeedBooster in loadout)
    ),
    "Parlor Sky Chozo Missile": lambda loadout: (
        (canSpeedOrFly in loadout) or
        (HiJump in loadout)
    ),
    "Parlor Power Bomb": lambda loadout: (
        (canUsePB in loadout)
    ),
    "Charge Left Super Missile": lambda loadout: (
        (Super in loadout) and
        (canUseBombs in loadout)
    ),
    "Charge Right Super Missile": lambda loadout: (
        (Super in loadout) and
        (Morph in loadout)
    ),
    "First Dip Left Missile": lambda loadout: (
        (rockyFall in loadout) and
        (canUseBombs in loadout)
    ),
    "First Dip Right Missile": lambda loadout: (
        (rockyFall in loadout) and
        (Morph in loadout) and
        (
            (HiJump in loadout) or
            (Ice in loadout) or
            (canFly in loadout)
        )
    ),
    "First Dip Center Missile": lambda loadout: (
        (rockyFall in loadout) and
        (canHop in loadout) and
        (
            (GravitySuit in loadout) or
            (canHighSBJ in loadout) or
            (Ice in loadout) or
            (canFly in loadout)
        )
    ),
    "First Dip Power Bomb": lambda loadout: (
        (rockyFall in loadout) and
        (canUsePB in loadout) and
        (
            (GravitySuit in loadout) or
            (Ice in loadout) or
            (canFly in loadout)
        )
    ),
    "Rocky Lower Energy Tank": lambda loadout: (
        (rockyFall2 in loadout) and
        (
            (canIBJ in loadout) or
            (powerBomb4 in loadout)
        ) and
        (
            (HiJump in loadout) or
            (GravitySuit in loadout)
        )
    ),
    "Rocky Lower Energy Missile": lambda loadout: (
        (rockyFall2 in loadout) and
        (canUseBombs in loadout) and
        (
            (HiJump in loadout) or
            (GravitySuit in loadout)
        )
        #copy of Rocky Lower Energy Tank
        #how about morphless though?
    ),
    "Rocky Lower Reserve Tank": lambda loadout: (
        (rockyFall2 in loadout) and
        (GravitySuit in loadout) and
        (Morph in loadout) and
        (SpeedBooster in loadout)
    ),
    "Rocky Lower Reserve Missile": lambda loadout: (
        (rockyFall2 in loadout) and
        (
            (GravitySuit in loadout) or
            (canHighSBJ in loadout)
        )
    ),
    "Bombs": lambda loadout: (
        (rockyFall2 in loadout) and
        (canHop in loadout) and
        (pinkDoor in loadout)
    ),
    "Warp Zone 1 Energy Tank": lambda loadout: (
        (warpZone in loadout)
    ),
    "Warp Zone 1 Power Bomb": lambda loadout: (
        (warpZone in loadout) and
        (canUsePB in loadout)
    ),
    "Warp Zone 1 Super Missile": lambda loadout: (
        (warpZone in loadout) and
        (Super in loadout) and
        (Wave in loadout)
    ),
    "Swamp Entrance Gate Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (Wave in loadout)
    ),
    "Swamp First Plunge Super Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (Super in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Swamp F Room Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (
            (Grapple in loadout) or
            (SpaceJump in loadout)
        ) and
        (canBreakBlocks in loadout)
    ),
    "Swamp Top Sand Right Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (canUseBombs in loadout) and
        (
            (powerBomb4 in loadout) or
            (canIBJ in loadout) or
            (Screw in loadout)
        )
    ),
    "Swamp Top Sand Left Missile": lambda loadout: (
        (swampWestFall in loadout)
    ),
    "Swamp Crumblemania Left Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Swamp Crumblemania Upper Super Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (Super in loadout) and
        (Springball in loadout)
    ),
    "Swamp Crumblemania Lower Super Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (Super in loadout) and
        (Springball in loadout)
    ),
    "Swamp Crumblemania Right Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (canIBJ in loadout)
    ),
    "HiJump Super Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (canUseBombs in loadout) and
        (Super in loadout) and
        (energy500 in loadout)
    ),
    "HiJump": lambda loadout: (
        (swampWestFall in loadout)
    ),
    "HiJump Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (canBreakBlocks in loadout)
    ),
    "Swamp Below H4 Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (Plasma in loadout) and
        (Super in loadout)
    ),
    "Swamp Namihe Climb Bottom Super Missile": lambda loadout: (
        (swampSuperWestFall in loadout) and
        (
            (canIBJ in loadout) or
            (Screw in loadout)
        )
    ),
    "Swamp Namihe Climb Top Super Missile": lambda loadout: (
        (swampSuperWestFall in loadout) and
        (
            (canIBJ in loadout) or
            (Screw in loadout)
        )
    ),
    "Swamp Namihe Climb East Super Missile": lambda loadout: (
        (swampSuperWestFall in loadout) and
        (Super in loadout) and
        (SpeedBooster in loadout)
    ),
    "Swamp Reserve Tank": lambda loadout: (
        (swampSuperWestFall in loadout) and
        (Grapple in loadout)
    ),
    "Swamp Reserve Left Missile": lambda loadout: (
        (swampSuperWestFall in loadout) and
        (canUsePB in loadout)
    ),
    "Swamp Reserve Super Missile": lambda loadout: (
        (swampSuperWestFall in loadout)
    ),
    "Swamp Reserve Right Missile": lambda loadout: (
        (swampSuperWestFall in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Swamp H2 Left Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (
            (SpaceJump in loadout) or
            (Grapple in loadout)
        ) and
        (
            (SpaceJump in loadout) or
            (SpeedBooster in loadout) or
            (canHighSBJ in loadout) or
            (canIBJ in loadout)
        )
    ),
    "Swamp H2 Above Island Missile": lambda loadout: (
        (swampSuperWestFall in loadout) and
        (SpaceJump in loadout)
    ),
    "Swamp H2 Below Island Missile": lambda loadout: (
        (swampSuperWestFall in loadout) and
        (SpaceJump in loadout)
    ),
    "Swamp Bottom Bridge Energy Tank": lambda loadout: (
        (swampSuperWestFall in loadout)
    ),
    "Evir Climb Missile": lambda loadout: (
        (swampSuperWestFall in loadout) and
        (Grapple in loadout)
    ),
    "Evir Climb Super Missile": lambda loadout: (
        (swampSuperWestFall in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Swamp H3 Shaft Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (Wave in loadout) and
        (Plasma in loadout)
    ),
    "Swamp H3 Shaft Super Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (Wave in loadout) and
        (Plasma in loadout)
    ),
    "Swamp H3 Power Bomb": lambda loadout: (
        (swampWestFall in loadout) and
        (Wave in loadout) and
        (Plasma in loadout) and
        (GravitySuit in loadout) and
        (SpaceJump in loadout)
    ),
    "Swamp H3 Exit Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (Wave in loadout) and
        (canUseBombs in loadout)
    ),
    "Swamp H3 Exit Power Bomb": lambda loadout: (
        (swampWestFall in loadout) and
        (Wave in loadout) and
        (canUseBombs in loadout)
    ),
    "Forest Meadow Underground Power Bomb": lambda loadout: (
        (warpZone in loadout) and
        (canUsePB in loadout)
    ),
    "Forest Meadow Underground Missile": lambda loadout: (
        (warpZone in loadout) and
        (canUsePB in loadout) and
        (
            (powerBomb4 in loadout) or
            (canIBJ in loadout) or
            (Springball in loadout)
        )
    ),
    "Forest Meadow Shed Missile": lambda loadout: (
        (warpZone in loadout)
    ),

    "Forest Entry Tease Super Missile": lambda loadout: (
        (warpZone in loadout) and
        (Super in loadout) and
        (Morph in loadout) and
        (canBreakBlocks in loadout)
    ),
    "Alpha Missile": lambda loadout: (
        (warpZone in loadout)
    ),
    "Morph Ball": lambda loadout: (
        (spore in loadout)
    ),
    "Outside Morph Missile": lambda loadout: (
        (spore in loadout)
    ),
    "Morph Hidden Missile": lambda loadout: (
        (spore in loadout) and
        (Grapple in loadout)
    ),
    "Morph Behind Missile": lambda loadout: (
        (spore in loadout) and
        (Grapple in loadout)
    ),
    "Jungle Gym Island Missile": lambda loadout: (
        (jungleGym in loadout) and
        (Morph in loadout)
    ),
    "Jungle Gym Underground Missile": lambda loadout: (
        (jungleGym in loadout) and
        (canUseBombs in loadout)
    ),
    "Forest D4 Missile": lambda loadout: (
        (warpZone in loadout) and
        (Morph in loadout)
    ),
    "Forest D4 Super Missile": lambda loadout: (
        (warpZone in loadout) and
        (Morph in loadout) and
        (Super in loadout)
    ),
    "Gravity Cubby Missile": lambda loadout: (
        (warpZone in loadout) and
        (Morph in loadout)
    ),
    "Gravity West Power Bomb": lambda loadout: (
        (warpZone in loadout) and
        (Morph in loadout) and
        (canUsePB in loadout)
    ),
    "Gravity Ceiling Missile": lambda loadout: (
        (warpZone in loadout) and
        (canUseBombs in loadout) and
        (SpeedBooster in loadout)
    ),
    "Gravity Power Bomb": lambda loadout: (
        (warpZone in loadout) and
        (canUseBombs in loadout) and
        (SpeedBooster in loadout)
    ),
    "Gravity Wall Missile": lambda loadout: (
        (warpZone in loadout) and
        (Morph in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Gravity Sky Chozo Missile": lambda loadout: (
        (warpZone in loadout) and
        (Morph in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Gravity Super Missile": lambda loadout: (
        (warpZone in loadout) and
        (Morph in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (Super in loadout)
    ),
    "Gravity Suit": lambda loadout: (
        (warpZone in loadout) and
        (Morph in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Forest Entry Tease Missile": lambda loadout: (
        (kraid in loadout) and
        (canUsePB in loadout)
    ),
    "Gravity East Tunnel Single Missile": lambda loadout: (
        (warpZone in loadout) and
        (canUseBombs in loadout) and
        (Grapple in loadout) and
        (canIBJ in loadout)
    ),
    "Gravity East Tunnel 2 Low Missile": lambda loadout: (
        (kraid in loadout)
    ),
    "Gravity East Tunnel 2 Top Missile": lambda loadout: (
        (kraid in loadout)
    ),
    "Grapple Beam": lambda loadout: (
        (kraid in loadout)
    ),
    "Forest Reserve Tank": lambda loadout: (
        (kraid in loadout) and
        (Super in loadout) and
        (SpaceJump in loadout)
    ),
    "Forest Reserve Energy Tank": lambda loadout: (
        (kraid in loadout) and
        (Super in loadout) and
        (canFly in loadout) and
        (canUsePB in loadout)
    ),
    "Forest D3 Right Super Missile": lambda loadout: (
        (kraid in loadout) and
        (Super in loadout) and
        (SpaceJump in loadout)
    ),
    "Forest D3 Left Super Missile": lambda loadout: (
        (kraid in loadout) and
        (Super in loadout) and
        (SpaceJump in loadout)
    ),
    "Forest Northwest Top Missile": lambda loadout: (
        (forestNorthwest in loadout)
    ),
    "Forest Northwest Gate Missile": lambda loadout: (
        (forestNorthwest in loadout)
    ),
    "Forest Northwest Floor Missile": lambda loadout: (
        (forestNorthwest in loadout) and
        (Grapple in loadout)
    ),
    "Forest Northwest Super Missile": lambda loadout: (
        (forestNorthwest in loadout) and
        (Super in loadout)
    ),
    "Forest Northwest Energy Tank": lambda loadout: (
        (forestNorthwest in loadout)
    ),
    "West of Springball Missile": lambda loadout: (
        (forestNorthwest in loadout)
    ),
    "Springball": lambda loadout: (
        (forestNorthwest in loadout) and
        (canUsePB in loadout)
    ),
     "Springball Super Missile": lambda loadout: (
        (forestNorthwest in loadout) and
        (Super in loadout) and
        (
            (canUseBombs in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "Springball Missile": lambda loadout: (
        (forestNorthwest in loadout) and
        (pinkDoor in loadout) and
        (
            (canUseBombs in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "East of Springball Missile": lambda loadout: (
        (forestNorthwest in loadout) and
        (
            (SpeedBooster in loadout) or
            (canUseBombs in loadout)
        )
    ),
    "Baby Kraid Missile": lambda loadout: (
        (forestNorthwest in loadout) and
        (SpeedBooster in loadout)
    ),
    "Baby Kraid Energy Tank": lambda loadout: (
        (forestNorthwest in loadout) and
        (canBreakBlocks in loadout) and
        (canSpeedOrFly in loadout)
    ),
    "Below Springball Missile": lambda loadout: (
        (etecoons in loadout) and
        (canUsePB in loadout)
    ),
    "Below Springball Super Missile": lambda loadout: (
        (etecoons in loadout) and
        (canUsePB in loadout) and
        (Super in loadout)
    ),
    "Etecoons High Hut Missile": lambda loadout: (
        (etecoons in loadout) and
        (SpeedBooster in loadout)
    ),
    "Etecoons High Tunnel Super Missile": lambda loadout: (
        (etecoons in loadout) and
        (Super in loadout) and
        (Morph in loadout)
    ),
    "Etecoons Mid Grapple Tunnel Missile": lambda loadout: (
        (etecoons in loadout) and
        (Grapple in loadout) and
        (canHop in loadout)
    ),
    "Etecoons Low Northwest Missile": lambda loadout: (
        (etecoons in loadout) and
        (Grapple in loadout) and
        (Morph in loadout)
    ),
    "Etecoons Low Southwest Missile": lambda loadout: (
        (etecoons in loadout)
    ),
    "Etecoons Low Southeast Missile": lambda loadout: (
        (etecoons in loadout) and
        (Morph in loadout)
    ),
    "Etecoons Low Right Super Missile": lambda loadout: (
        (etecoons in loadout) and
        (Super in loadout) and
        (Morph in loadout)
    ),
    "Etecoons Speedlocked Missile": lambda loadout: (
        (etecoons in loadout) and
        (SpeedBooster in loadout)
    ),
    "Etecoons Mid Left Super Missile": lambda loadout: (
        (etecoons in loadout) and
        (Super in loadout)
    ),
    "Etecoons Low Left Super Missile": lambda loadout: (
        (etecoons in loadout) and
        (Super in loadout) and
        (Morph in loadout)
    ),
    "Forest D2 Missile": lambda loadout: (
        (etecoons in loadout) and
        (SpeedBooster in loadout) and
        (canHop in loadout)
    ),
    "Plasma Beam": lambda loadout: (
        (warpZone in loadout) and
        (Morph in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (Super in loadout) and
        (Wave in loadout) and
        (canFly in loadout) and
        (canBreakBlocks in loadout) and
        (Plasma in loadout)
        #based on gravity super
    ),
    "Plasma Super Missile": lambda loadout: (
        (warpZone in loadout) and
        (Morph in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (Super in loadout) and
        (Wave in loadout) and
        (canFly in loadout) and
        (canBreakBlocks in loadout) and
        (Plasma in loadout)
        #matches plasma beam
    ),
    "Rocky Warp Cavern Left Missile": lambda loadout: (
        (rockyFall2 in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (canUseBombs in loadout)
    ),
    "Rocky Warp Cavern Right Missile": lambda loadout: (
        (rockyFall2 in loadout) and
        (
            (
                (GravitySuit in loadout) and
                (
                    (HiJump in loadout) or
                    (canSpeedOrFly in loadout)
                )
            ) or
            (Grapple in loadout)
        )
    ),
    "Rocky Hurdles Speedlocked Missile": lambda loadout: (
        (rockyHurdles in loadout) and
        (SpeedBooster in loadout) and
        (
            (SpaceJump in loadout) or
            (
                (Super in loadout) and
                (Charge in loadout) and
                (Wave in loadout)
            )
        )
    ),
    "Rocky Hurdles Missile": lambda loadout: (
        (rockyHurdles in loadout)
    ),
    "Rocky Gate R3 Power Bomb": lambda loadout: (
        (r3gate in loadout) and
        (canUseBombs in loadout)
    ),
    "Rocky Gate R3 Missile": lambda loadout: (
        (r3gate in loadout) and
        (canFly in loadout) and
        (canBreakBlocks in loadout)
    ),
    "Rocky Ninjas Power Bomb": lambda loadout: (
        (r3gate in loadout) and
        (Super in loadout) and
        (Grapple in loadout)
    ),
    "Rocky Ninjas Missile": lambda loadout: (
        (r3gate in loadout) and
        (canFly in loadout)
    ),
    "Wave Wall Lower Missile": lambda loadout: (
        (waveRoom in loadout)
    ),
    "Wave Beam": lambda loadout: (
        (waveRoom in loadout)
    ),
    "Wave Wall Upper Missile": lambda loadout: (
        (waveRoom in loadout)
    ),
    "Wave Gem Missile": lambda loadout: (
        (waveRoom in loadout) and
        (Plasma in loadout) and
        (Super in loadout)
    ),
    "Rocky Upper Reserve Power Bomb": lambda loadout: (
        (btDoor in loadout) and
        (Grapple in loadout)
    ),
    "Rocky Upper Reserve Tank": lambda loadout: (
        (btDoor in loadout)
    ),
    "Mountain Entry Speedlocked Missile": lambda loadout: (
        (btDoor in loadout) and
        (iceHellrun in loadout) and
        (SpeedBooster in loadout)
    ),
    "Mountain Entry Left Missile": lambda loadout: (
        (btDoor in loadout) and
        (iceHellrun in loadout) and
        (canUsePB in loadout)
    ),
    "Mountain Slalom Right Missile": lambda loadout: (
        (btDoor in loadout) and
        (iceHellrun in loadout) and
        (SpeedBooster in loadout)
        # or from below?
    ),
    "Mountain Slalom Left Missile": lambda loadout: (
        (btDoor in loadout) and
        (iceHellrun in loadout) and
        (SpeedBooster in loadout) and
        (hellrun4 in loadout)
        # or from below?
    ),
    "Mountain West Warp Missile": lambda loadout: (
        (btDoor in loadout) and
        (iceHellrun in loadout) and
        (Grapple in loadout) and
        (hellrun4 in loadout)
    ),
    "Mountain West Warp Power Bomb": lambda loadout: (
        (btDoor in loadout) and
        (iceHellrun in loadout) and
        (
            (Plasma in loadout) or
            (canUsePB in loadout)
        ) and
        (hellrun4 in loadout)
    ),
    "Warp Zone 2 Missile": lambda loadout: (
        (warpZone2 in loadout)
    ),
    "Spore Spawn Missile": lambda loadout: (
        (spore in loadout)
    ),
    "Outside Morph Super Missile": lambda loadout: (
        (spore in loadout) and
        (Super in loadout)
    ),
    "Xray": lambda loadout: (
        (
            (energy200 in loadout) or
            (Grapple in loadout)
        ) and
        (
            (
                (forestNorthwest in loadout) and
                (SpeedBooster in loadout)
            ) or
            (
                (etecoons in loadout) and
                (canUsePB in loadout)
            )
        )
    ),
    "Mountain Southeast Energy Tank": lambda loadout: (
        (warpZone2 in loadout) and
        (hellrun3 in loadout) and
        (Morph in loadout) and
        (
            (canUseBombs in loadout) or
            (Screw in loadout) or
            (pinkDoor in loadout) or
            (energy600 in loadout)
        )
    ),
    "Mountain Entry Under Bridge Missile": lambda loadout: (
        (iceHellrun in loadout) and
        (hellrun5 in loadout) and
        (Grapple in loadout)
    ),
    "Mountain Entry Hoppers Super Missile": lambda loadout: (
        (iceHellrun in loadout) and
        (hellrun7 in loadout) and
        (energy400 in loadout) and
        (super12 in loadout)
    ),
    "Mountain Inner Door Speedlocked Missile": lambda loadout: (
        (iceHellrun in loadout) and
        (hellrun5 in loadout) and
        (SpeedBooster in loadout)
    ),
    "Mountain Pirate Cargo Low Super Missile": lambda loadout: (
        (cargo in loadout) and
        (Morph in loadout) and
        (Super in loadout) 
    ),
    "Mountain Pirate Cargo Power Bomb": lambda loadout: (
        (cargo in loadout) and
        (Morph in loadout) and
        (Super in loadout)
    ),
    "Mountain Pirate Cargo Low Missile": lambda loadout: (
        (cargo in loadout) and
        (Morph in loadout) and
        (Super in loadout)
    ),
    "Mountain Pirate Cargo High Missile": lambda loadout: (
        (cargo in loadout) and
        (canUseBombs in loadout)
    ),
    "Mountain Pirate Cargo High Super Missile": lambda loadout: (
        (cargo in loadout) and
        (Super in loadout) and
        (canFly in loadout)
    ),
    "Pre-Alpha Power Bomb": lambda loadout: (
        (cargo in loadout) and
        (
            (warpZone2 in loadout) or
            (SpeedBooster in loadout)
        ) and
        (canUsePB in loadout)
    ),
    "Alpha Power Bomb": lambda loadout: (
        (cargo in loadout) and
        (
            (warpZone2 in loadout) or
            (SpeedBooster in loadout)
        ) and
        (
            (canUsePB in loadout) or
            (Plasma in loadout)
        )
    ),
    "Ant Farm Entry Super Missile": lambda loadout: (
        (antfarm in loadout) and
        (canFly in loadout) and
        (Super in loadout)
    ),
    "Ant Farm Entry Right Missile": lambda loadout: (
        (antfarm in loadout) and
        (
            (canSpeedOrFly in loadout) or
            (HiJump in loadout) or
            (Ice in loadout)
        )   
    ),
    "Ant Farm Entry Ceiling Missile": lambda loadout: (
        (antfarm in loadout)
    ),
    "Ant Farm Entry Left Missile": lambda loadout: (
        (antfarm in loadout) and
        (
            (canSpeedOrFly in loadout) or
            (HiJump in loadout)
        )   
    ),
    "Ant Farm Right Power Bomb": lambda loadout: (
        (antfarm in loadout)
    ),
    "Ant Farm Underwater Missile": lambda loadout: (
        (antfarm in loadout) and
        (
            (Springball in loadout) or
            (
                (GravitySuit in loadout) and
                (canHop in loadout)
            )
        )
    ),
    "Ant Farm Left Power Bomb": lambda loadout: (
        (antfarm in loadout)
    ),
    "Ant Farm Super Missile": lambda loadout: (
        (antfarm in loadout) and
        (Super in loadout)
    ),
    "Ant Farm Underwater Power Bomb": lambda loadout: (
        (antfarm in loadout)
    ),
    "Ant Farm Top Right Missile": lambda loadout: (
        (antfarm in loadout) and
        (SpeedBooster in loadout)
    ),
    "Ant Farm Top Left Missile": lambda loadout: (
        (antfarm in loadout) and
        (SpeedBooster in loadout)
    ),
    "Mountain Crossroads West Missile": lambda loadout: (
        (crossroadsWest in loadout) and
        (Grapple in loadout)
    ),
    "Early Super Missile": lambda loadout: (
        (crossroadsWest in loadout) and
        (
            (Super in loadout) or
            (Ice in loadout)
        )
    ),
    "Early Super Gate Missile": lambda loadout: (
        (crossroadsWest in loadout) and
        (pinkDoor in loadout) and
        (canBreakBlocks in loadout) and
        (canHop in loadout)
    ),
    "Mountain Southeast Atrium Missile": lambda loadout: (
        (crossroadsWest in loadout) and
        (SpeedBooster in loadout)
    ),
    "Mountain Southeast Atrium Power Bomb": lambda loadout: (
        (crossroadsWest in loadout) and
        (canUsePB in loadout)
    ),
    "Mountain Crossroads Super Missile": lambda loadout: (
        (crossroads in loadout) and
        (Super in loadout)
    ),
    "Mountain Crossroads Missile": lambda loadout: (
        (crossroads in loadout) and
        (Morph in loadout) and
        (Grapple in loadout)
    ),
    "Mountain Crossroads Hidden Missile": lambda loadout: (
        (crossroads in loadout) and
        (Morph in loadout) and
        (Grapple in loadout)
    ),
    "Mountain F4 Path Super Missile": lambda loadout: (
        (crossroads in loadout) and
        (cargo in loadout) and
        (SpaceJump in loadout) and
        (
            (Screw in loadout) or
            (Bombs in loadout)
        ) and
        (Super in loadout)
    ),
    "Three Musketeers Super Missile": lambda loadout: (
        (crossroadsWest in loadout) and
        (Morph in loadout) and
        (Super in loadout)
    ),
    "Three Musketeers Missile": lambda loadout: (
        (crossroadsWest in loadout) and
        (Morph in loadout) and
        (Grapple in loadout)
    ),
    "Three Musketeers Power Bomb": lambda loadout: (
        (crossroadsWest in loadout) and
        (Morph in loadout)
    ),
    "Three Musketeers Hidden Missile": lambda loadout: (
        (crossroadsWest in loadout) and
        (Morph in loadout) and
        (Grapple in loadout)
    ),
    "Mountain Hopper Gate Hidden Super Missile": lambda loadout: (
        (hoppergate in loadout) and
        (Super in loadout)
    ),
    "Mountain Hopper Gate Super Missile": lambda loadout: (
        (hoppergate in loadout) and
        (Super in loadout)
    ),
    "Mountain F5 Energy Tank": lambda loadout: (
        (hoppergate in loadout) and
        (canBreakBlocks in loadout) and
        (canHop in loadout)
    ),
    "Outside Speed Missile": lambda loadout: (
        (iceHellrun in loadout) and
        (Varia in loadout) and
        (SpeedBooster in loadout) and
        (Morph in loadout)
    ),
    "Speed Booster": lambda loadout: (
        (iceHellrun in loadout) and
        (Varia in loadout) and
        (SpeedBooster in loadout) and
        (Morph in loadout) and
        (Grapple in loadout)
    ),
    "Mountain Ninja Cell Missile": lambda loadout: (
        (
            (iceHellrun in loadout) and
            (Varia in loadout) and
            (SpeedBooster in loadout)
        ) or
        (
            (crossroadsWest in loadout) and
            (canUsePB in loadout) and
            (
                (SpeedBooster in loadout) or
                (
                    (canBreakBlocks in loadout) and
                    (Morph in loadout) and
                    (Ice in loadout)
                )
            )
        )
    ),
    "Mountain Low Grapple Climb Missile": lambda loadout: (
        (crocAtrium in loadout) and
        (
            (Grapple in loadout) or
            (canFly in loadout)
        )
    ),
    "Crocomire Missile": lambda loadout: (
        (crocAtrium in loadout)
    ),
    "Crocomire Super Missile": lambda loadout: (
        (crocAtrium in loadout) and
        (canFly in loadout) and
        (Super in loadout)
    ),
    "Crocomire Energy Tank": lambda loadout: (
        (crocAtrium in loadout) and
        (canFly in loadout) and
        (super12 in loadout)
    ),
    "Mountain Leap of Faith Missile": lambda loadout: (
        (crocAtrium in loadout) and
        (
            (Grapple in loadout) or
            (canFly in loadout)
        )
    ),
    "Ridley Speedway Missile": lambda loadout: (
        (crocAtrium in loadout) and
        (
            (Grapple in loadout) or
            (canFly in loadout)
        ) and
        (
            (SpeedBooster in loadout) or
            (canUsePB in loadout)
        )
    ),
    "Ridley Speedway Super Missile": lambda loadout: (
        (crocAtrium in loadout) and
        (
            (Grapple in loadout) or
            (canFly in loadout)
        ) and
        (SpeedBooster in loadout)
    ),
    "Ridley Energy Tank": lambda loadout: (
        (crocAtrium in loadout) and
        (canUsePB in loadout) and
        (
            (Grapple in loadout) or
            (canFly in loadout)
        )
    ),
    
    "Ice Beam Super Missile": lambda loadout: (
        (crocAtrium in loadout) and
        (Super in loadout) and
        (canUsePB in loadout) and
        (
            (Grapple in loadout) or
            (canFly in loadout)
        )
    ),
    "Ice Beam": lambda loadout: (
        (crocAtrium in loadout) and
        (canUseBombs in loadout) and
        (
            (Ice in loadout) or
            (SpaceJump in loadout)
        )
    ),
    "Ridley Missile": lambda loadout: (
        (crocAtrium in loadout) and
        (Super in loadout) and
        (canUsePB in loadout) and
        (
            (Grapple in loadout) or
            (canFly in loadout)
        )
    ),
    "Acid Bath Energy Tank": lambda loadout: (
        (ridley in loadout)
    ),
    "Mountain F1 Missile": lambda loadout: (
        (cargo in loadout) and
        (canUsePB in loadout)
    ),
    "Mountain Grapple Gym Missile": lambda loadout: (
        (crocAtrium in loadout)
    ),
    "Grapple Super Missile": lambda loadout: (
        (kraid in loadout) and
        (Plasma in loadout) and
        (SpeedBooster in loadout) and
        (Super in loadout)
    ),
    "Forest Double First Super Missile": lambda loadout: (
        (kraid in loadout) and
        (canSpeedOrFly in loadout) and
        (Super in loadout)
    ),
    "Forest Double Second Super Missile": lambda loadout: (
        (kraid in loadout) and
        (canSpeedOrFly in loadout) and
        (Super in loadout)
    ),
    "Forest Triple Left Super Missile": lambda loadout: (
        (kraid in loadout) and
        (SpeedBooster in loadout) and
        (
            (canIBJ in loadout) or
            (Springball in loadout)
        )
    ),
    "Forest Triple Right Super Missile": lambda loadout: (
        (kraid in loadout) and
        (SpeedBooster in loadout) and
        (
            (canIBJ in loadout) or
            (Springball in loadout)
        )
    ),
    "Forest Triple Lower Super Missile": lambda loadout: (
        (kraid in loadout) and
        (SpeedBooster in loadout) and
        (
            (canIBJ in loadout) or
            (Springball in loadout)
        )
    ),
    "Varia Left Missile": lambda loadout: (
        (variaRoom in loadout)
    ),
    "Varia Right Missile": lambda loadout: (
        (variaRoom in loadout)
    ),
    "Varia Center Missile": lambda loadout: (
        (variaRoom in loadout) and
        (
            (Grapple in loadout) or
            (SpaceJump in loadout) or
            (GravitySuit in loadout) or
            (HiJump in loadout)
        )
    ),
    "Spazer Left Missile": lambda loadout: (
        (variaRoom in loadout)
    ),
    "Spazer Right Missile": lambda loadout: (
        (variaRoom in loadout) and
        (canSpeedOrFly in loadout)
    ),
    "Spazer": lambda loadout: (
        (
            (variaRoom in loadout) or
            (warpZone2 in loadout)
        ) and
        (canUseBombs in loadout)
    ),
    "Outside Draygon Super Missile": lambda loadout: (
        (draygonArea in loadout) and
        (Super in loadout)
    ),
    "Outside Draygon Missile": lambda loadout: (
        (draygonArea in loadout)
    ),
    "Screw Attack": lambda loadout: (
        (draygonDead in loadout)
    ),
    "Screw Ninjas Missile": lambda loadout: (
        (draygonArea in loadout)
    ),
    "Swamp Caged Mochtroids Missile": lambda loadout: (
        (draygonArea in loadout)
    ),
    "Shaktool Missile?": lambda loadout: (
        (draygonArea in loadout)
    ),
    "Swamp Pain Missile": lambda loadout: (
        (spazerGate in loadout) and
        (energy600 in loadout) and
        (GravitySuit in loadout) and
        (Varia in loadout) and
        (SpaceJump in loadout) and
        (Grapple in loadout)
    ),
    "Pain 2 Energy Tank": lambda loadout: (
        (spazerGate in loadout) and
        (energy600 in loadout) and
        (GravitySuit in loadout) and
        (Varia in loadout) and
        (SpaceJump in loadout) and
        (Grapple in loadout) and
        (Wave in loadout)
        #same as pain, but needs Wave
    ),
    "Draygon Door Super Missile": lambda loadout: (
        (draygonDead in loadout)
    ),
    "Varia Suit": lambda loadout: (
        (variaRoom in loadout)
    ),
    "Swamp Moat Power Bomb": lambda loadout: (
        (canUsePB in loadout) and
        (swampSoutheast in loadout)
    ),
    "Swamp Moat Right Missile": lambda loadout: (
        (swampSoutheast in loadout) and
        (Grapple in loadout)
    ),
    "Swamp Moat Island Energy Tank": lambda loadout: (
        (swampSoutheast in loadout) and
        (
            (HiJump in loadout) or
            (GravitySuit in loadout) or
            (canSpeedOrFly in loadout)
        )
    ),
    "Swamp Moat Left Missile": lambda loadout: (
        (swampSoutheast in loadout) and
        (Grapple in loadout)
    ),
    "Swamp H4 Super Missile": lambda loadout: (
        (swampWestFall in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (Plasma in loadout) and
        (Super in loadout)
    ),
    "Below Spazer Super Missile": lambda loadout: (
        (swampSoutheast in loadout) and
        (Super in loadout)
    ),
    "Swamp H1 Super Missile": lambda loadout: (
        (draygonDead in loadout)
    ),
    "Rocky Center Power Bomb": lambda loadout: (
        (rockyFall2 in loadout) and
        (canUsePB in loadout) and
        (
            (GravitySuit in loadout) or
            (Grapple in loadout) or
            (HiJump in loadout)
        ) and
        (energy300 in loadout) and
        (
            (missile20 in loadout) or
            (super12 in loadout) or
            (Plasma in loadout)
        )  
    ),
    "Rocky Southeast Super Missile": lambda loadout: (
        (r3gate in loadout) and
        (Super in loadout) and
        (SpeedBooster in loadout)
    ),
    "Space Jump": lambda loadout: (
        (ridley in loadout) and
        (
            (Ice in loadout) or
            (SpaceJump in loadout) or
            (energy600 in loadout)
        )
    ),
    "Tourian Entrance Missile": lambda loadout: (
        (forestNorthwest in loadout) and
        (Super in loadout) and
        (Plasma in loadout)
    ),
    "Tourian Entrance Power Bomb": lambda loadout: (
        (forestNorthwest in loadout) and
        (Super in loadout) and
        (Plasma in loadout)
    ),
    
    "Rocky East Energy Super Missile": lambda loadout: (
        (Super in loadout) and
        (
            (Morph in loadout) and
            (Grapple in loadout) and
            (canFly in loadout)
        ) or
        (
            (rockyFall2 in loadout) and
            (canUsePB in loadout) and
            (
                (GravitySuit in loadout) or
                (Grapple in loadout) or
                (HiJump in loadout)
            ) and
            (energy300 in loadout) and
            (
                (missile20 in loadout) or
                (super12 in loadout) or
                (Plasma in loadout)
            ) 
        )
    ),
    "Rocky East Energy Tank": lambda loadout: (
        (canSpeedOrFly in loadout) and
        (
            (Morph in loadout) and
            (Grapple in loadout) and
            (canFly in loadout)
        ) or
        (
            (rockyFall2 in loadout) and
            (canUsePB in loadout) and
            (
                (GravitySuit in loadout) or
                (Grapple in loadout) or
                (HiJump in loadout)
            ) and
            (energy300 in loadout) and
            (
                (missile20 in loadout) or
                (super12 in loadout) or
                (Plasma in loadout)
            ) 
        )
    ),
}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
