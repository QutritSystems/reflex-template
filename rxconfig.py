import reflex as rx

config = rx.Config(
    app_name="todo_app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.PROD,  # Changed to PROD
    frontend_port=3000,
    backend_port=8000,
    frontend_host="0.0.0.0",
    backend_host="0.0.0.0",
)
