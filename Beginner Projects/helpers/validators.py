from questionary import Validator, ValidationError

"""Simple validator class used by interative CLI implemented using questionary package to ensure user input."""
class valueValidator(Validator):
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message="Please enter a value",
                cursor_position=len(document.text),
            )
