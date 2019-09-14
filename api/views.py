# -*- coding:utf-8 -*-
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from info.models import Scheme


class Ticket(APIView):
    '''
    func get: 根据月份返回对应的ticket信息
    '''

    def get(self, request, *args, **kwargs):
        months = request.GET.get('months')
        scheme_id = request.GET.get('s_id')
        scheme = Scheme.objects.filter(_id=scheme_id).first()
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        if not scheme:
            return Response({'code': 4001, 'error': '套餐不存在'})
        if months == '' or months == '00':
            # 未指定月份,返回当天以后的票务信息
            tickets = scheme.tickets
            response_tickets = []
            for ticket in tickets:
                if ticket.start_date == current_date:
                    current_date_index = tickets.index(ticket)
                    response_tickets = tickets[current_date_index:current_date_index + 30]
                    break
            if response_tickets:
                response_tickets = [
                    {'start_date': ticket.start_date, 'end_date': ticket.end_date, 'surplus': ticket.surplus,
                     'unit_price': ticket.unit_price} for ticket in response_tickets]
            return Response({'code': 2001, 'tickets': response_tickets})
        else:
            months = months.split(',')
            months = filter(lambda x: int(x) >= current_month, months)
            year_months = []
            for month in months:
                year_months.append(str(current_year) + "-" + month)
            ticket_months = scheme.ticket_month
            year_month_intersection = list(set(year_months) & set(ticket_months))
            if not year_month_intersection:
                return Response({'code': 2001, 'tickets': []})
            else:
                tickets = scheme.tickets
                if len(str(current_month)) == 1:
                    current_month = '0' + str(current_month)
                current_year_month = str(current_year) + "-" + str(current_month)
                response_tickets = []
                if current_year_month in year_month_intersection:
                    year_months.remove(current_year_month)
                    for ticket in tickets:
                        if ticket.start_date.startswith(current_year_month):
                            response_tickets.append(ticket)
                    for ticket in response_tickets:
                        if ticket.start_date == current_date:
                            current_date_index = tickets.index(ticket)
                            response_tickets = response_tickets[current_date_index::]
                for year_month in year_months:
                    for ticket in tickets:
                        if ticket.start_date.startswith(year_month):
                            response_tickets.append(ticket)
                if response_tickets:
                    response_tickets = [
                        {'start_date': ticket.start_date, 'end_date': ticket.end_date, 'surplus': ticket.surplus,
                         'unit_price': ticket.unit_price} for ticket in response_tickets]
                    return Response({'code': 2001, 'tickets': response_tickets})
