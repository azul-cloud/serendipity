$(document).ready(function() {
  //===== Shopping =====//
  /* in the shopping section we're going to be performing actions 
    that aid the shopping cart. */

  // define shopping variables
  shopping_add_url = '/shopping/add/'
  shopping_remove_url = '/shopping/remove/'
  shopping_cart_url = '/shopping/cart/'

  $(document).on('click', '.add-to-cart', function(e) {
    /* this function will add the item into the cart via the
       shared product panel template */
    e.preventDefault();
    id = $(this).data('id');
    url = shopping_add_url + id + '/';
    $.get(url);

    // after the item is added change the anchor element
    $(this).removeClass('add-to-cart');
    $(this).text('View in Cart');
    $(this).attr('href', shopping_cart_url);
  });

  $(document).on('click', '.cart-remove-item', function() {
    // removes the item from the cart, used on the cart page
    row = $(this).parent().parent();
    id = row.data('id');

    url = shopping_remove_url + id + '/';
    $.get(url);

    row.remove();
  });

  function updateCart(element, action) {
    /* update the cart data by either incrementing the item or 
        decrementing it */

    row = $(element).parent().parent();
    id = row.data('id');
    subtotalCell = row.find('td.subtotal');
    priceCell = row.find('td.price');
    quantityCell = row.find('td.quantity');

    // get the price
    priceText = priceCell.text().replace('$', '')
    price = parseFloat(priceText).toFixed(2)
    console.log(price);

    // update the quantity data
    quantityStr = quantityCell.text();
    quantity = parseInt(quantityStr);
    if (action == "increment") {
        quantity += 1;
    }
    else if (action == "decrement") {
        quantity -= 1;
    }
    quantityCell.text(quantity);

    // update the subtotal data
    subtotalStr = subtotalCell.text();
    originalSubtotal = parseFloat(priceText).toFixed(2);
    newSubtotal = parseFloat(quantity * price).toFixed(2);
    subtotalCell.text(newSubtotal);

    // hit the server API URL
    if (action == "increment") {
        url = shopping_add_url + id + '/';;
    }
    else if (action == "decrement") {
        url = shopping_remove_url + id + '/';;
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



