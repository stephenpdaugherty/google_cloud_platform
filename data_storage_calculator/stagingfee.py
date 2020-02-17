import numpy
#Add numpy to requirements.txt in cloud function

def calculations(request):
    #Form Inputs
    start = request.args.get('start')
    end = request.args.get('end')
    size_str = request.args.get('size')

    if ',' in size_str:
        size_str = size_str.replace(',', '')
    size = float(size_str)

    distance = float(numpy.busday_count(start, end, weekmask='1111111'))
    distance_int = int(distance)
    cost_rate = 0.026
    monthly_cost = (size * cost_rate)
    daily_cost = (monthly_cost / 30)
    total_cost = (daily_cost * distance)

    feedback = f'RATE: ${cost_rate} | \
    CALENDAR DAYS: {distance_int} | \
    DAILY COST: ${daily_cost} | TOTAL COST: ${total_cost}'

    return feedback
