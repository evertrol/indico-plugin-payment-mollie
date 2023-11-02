# This file is part of the Indico plugins.
# Copyright (C) 2023 Evert Rol, University of Amsterdam
#
# The Indico plugins are free software; you can redistribute
# them and/or modify them under the terms of the MIT License;
# see the LICENSE file for more details.

from indico.core.plugins import IndicoPluginBlueprint

from indico_payment_mollie.controllers import (RHInitMolliePayment, MollieNotificationHandler, UserCancelHandler,
                                               UserFailureHandler, UserSuccessHandler)


blueprint = IndicoPluginBlueprint(
    'payment_mollie', __name__,
    url_prefix='/event/<int:event_id>/registrations/<int:reg_form_id>/payment/mollie'
)

blueprint.add_url_rule('/init', 'init', RHInitMolliePayment, methods=('GET', 'POST'))
blueprint.add_url_rule('/failure', 'failure', UserFailureHandler, methods=('GET', 'POST'))
blueprint.add_url_rule('/cancel', 'cancel', UserCancelHandler, methods=('GET', 'POST'))
blueprint.add_url_rule('/success', 'success', UserSuccessHandler, methods=('GET', 'POST'))
blueprint.add_url_rule('/notify', 'notify', MollieNotificationHandler, methods=('Get', 'POST'))
