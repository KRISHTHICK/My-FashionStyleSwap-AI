import streamlit as st
import cv2
import os
import numpy as np
from PIL import Image
import random

st.set_page_config(page_title="🧢 FashionStyleSwap AI", layout="wide")

st.title("🧢 FashionStyleSwap AI - Virtual Outfit Swapper & Stylist")

# Upload images
user_img_file = st.file_uploader("📤 Upload Your Image", type=["jpg", "jpeg", "png"])
outfit_img_file = st.file_uploader("👕 Upload Outfit Image", type=["jpg", "jpeg", "png"])

# Image enhancement
def enhance_image(image):
    img_np = np.array(image)
    enhanced = cv2.detailEnhance(img_np, sigma_s=10, sigma_r=0.15)
    return Image.fromarray(enhanced)

# Overlay simulation (demo)
def swap_outfit(user_img, outfit_img):
    user_img = user_img.resize((400, 400))
    outfit_img = outfit_img.resize((400, 400))
    blended = Image.blend(user_img, outfit_img, alpha=0.4)
    return blended

# Accessory recommender
def recommend_accessories():
    options = [
        "👜 White Leather Bag",
        "👟 Chunky Sneakers",
        "⌚ Minimalist Watch",
        "🕶️ Aviator Sunglasses",
        "🧢 Cap"
    ]
    return random.sample(options, 3)

# Style caption generator
def generate_caption():
    captions = [
        "Rocking this modern streetwear look! 🔥",
        "Effortless vibes with a touch of class. ✨",
        "Keeping it casual, keeping it chic. 💃",
        "Elegance in simplicity. #OOTD",
    ]
    return random.choice(captions)

if user_img_file and outfit_img_file:
    user_img = Image.open(user_img_file).convert("RGB")
    outfit_img = Image.open(outfit_img_file).convert("RGB")

    st.image([user_img, outfit_img], caption=["Your Photo", "Outfit Image"], width=300)

    st.subheader("✨ Enhanced & Blended View")
    enhanced_user = enhance_image(user_img)
    enhanced_outfit = enhance_image(outfit_img)
    styled_img = swap_outfit(enhanced_user, enhanced_outfit)
    st.image(styled_img, caption="Virtual Style Preview", use_column_width=True)

    # Download final image
    st.download_button("📥 Download Styled Image", data=styled_img.tobytes(), file_name="styled_output.jpg")

    # Accessories
    st.subheader("🎒 Recommended Accessories")
    accessories = recommend_accessories()
    st.write(", ".join(accessories))

    # Caption & Hashtags
    st.subheader("✍️ Style Caption Generator")
    caption = generate_caption()
    hashtags = "#fashion #styleinspo #virtualtryon"
    st.text_area("Caption:", caption, height=70)
    st.text_area("Hashtags:", hashtags, height=80)

else:
    st.info("Please upload both your image and an outfit image to begin.")

