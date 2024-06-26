from ndx_franklab_novela import CameraDevice, DataAcqDevice, HeaderDevice, Probe
from pynwb.device import Device
from rec_to_nwb.processing.nwb.components.device.acq.fl_data_acq_device import \
    FlDataAcqDevice
from rec_to_nwb.processing.nwb.components.device.camera.fl_camera_device import \
    FlCameraDevice
from rec_to_nwb.processing.nwb.components.device.fl_device import FlDevice
from rec_to_nwb.processing.nwb.components.device.header.fl_header_device import \
    FlHeaderDevice
from rec_to_nwb.processing.nwb.components.device.probe.fl_probe import FlProbe
from rec_to_nwb.processing.tools.beartype.beartype import beartype
from rec_to_nwb.processing.tools.validate_parameters import \
    validate_parameters_not_none


class DeviceFactory:

    @classmethod
    @beartype
    def create_device(cls, fl_device: FlDevice) -> Device:
        validate_parameters_not_none(__name__, fl_device.name)
        return Device(
            name=str(fl_device.name)
        )

    @classmethod
    @beartype
    def create_camera_device(cls, fl_camera_device: FlCameraDevice) -> CameraDevice:
        validate_parameters_not_none(
            __name__, fl_camera_device.name, fl_camera_device.meters_per_pixel)
        return CameraDevice(
            name=fl_camera_device.name,
            meters_per_pixel=fl_camera_device.meters_per_pixel,
            manufacturer=fl_camera_device.manufacturer,
            model=fl_camera_device.model,
            lens=fl_camera_device.lens,
            camera_name=fl_camera_device.camera_name
        )

    @classmethod
    @beartype
    def create_probe(cls, fl_probe: FlProbe) -> Probe:
        validate_parameters_not_none(__name__, fl_probe.probe_id, fl_probe.name, fl_probe.probe_type, fl_probe.units,
                                     fl_probe.probe_description, fl_probe.contact_side_numbering,
                                     fl_probe.contact_size, fl_probe.shanks)
        probe = Probe(
            id=fl_probe.probe_id,
            name=fl_probe.name,
            probe_type=fl_probe.probe_type,
            units=fl_probe.units,
            probe_description=fl_probe.probe_description,
            contact_side_numbering=fl_probe.contact_side_numbering,
            contact_size=fl_probe.contact_size
        )
        for shank in fl_probe.shanks:
            probe.add_shank(shank)

        return probe

    @classmethod
    @beartype
    def create_data_acq_device(cls, fl_data_acq_device: FlDataAcqDevice) -> DataAcqDevice:
        validate_parameters_not_none(__name__, fl_data_acq_device.name, fl_data_acq_device.system,
                                     fl_data_acq_device.amplifier, fl_data_acq_device.adc_circuit)
        return DataAcqDevice(
            name=fl_data_acq_device.name,
            system=fl_data_acq_device.system,
            amplifier=fl_data_acq_device.amplifier,
            adc_circuit=fl_data_acq_device.adc_circuit
        )

    @classmethod
    @beartype
    def create_header_device(cls, fl_header_device: FlHeaderDevice) -> HeaderDevice:
        validate_parameters_not_none(
            __name__, fl_header_device.name, fl_header_device.global_configuration)
        return HeaderDevice(
            name=fl_header_device.name,
            headstage_serial=fl_header_device.global_configuration['headstage_serial'],
            headstage_smart_ref_on=fl_header_device.global_configuration['headstage_smart_ref_on'],
            realtime_mode=fl_header_device.global_configuration['realtime_mode'],
            headstage_auto_settle_on=fl_header_device.global_configuration[
                'headstage_auto_settle_on'],
            timestamp_at_creation=fl_header_device.global_configuration['timestamp_at_creation'],
            controller_firmware_version=fl_header_device.global_configuration[
                'controller_firmware_version'],
            controller_serial=fl_header_device.global_configuration['controller_serial'],
            save_displayed_chan_only=fl_header_device.global_configuration[
                'save_displayed_chan_only'],
            headstage_firmware_version=fl_header_device.global_configuration[
                'headstage_firmware_version'],
            qt_version=fl_header_device.global_configuration['qt_version'],
            compile_date=fl_header_device.global_configuration['compile_date'],
            compile_time=fl_header_device.global_configuration['compile_time'],
            file_prefix=fl_header_device.global_configuration['file_prefix'],
            headstage_gyro_sensor_on=fl_header_device.global_configuration[
                'headstage_gyro_sensor_on'],
            headstage_mag_sensor_on=fl_header_device.global_configuration[
                'headstage_mag_sensor_on'],
            trodes_version=fl_header_device.global_configuration['trodes_version'],
            headstage_accel_sensor_on=fl_header_device.global_configuration[
                'headstage_accel_sensor_on'],
            commit_head=fl_header_device.global_configuration['commit_head'],
            system_time_at_creation=fl_header_device.global_configuration[
                'system_time_at_creation'],
            file_path=fl_header_device.global_configuration['file_path']
        )
