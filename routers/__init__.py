from routers.greeting import router as greeting_router
from routers.conversion import router as conversion_router
from routers.chat import router as chat_router


all_routers = [
    greeting_router,
    conversion_router,
    chat_router
]