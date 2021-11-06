let stripePublicKey = $("#strp-public-key").text().slice(1, -1)
let clientSecret = $("#strp-client-secret").text().slice(1, -1)

const stripe = Stripe(stripePublicKey);
const options = {
    clientSecret: clientSecret,
    appearance: {
        theme: 'flat',
    }
};
const elements = stripe.elements(options);

const paymentElement = elements.create('card', {hidePostalCode: true});
paymentElement.mount('#payment-element');

const form = $("#payment-form").get(0);

(paymentElement).on('change', function(event) {
    if (event.error) {
        showMessage(event.error.message);
    }
});


$(form).on('submit', function(ev) {
    ev.preventDefault();
    paymentElement.update({ 'disabled': true});
    $('#submit-payment').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading').fadeToggle(100);

    let saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    let url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: paymentElement,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                if (result.error.type === "card_error" || result.error.type === "validation_error") {
                    showMessage(result.error.message);
                } else {
                    showMessage("An unexpected error occured.");
                }
                $('#payment-form').fadeToggle(100);
                $('#loading').fadeToggle(100);
                paymentElement.update({ 'disabled': false});
                $('#submit-payment').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});

function showMessage(messageText) {
    messageHtml = `<i class="bi bi-exclamation-diamond-fill"></i> ${messageText}`
    const messageContainer = document.querySelector("#error-message");
    messageContainer.classList.remove("hidden");
    messageContainer.innerHTML = messageHtml;
    setTimeout(function () {
        messageContainer.classList.add("hidden");
        messageText.innerHTML = "";
    }, 4000);
}