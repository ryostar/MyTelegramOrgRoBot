#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Shrimadhav U K
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" BƯỚC 1 """

import requests


def request_tg_code_get_random_hash(input_phone_number):
    """ yêu cầu Mã đăng nhập
    và trả về một random_hash
    được sử dụng trong BƯỚC HAI """
    request_url = "https://my.telegram.org/auth/send_password"
    request_data = {
        "phone": input_phone_number
    }
    response_c = requests.post(request_url, data=request_data)
    json_response = response_c.json()
    return json_response["random_hash"]
