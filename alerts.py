from plyer import notification

from plyer import notification

def send_alert(game_name, old_price, new_price, status):
    if status == 0:
        return
    elif status > 0:
        title = "🔥 Steam Price Drop!"
    else:
        title = "📈 Steam Price Increase!"

    message = (
        f"{game_name}\n"
        f"{old_price} → {new_price}"
    )

    notification.notify(
        title=title,
        message=message,
        app_name="Steam Tracker",
        timeout=10
    )