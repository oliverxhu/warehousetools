from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'labels/index.html')


def label(request, barcode, pallet_number, sku, supplier):
    sep = ';;'
    barcode_list = str(barcode).split(sep=sep)
    pallet_number_list = str(pallet_number).split(sep=sep)
    sku_list = str(sku).split(sep=sep)
    supplier_list = str(supplier).split(sep=sep)

    pallet_ranges = []
    for n in pallet_number_list:
        pallet_ranges.append(list(range(1, int(n)+1)))

    parameter_list = list(zip(pallet_ranges, barcode_list, sku_list, supplier_list))

    return render(request, 'labels/label.html', {
        'parameters': parameter_list
    })
