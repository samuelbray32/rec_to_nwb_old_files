from ndx_franklab_novela import ShanksElectrode

from rec_to_nwb.processing.nwb.components.device.probe.shanks_electrodes.fl_shanks_electrode import FlShanksElectrode
from rec_to_nwb.processing.tools.beartype.beartype import beartype
from rec_to_nwb.processing.tools.validate_parameters import validate_parameters_not_none


class ShanksElectrodeCreator:

    @classmethod
    @beartype
    def create(cls, fl_shanks_electrode: FlShanksElectrode) -> ShanksElectrode:
        validate_parameters_not_none(__name__, fl_shanks_electrode.shanks_electrode_id,
                                     fl_shanks_electrode.rel_x, fl_shanks_electrode.rel_y, fl_shanks_electrode.rel_z)

        return ShanksElectrode(
            name=str(fl_shanks_electrode.shanks_electrode_id),
            rel_x=float(fl_shanks_electrode.rel_x),
            rel_y=float(fl_shanks_electrode.rel_y),
            rel_z=float(fl_shanks_electrode.rel_z),
        )
