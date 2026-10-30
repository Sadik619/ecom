from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Product


def customer_list(request):
    customers = Customer.objects.all()

    return render(
        request,
        "shop/customer.html",
        {"customers": customers}
    )


def customer_create(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")

        Customer.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address
        )

        return redirect("customer_list")

    return render(request, "shop/customer_add.html")


# def customer_update(request, id):

#     customer = get_object_or_404(Customer, id=id)

#     if request.method == "POST":

#         customer.name = request.POST.get("name")
#         customer.email = request.POST.get("email")
#         customer.phone_number = request.POST.get("phone_number")
#         customer.address = request.POST.get("address")

#         customer.save()

#         return redirect("customer_list")

#     return render(
#         request,
#         "shop/customer_add.html",
#         {"customer": customer}
#     )

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Customer

def customer_update(request, id):

    customer = get_object_or_404(Customer, id=id)

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        # Check duplicate email excluding current customer
        if Customer.objects.filter(email=email).exclude(id=id).exists():

            return render(request, 'shop/customer.html', {
                'customer': customer,
                'customers': Customer.objects.all(),
                'error': 'Email already exists!'
            })

        customer.name = name
        customer.email = email
        customer.phone_number = phone_number
        customer.address = address

        customer.save()

        return redirect('customer_list')

    return render(request, 'shop/customer_add.html', {
        'customer': customer,
        'customers': Customer.objects.all()
    })



def customer_delete(request, id):

    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        customer.delete()
        return redirect("customer_list")

    return render(
        request,
        "shop/customer_delete_form.html",
        {"customer": customer}
    )
def product_list(request):

    products = Product.objects.all()

    return render(
        request,
        "shop/product_list.html",
        {"products": products}
    )


def product_create(request):

    if request.method == "POST":

        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        stock = request.POST.get("stock")

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock
        )

        return redirect("product_list")

    return render(request, "shop/product_add.html")


def product_update(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":

        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")

        product.save()

        return redirect("product_list")

    return render(
        request,
        "shop/product_add.html",
        {"product": product}
    )


def product_delete(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":

        product.delete()

        return redirect("product_list")

    return render(
        request,
        "shop/product_delete_form.html",
        {"product": product}
    )