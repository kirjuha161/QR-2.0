import qrcode
from io import BytesIO
from django.shortcuts import render
import base64


def generate_qr_code(request):
    qr_code_url = None  # QR-код отсутствует до нажатия кнопки
    if request.method == "POST":
        # Получаем данные из формы
        data = request.POST.get("data", "Default QR Code Data")
        style = request.POST.get("style", "default")  # Получаем выбранный стиль

        # Устанавливаем цвета в зависимости от выбранного стиля
        if style == "default":
            fill_color = "#000000"  # Черный код
            back_color = "#FFFFFF"  # Белый фон
        elif style == "blue":
            fill_color = "#0000FF"  # Синий код
            back_color = "#FFFFFF"  # Белый фон
        elif style == "red":
            fill_color = "#FF0000"  # Красный код
            back_color = "#FFFF00"  # Желтый фон
        elif style == "green":
            fill_color = "#00FF00"  # Зеленый код
            back_color = "#000000"  # Черный фон
        else:
            fill_color = "#000000"
            back_color = "#FFFFFF"

        # Генерация QR-кода с выбранными цветами
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Сохранение изображения в буфер
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Преобразуем QR-код в base64 для отображения в шаблоне
        qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()
        qr_code_url = f"data:image/png;base64,{qr_code_base64}"

    return render(
        request, "qrcode_generator/generate_qr.html", {"qr_code_url": qr_code_url}
    )
