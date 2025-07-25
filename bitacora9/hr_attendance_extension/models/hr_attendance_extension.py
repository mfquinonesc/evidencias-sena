# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


class hr_attendance_extension(models.Model):   
    _inherit = 'hr.attendance'  

    weekly_hours = fields.Float(string='Weekly Hours', compute="_compute_weekly_hours", store=False)

    def _get_week_boundaries(self, ref_date):
        """Return (start, end) of the ISO week of ref_date."""
        iso_year, iso_week, _ = ref_date.isocalendar()
        start = datetime.strptime(f'{iso_year}-W{iso_week}-1', "%G-W%V-%u")
        end = start + timedelta(days=7)
        return start, end


    def _get_total_weekly_hours(self, employee_id, ref_date=None):
        """Return total worked hours for the employee in the week of ref_date."""
        ref_date = ref_date or fields.Date.context_today(self)
        start, end = self._get_week_boundaries(ref_date)

        attendances = self.search([
            ('employee_id', '=', employee_id),
            ('check_in', '>=', start),
            ('check_in', '<', end),
            ('check_out', '!=', False),
        ])

        return sum(
            (a.check_out - a.check_in).total_seconds() / 3600
            for a in attendances
        )

 
    @api.depends('check_in', 'check_out')
    def _compute_weekly_hours(self):
        for record in self:
            if record.employee_id and record.check_in:
                record.weekly_hours = self._get_total_weekly_hours(
                    record.employee_id.id,
                    record.check_in.date()
                )
            else:
                record.weekly_hours = 0.0

   
    @api.model
    def get_weekly_hours(self):
        """Return the weekly worked hours of the current user's employee."""
        employee = self.env.user.employee_id
        if not employee:
            return 0.0
        total = self._get_total_weekly_hours(employee.id)
        return round(total, 2)
      

    @api.model
    def set_lunch_hour(self):
        """Set the lunch hour for the current user."""
        employee = self.env.user.employee_id
        if not employee:
            return None

        # Close current attendance
        last_attendance = self.search([
            ('employee_id', '=', employee.id),
            ('check_out', '=', False)
        ], limit=1, order='check_in desc')

        check_out = fields.Datetime.now()

        if last_attendance:
            last_attendance.write({'check_out': check_out })

        # Create new check-in for after lunch
        check_in = check_out + timedelta(hours=1)
        self.create({
            'employee_id': employee.id,
            'check_in': check_in,
        })

        return {
            'check_out': check_out,
            'check_in': check_in,
        }


    @api.model
    def get_lunch_check_in(self):
        """Retrieves the next attendance record marked as a lunch check-in for the current user's employee."""  
        employee = self.env.user.employee_id
        if not employee:
            return None
        
        now = fields.Datetime.now()
        
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
      
        # Get all today's attendances ordered by check_in
        attendances_today = self.search([
            ('employee_id', '=', employee.id),
            ('check_in', '>=', today_start),
            ('check_in', '<', today_end),          
        ], order='check_in asc')

        # Loop through consecutive attendances
        for i in range(len(attendances_today) - 1):
            current = attendances_today[i]
            next_att = attendances_today[i + 1]

            if current.check_out and next_att.check_in:
                gap = (next_att.check_in - current.check_out).total_seconds() / 3600

                if gap > 0.9: 
                    return next_att.read(['id', 'check_in', 'check_out', 'employee_id'])[0]

        return None
