import pandas as pd
from create_df import create_random_df


def apply_session_id(target_df: pd.DataFrame) -> None:
    """
    Проставление session_id для датафрейма
    :param target_df: целевой датафрейм
    :type target_df: pd.DataFrame
    :return: None
    """

    id_generator = (ses_id for ses_id in range(1, len(target_df) + 1))

    def get_session_df(cur_row: pd.Series) -> pd.DataFrame:
        """
        Генерация датафрейма с предыдущими соседями по сессии

        :param cur_row: строка датафрейма
        :type cur_row: pd.Series
        :return: датафрейма с предыдущими соседями по сессии
        """

        customer_id = cur_row.loc['customer_id']
        timestamp = cur_row.loc['timestamp']

        cur_session_df = target_df[
            ((target_df['customer_id'] == customer_id)
             & (target_df['timestamp'] >= timestamp - 180)
             & (target_df['timestamp'] <= timestamp))
        ]
        return cur_session_df

    def unique_session_generator(cur_row: pd.Series) -> int:
        """
        Определение уникальных session_id.
        Записи, относящиеся к уже существующей сессии маркируются нулём.

        :param cur_row: строка датафрейма
        :type cur_row: pd.Series
        :return: id сессии
        """

        nonlocal id_generator
        cur_session_df = get_session_df(cur_row)

        if len(cur_session_df) == 1:
            return next(id_generator)
        else:
            return 0

    def session_id_specifier(cur_row: pd.Series) -> int:
        """
        Определение session_id для записей, относящихся к существующим сессиям на основе ближайших соседей
        :param cur_row: строка датафрейма
        :type cur_row: pd.Series
        :return: id сессии
        """

        session_id = cur_row.loc['session_id']
        if session_id == 0:
            cur_session_df = get_session_df(cur_row)
            session_id = cur_session_df['session_id'].max()
            return session_id
        else:
            return session_id

    target_df.sort_values(by='timestamp', ascending=True)
    target_df['session_id'] = target_df.apply(unique_session_generator, axis=1)
    while 0 in target_df['session_id'].unique():
        target_df['session_id'] = target_df.apply(session_id_specifier, axis=1)


if __name__ == '__main__':
    df = create_random_df(10000, 100, 60 * 24)
    print('Исходный датафрейм')
    print(df)
    apply_session_id(df)
    print('\nТрансформированный датафрейм:')
    print(df)
