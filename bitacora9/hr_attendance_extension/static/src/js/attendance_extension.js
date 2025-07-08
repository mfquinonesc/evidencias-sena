odoo.define('hr_attendance_extension.hr_attendance_extension', function (require) {
    'use strict';   

    const defaultAttendances = require('hr_attendance.my_attendances');

    const rpc = require('web.rpc');

    const floatToHHMM = (hoursFloat) =>{
        const hours = Math.floor(hoursFloat);
        const minutes = Math.round((hoursFloat - hours) * 60);
        const paddedHours = String(hours).padStart(2, '0');
        const paddedMinutes = String(minutes).padStart(2, '0');
        return `${paddedHours}:${paddedMinutes}`;
    }

    const attendanceExtension = defaultAttendances.include({
         start: async function () {           
            await this._super.apply(this, arguments);

            const result = await rpc.query({
                model: 'hr.attendance',
                method: 'get_weekly_hours',
                args: [],
            });

            const container = this.$el.find('h4, h3').first();
            container.append(`<div class="alert alert-info mt-2">
                Weekly Hours: ${floatToHHMM(result)} hours
            </div>`);  

            return Promise.resolve();
        },
    });

    return attendanceExtension;
});