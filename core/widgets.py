from django.forms import RadioSelect


class GovbrSelect(RadioSelect):
    template_name = "widgets/select.html"
    option_template_name = "widgets/radio_option.html"
