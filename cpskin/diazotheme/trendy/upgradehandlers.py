# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger('cpskin.diazotheme.trendy')


def upgrade_to_less(context):
    context.runImportStepFromProfile(
        'profile-cpskin.diazotheme.trendy:default',
        'lessregistry'
    )
    logger.info('LESS files installed and configurations done !')
