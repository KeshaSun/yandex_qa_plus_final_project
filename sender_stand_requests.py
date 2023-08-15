from requests import post, get

from configuration import CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH


# получение номера трека

def post_new_order(body: dict[str, str]):
    return post(
        CREATE_ORDER_PATH,
        json=body,
    )


# получение заказа по его трек номеру


def get_order(track_id):
    payload = {'t': track_id}
    r = get(
        GET_ORDER_BY_TRACK_PATH,
        params=payload
    )
    return r
