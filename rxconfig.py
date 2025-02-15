import reflex as rx

config = rx.Config(
    app_name="todo_app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)
