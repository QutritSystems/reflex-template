import reflex as rx
import os

config = rx.Config(
    app_name="todo_app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.PROD,
    backend_host="0.0.0.0",
    port=8080  # Railway's default port
)
