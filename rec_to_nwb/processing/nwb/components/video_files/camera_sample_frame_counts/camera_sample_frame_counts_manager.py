"""Gets the video frame counts and timestamps for all epochs and inserts them
into an NWB timeseries object"""
from rec_to_nwb.processing.nwb.components.video_files.camera_sample_frame_counts.camera_sample_frame_counts_builder import \
    CameraSampleFrameCountsBuilder
from rec_to_nwb.processing.nwb.components.video_files.camera_sample_frame_counts.camera_sample_frame_counts_extractor import \
    CameraSampleFrameCountsExtractor


class CameraSampleFrameCountsManager:
    def __init__(self, raw_data_path):
        self.extractor = CameraSampleFrameCountsExtractor(raw_data_path)

    def get_timeseries(self):
        """Gets the video frame counts and timestamps for all epochs and
        inserts them into an NWB timeseries object"""
        data = self.extractor.extract()
        builder = CameraSampleFrameCountsBuilder(data)
        return builder.build()
