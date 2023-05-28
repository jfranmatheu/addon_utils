from .reg_property_group import PropertyGroupRegister
from .reg_ui_append import UIAppend
from .reg_rna_sub import subscribe_to_rna_change # RNASubscription
from .reg_timer import new_timer_as_decorator


class RegDeco:
    PROP_GROUP = PropertyGroupRegister
    RNA_SUB = subscribe_to_rna_change
    TIMER = new_timer_as_decorator
    UI_APPEND = UIAppend
