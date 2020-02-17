import numpy
#Add numpy to requirements.txt in cloud function

def calculations(request):
    #Form Inputs
    start = request.args.get('start')
    end = request.args.get('end')
    appliance = str(request.args.get('appliance'))

    distance = numpy.busday_count(start, end)

    if appliance == 'ta100':
        cost_rate = 30

    if appliance =='ta480':
        cost_rate = 90

    total_fees = cost_rate * distance

    feedback = f'APPLIANCE: {appliance} | \
    TOTAL LATE DAYS: {distance} | \
    DAILY RATE: ${cost_rate} | \
    TOTAL FEES: ${total_fees}'

    return feedback
