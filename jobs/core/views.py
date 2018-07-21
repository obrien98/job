from django.shortcuts import render, redirect
import os
import stripe



def payment(request):
    # Set your secret key: remember to change this to your live secret key in production
    # See your keys here: https://dashboard.stripe.com/account/apikeys
    stripe.api_key = "sk_test_BJUliYkgS5VZEKFM1UQAz9cF"

    # Token is created using Checkout or Elements!
    # Get the payment token ID submitted by the form:
    token = request.POST['stripeToken']

    charge = stripe.Charge.create(
        amount=999,
        currency='usd',
        description='Example charge',
        source=token,
    )
