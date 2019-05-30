# -*- coding: utf-8 -*-

import falcon


def auth_required(req, res, resource, id):
    if req.context['auth_user'] is None:
        raise Exception("Unauthorized!")
