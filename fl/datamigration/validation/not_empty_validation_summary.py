from fl.datamigration.validation.validation_summary import ValidationSummary


class NotEmptyValidationSummary(ValidationSummary):

    def __init__(self, parameter):
        self.parameter = parameter

    def isValid(self):
        if self.parameter:
            return True
        else:
            return False
