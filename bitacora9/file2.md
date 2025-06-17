# Crear un historial de las modificaciones que realiza un usuario a los campos del formulario Órdenes de Servicio cuando se edita

El siguiente fragmento de código corresponde a la función que se encarga de guardar los cambios cuando se edtita una orden ya creada. Por cada campo modificado se agregó una condición que valida si se modificó. Si se modifica el campo se crea el mensaje con el nuevo valor.

```python
    def write(self, vals):
        # self.env['mail.message'].create({
        #     'body': "Se actualizo informacion documento",
        #     'model': 'motion.service_orders',
        #     'res_id': self.id,
        # })
               
        if 'employee_id' in vals and vals['employee_id'] and self.stage_id == 1:
            vals['state'] = 'assigned'
        res = super(serviceOrder, self).write(vals)        
        for record in self:
            if 'partner_id' in vals and vals['partner_id']:
                record.message_post(
                    body=f"{record.write_uid.name} editó la orden de servicio y cambió el cliente a: <b>{record.partner_id.name}</b>")
            if 'wialon_unit' in vals and vals['wialon_unit']:
                record.message_post(
                    body=f"{record.write_uid.name} editó la orden de servicio y cambió el vehiculo wialon a: <b>{record.wialon_unit.name}</b>")            
            if 'service_type' in vals and vals['service_type']:
                record.message_post(
                    body=f"{record.write_uid.name} editó la orden y cambió el tipo de servicio a: <b>{record.service_type}</b>")            
            if 'service_obs' in vals and vals['service_obs']:
                record.message_post(
                    body=f"{record.write_uid.name} editó la orden y cambió las observaciones del servicio a: <b>{record.service_obs}</b>")
            if 'employee_id' in vals and vals['employee_id']:
                record.message_post(
                    body=f"{record.write_uid.name} editó la orden y cambió el empleado asignado a: <b>{record.employee_id.name}</b>")                
        return res
```