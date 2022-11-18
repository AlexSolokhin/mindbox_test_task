import pandas as pd
import numpy as np
import time


def create_random_df(length: int, customers: int, timeframe: int) -> pd.DataFrame:
    """
    Создание датафрейма со случайными данными.

    :param length: количество записей в датафрейме
    :type length: int
    :param customers: количество клиентов
    :type customers: int
    :param timeframe: период до настоящего момента (в минутах)
    :return: pd.DataFrame
    """

    time_start = time.time() - 60 * timeframe
    time_end = time.time()
    mapper_func = lambda rand: rand * (time_end - time_start) + time_start
    customer_id_list = np.random.randint(customers, size=length)
    product_id_list = np.random.randint(50, size=length)
    timestamp_list = mapper_func(np.random.rand(length))

    df = pd.DataFrame({'customer_id': customer_id_list, 'product_id': product_id_list, 'timestamp': timestamp_list})

    return df
