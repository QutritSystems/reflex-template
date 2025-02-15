import reflex as rx

config = rx.Config(
    app_name="todo_app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.PROD,
    backend_host="0.0.0.0",
    backend_port=8080,
)
