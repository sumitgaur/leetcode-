class Booking:
    pass


def create_booking(request, db):
    booking = Booking(
        user_id=request["user_id"],
        room_id=request["room_id"],
        status="CONFIRMED"
    )
    db.add(booking)
    db.commit()

    charge_card(request["user_id"], request["amount"])
    return booking

'''
correctness -> consistency->concurrency-> performance and scalability->security->error handling->maintainability ->testability   
#1 Booking is created and marked confirmed but charge API failed, data becomes inconsistent -- idempotency no key 
#2 Two booking are coming for same room by different users, race condition, no locking 
#3 perf is ok, what if huge number of requests coming for same hotel/room, payment gateway should be async, booking should be marked pending_payment, webhook from payment to set paid, 
#4 no logging, mockable 

'''


class SupplyQueryDateType(Enum):
    BOOKING_DATE = 1
    CHECKIN_DATE = 2


class DBRepository():
    def query_bookings_by_supplier_id_and_booking_date(self, supplier_id, start, end):
        pass

    def query_bookings_by_supplier_id_and_check_in_date(self, supplier_id, start, end):
        pass


class CacheRepository():
    def contains(self, key):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass


class DBResult():
    pass


def create_key(supplier_id, mode, start, end):
    pass


def map_to_supply_booking(db_result):
    pass


from enum import Enum
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class SupplyQueryDateType(Enum):
    BOOKING_DATE = 1
    CHECKIN_DATE = 2


class SupplyQueryService:
    def __init__():
        DBRepository()
        CacheRepository()

    TTL = 60 * 60

    def query_bookings_by_supplier_id(self, supplier_id, mode, start, end):  # types
        # validations logic to be moved to a separate
        if start.is_after(end):
            raise ValueError("Start date must be before end date")

        if mode == SupplyQueryDateType.BOOKING_DATE and start.is_after(datetime.now()) and end.is_after(datetime.now()):
            raise ValueError("Start date must be before end date")

        if mode == SupplyQueryDateType.CHECKIN_DATE and start.is_after(datetime.now()) and end.is_after(datetime.now()):
            raise ValueError("Start date must be before end date")

        try:
            db_repository = DBRepository()  # object in method mockable dependency ingestion
            cache_repository = CacheRepository()  # object in method mockable dependency ingestion
            db_result = DBResult()
            key = create_key(supplier_id, mode, start, end)
            # concurrency issue
            if mode == SupplyQueryDateType.BOOKING_DATE:
                if cache_repository.contains(key):
                    logger.info(f"Cache hit for key: {key}")
                    db_result = cache_repository.get(key)
                else:
                    logger.info(f"Cache miss for key: {key}")
                    db_result = db_repository.query_bookings_by_supplier_id_and_booking_date(supplier_id, start,
                                                                                             end)  # more db calls
                    cache_repository.put(key, db_result)  # Expiry TTL
            else:
                if cache_repository.contains(key):
                    logger.info(f"Cache hit for key: {key}")
                    db_result = cache_repository.get(key)
                else:
                    logger.info(f"Cache miss for key: {key}")
                    db_result = db_repository.query_bookings_by_supplier_id_and_check_in_date(supplier_id, start, end)
                    cache_repository.put(key, db_result)

            return map_to_supply_booking(db_result)
        except Exception as e:  # custom exceptions   db exceptions   # cache
            logger.error(e)
            raise e

#  no paginatinations   .offset().limit()