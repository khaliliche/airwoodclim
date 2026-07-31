from urllib.parse import quote
from django.conf import settings
from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem


def checkout(request):
    cart = Cart(request)

    if len(cart) == 0:
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            lines = ["Bonjour, je veux passer ma commande :"]
            for item in cart:
                lines.append(f"- {item['product'].name} x{item['quantity']}")
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    product_name=item['product'].name,
                    price=item['price'],
                    quantity=item['quantity'],
                )

            lines.append("")
            lines.append(f"Nom: {order.name}")
            lines.append(f"Telephone: {order.phone}")
            lines.append(f"Ville: {order.city}")
            lines.append(f"Adresse: {order.address}")

            message = "\n".join(lines)
            cart.clear()

            whatsapp_url = f"https://wa.me/{settings.WHATSAPP_NUMBER}?text={quote(message)}"
            return redirect(whatsapp_url)
    else:
        form = OrderCreateForm()

    return render(request, 'orders/checkout.html', {'cart': cart, 'form': form})