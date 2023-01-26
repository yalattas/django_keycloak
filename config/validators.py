from django.core.validators import RegexValidator

_NAME_REGEX = RegexValidator(
    regex=r"^[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z]+[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z ]*$", message=("Special characters and digits are now allowed."),
)
_PHONE_REGEX = RegexValidator(
    regex=r"^05\d{8}$", message=("Mobile number must be 10 digits starting with '05'."),
)