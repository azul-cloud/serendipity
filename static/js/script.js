$(document).ready(function() {
  //===== Shopping =====//
  /* in the shopping section we're going to be performing actions 
    that aid the shopping cart. */

  // define global shopping variables
  var shoppingAddUrl = '/shopping/add/',
      shoppingRemoveUrl = '/shopping/remove/',
      shoppingRemoveSingleUrl = '/shopping/removesingle/',
      shoppingCartUrl = '/shopping/cart/',
      shoppingTotalCell = $('#total-cell');


  $(document).on('click', '.add-to-cart', function(e) {
    /* this function will add the item into the cart via the
       shared product panel template */
    e.preventDefault();
    var id = $(this).data('id'),
        url = shoppingAddUrl + id + '/';
    
    $.get(url);

    // after the item is added change the anchor element
    $(this).removeClass('add-to-cart');
    $(this).text('View in Cart');
    $(this).attr('href', shoppingCartUrl);
  });


  $(document).on('click', '.cart-remove-item', function() {
    // removes the item from the cart, used on the cart page
    var row = $(this).parent().parent(),
        id = row.data('id'),
        url = shoppingRemoveUrl + id + '/',
        subtotalCell = row.find('td.subtotal'),
        subtotalStr = subtotalCell.text().replace('$', ''),
        subtotal = +parseFloat(subtotalStr) * -1;

        updateTotal(subtotal);

    $.get(url);
    row.remove();
  });


  function updateTotal(amount) {
    /* update the total in the cart in both the table cell and
        in the stripe button data-amount */
    var totalStr = shoppingTotalCell.text().replace('$', ''),
        originalTotal = parseFloat(totalStr),
        newTotal = Math.round(originalTotal + amount, 2),
        newStripeTotal = newTotal * 100,
        newTotalStr = newTotal.toFixed(2),
        amount_obj = $("#stripeAmount");

    shoppingTotalCell.text('$' + newTotalStr);
    amount_obj.val(newStripeTotal);
  }


  function updateCart(element, action) {
    /* update the cart data by either incrementing the item or 
        decrementing it */

    var row = $(element).parent().parent(),
        id = row.data('id'),
        subtotalCell = row.find('td.subtotal'),
        priceCell = row.find('td.price'),
        quantityCell = row.find('td.quantity');

    // get the price
    var priceText = priceCell.text().replace('$', ''),
        price = parseFloat(priceText).toFixed(2);

    // update the quantity data
    var quantityStr = quantityCell.text(),
        quantity = parseInt(quantityStr);
    
    if (action == "increment") {
        quantity += 1;
    }
    else if (action == "decrement") {
        quantity -= 1;
    }

    quantityCell.text(quantity);

    // get the original subtotal
    var subtotalStr = subtotalCell.text().replace('$', ''),
        originalSubtotal = parseFloat(subtotalStr).toFixed(2);

    // update the subtotal data
    var newSubtotal = parseFloat(quantity * price).toFixed(2);
    subtotalCell.text('$' + String(newSubtotal));

    // update the totals in the table and in the script data-amount
    var changeAmount = +parseFloat(newSubtotal - originalSubtotal).toFixed(2);

    updateTotal(changeAmount);

    // hit the server API URL
    if (action == "increment") {
        url = shoppingAddUrl + id + '/';;
    }
    else if (action == "decrement") {
        url = shoppingRemoveSingleUrl + id + '/';;
    }
    $.get(url); 
  }


  $(document).on('click', '.cart-increment-item', function() {
    updateCart($(this), 'increment');
  });


  $(document).on('click', '.cart-decrement-item', function() {
    updateCart($(this), 'decrement');
  });
}); 



