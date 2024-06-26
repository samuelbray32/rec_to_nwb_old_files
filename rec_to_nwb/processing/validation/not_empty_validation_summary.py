from rec_to_nwb.processing.validation.validation_summary import \
    ValidationSummary


class NotEmptyValidationSummary(ValidationSummary):

    def __init__(self, parameter):
        self.parameter = parameter

    def is_valid(self):
        return bool(self.parameter)
