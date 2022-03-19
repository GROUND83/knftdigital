from django import forms

CONTACT_TYPE_CHOICES = (
    ("1", "collect"),
    ("2", "contact"),
)


HELP_TYPE_CHOICES = [
    ("Buying NFTs", "Buying NFTs"),
    ("Question about NFT art", "Question about NFT art"),
    ("Participating in an NFT project", "Participating in an NFT project"),
    ("Question about K-NFT", "Question about K-NFT"),
    ("Partnering with K-NFT", "Partnering with K-NFT"),
    ("Other", "Other"),
]


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your full name", "class": "mt-1 outline-none"}
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your Email", "class": "mt-1 outline-none"}
        ),
    )

    helpType = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "mt-1 outline-none"}),
        choices=HELP_TYPE_CHOICES,
        initial="Buying NFTs",
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"placeholder": "Type your Message", "class": "mt-1 outline-none"}
        ),
    )


class SubscripbleForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your Email", "class": "mt-1 outline-none"}
        ),
    )
