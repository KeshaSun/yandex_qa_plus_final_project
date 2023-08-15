# Cандюк Иннокентий, 7-я когорта — Финальный проект. Инженер по тестированию плюс

import data

from sender_stand_requests import post_new_order, get_order


def get_new_track():
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.order_body.copy()
    # отправляем запрос
    track_response = post_new_order(current_body).json()
    # получаем номер трека
    return track_response['track']


print(get_new_track())


def test_get_order_by_trak():
    track = get_new_track()
    order = get_order(track)
    assert order.status_code == 200


