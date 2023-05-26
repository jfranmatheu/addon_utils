from .ops import OperatorTypes, OpsReturn, ModalFlags
from .preferences import AddonPreferences
from .ui import InterfaceTypes, PanelFlags
from .property_group import PropertyGroup


class RegType:
    PREFS = AddonPreferences
    UI = InterfaceTypes
    OPS = OperatorTypes
    PROP_GROUP = PropertyGroup