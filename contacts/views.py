from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SubscripbleForm
from .models import Contact
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        # form["type"] = "1"
        if contact_form.is_valid():
            email = contact_form.cleaned_data["email"]
            name = contact_form.cleaned_data["name"]
            type = "contact"
            helpType = contact_form.cleaned_data["helpType"]
            message = contact_form.cleaned_data["message"]
            messagetext = f"{name}\n{message}\nfrom {email}"
            send_mail(
                helpType,
                messagetext,
                "info@k-nft.io",
                ["info@k-nft.io"],
                fail_silently=False,
            )

            Contact.objects.create(
                email=email, type=type, helpType=helpType, name=name, message=message
            )

            return render(request, "success.html")
    else:
        form_class = ContactForm()
        return render(
            request,
            "contact.html",
            {
                "form": form_class,
            },
        )


def emailsubscription(request):
    # if request.method == "GET":
    #     contact_form = SubscripbleForm()
    #     return render(request, "partials/footer.html", {"form": contact_form})
    # else:
    if request.method == "POST":
        contact_form = SubscripbleForm(request.POST)
        print(contact_form)
        if contact_form.is_valid():
            email = contact_form.cleaned_data["email"]
            type = "collect"
            helpType = "Other"
            print(email)
            # contact_form.save()
            try:
                Contact.objects.create(email=email, type=type, helpType=helpType)
                return render(request, "success.html")
            except:
                pass
        else:
            pass
    else:
        form_class = ContactForm()
        return render(
            request,
            "partials/footer.html",
            {
                "form": form_class,
            },
        )
