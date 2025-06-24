from app.ui.layout import outputs

def update_output(data):
    for key, value in data.items():
        outputs[key].config(text=f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}")
