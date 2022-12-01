from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin, fsmAdmin, notification
import logging
from database.mentors_database import sql_create
import asyncio


async def on_startup(_):
    asyncio.create_task(notification.scheduler())

    sql_create()

notification.register_handlers_notification(dp)
fsmAdmin.register_handler_fsmAdmin(dp)
client.register_client_handlers(dp)
# callback.register_callback_handlers(dp)
admin.register_handler_admin(dp)


extra.register_handler_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
