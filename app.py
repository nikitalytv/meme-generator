from flask import Flask, render_template, request, send_file
from PIL import Image, ImageFont, ImageDraw, ImageOps
import io
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    file = request.files["image"]
    top = request.form["top"]
    bottom = request.form["bottom"]

    image = Image.open(file.stream)
    image = ImageOps.contain(image, (800, 600))

    draw = ImageDraw.Draw(image)
    W, H = image.size

    def fit_font(draw, text, max_font_size, max_width):
        font_size = max_font_size
        while font_size > 10:
            # font = ImageFont.truetype("/Library/Fonts/Arial.ttf", font_size)
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
            w = draw.textbbox((0, 0), text, font=font, stroke_width=4)[2]
            if w <= max_width - 30:
                return font
            font_size -= 2
        return font

    def draw_centered(text, y):
        font = fit_font(draw, text, 70, W)
        bbox = draw.textbbox((0, 0), text, font=font, stroke_width=4)
        text_w = bbox[2] - bbox[0]
        x = (W - text_w) / 2

        draw.text(
            (x, y),
            text,
            fill="white",
            font=font,
            stroke_width=4,
            stroke_fill="black"
        )

    draw_centered(top, 20)
    draw_centered(bottom, H - 100)

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
    # app.run(debug=True)
