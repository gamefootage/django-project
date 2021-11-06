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

const paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');


$("#payment-form").on('submit', async (event) => {
  event.preventDefault();

  const {error} = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
    elements,
    confirmParams: {
      return_url: 'http://127.0.0.1:8000/checkout/',
    },
  });

  if (error) {
    // This point will only be reached if there is an immediate error when
    // confirming the payment. Show error to your customer (e.g., payment
    // details incomplete)
    const $messageContainer = $('#error-message');
    $messageContainer.text(error.message);
  } else {
    // Your customer will be redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer will be redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});