# ===   Возьмите любую 1 задачу из прошлых домашних заданий.
# ===   Добавьте к ним логирование ошибок и полезной информации.
# ===   Также реализуйте возможность запуска из командной строки с передачей параметров.


#  Задача из урока 6 - Проверка существования переданной даты
import argparse
import logging
import datetime

logging.basicConfig(filename="task_7.log", encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def is_exist(input_date: str) -> bool:
    day, month, year = list(map(int, input_date.split('.')))

    logger.info(f"Day {day} Month {month} Year {year}")

    if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999:
        match month:
            case 4 | 6 | 9 | 11:
                if day == 31:
                    return False
            case 2:
                if day == 29 and not _is_leap_year(year) or day > 29:
                    return False
                return True
            case _:
                return True
    return False


# проверка года на високосность
def _is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        logger.info(f"Year {year} is leap")
        return True
    if year % 100 == 0:
        logger.info(f"Year {year} is leap")
        return False
    if year % 4 == 0:
        logger.info(f"Year {year} is leap")
        return True

    logger.info(f"Year {year} is not leap")
    return False


# run module
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Дата в формате DD.MM.YYYY")
    parser.add_argument('--date', default=str(datetime.date))
    args = parser.parse_args()
    is_exist(args.date)

