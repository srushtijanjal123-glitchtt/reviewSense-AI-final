
import streamlit as st
import joblib

# Load the trained three-class model
model = joblib.load("reviewsense_svm_3class.pkl")

# Page configuration
st.set_page_config(
    page_title="ReviewSense AI",
    page_icon="🍽️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom website styling
st.markdown("""
<style>
/* Main page */
.stApp {
    background: linear-gradient(135deg, #fff8ef, #f5e8da);
    color: #542b1c;
}

.main .block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Default text colors */
.stApp p,
.stApp label,
.stApp h2,
.stApp h3,
.stApp li,
.stApp [data-testid="stMarkdownContainer"] {
    color: #542b1c;
}

/* Hero header */
.hero {
    background: #ffffff;
    padding: 28px;
    border-radius: 18px;
    border: 1px solid #ead9c8;
    margin-bottom: 25px;
    box-shadow: 0 5px 18px rgba(84, 43, 28, 0.06);
}

.hero h1 {
    color: #542b1c !important;
    font-size: 40px;
    margin-bottom: 8px;
}

.hero .tagline {
    color: #a94f2b !important;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
}

.hero p {
    color: #765d4d !important;
    font-size: 16px;
    line-height: 1.7;
}

/* Review input */
.stTextArea textarea {
    background-color: #ffffff !important;
    color: #542b1c !important;
    border: 1px solid #d9c3af !important;
    border-radius: 12px !important;
    font-size: 15px !important;
}

.stTextArea textarea::placeholder {
    color: #927d6d !important;
    opacity: 1;
}

/* Input label */
.stTextArea label,
.stTextArea label p {
    color: #542b1c !important;
    font-weight: 600;
}

/* Buttons */
.stButton > button {
    background-color: #a94f2b;
    color: #ffffff !important;
    border: 1px solid #a94f2b;
    border-radius: 10px;
    min-height: 44px;
    font-weight: 600;
    transition: 0.2s ease;
}

.stButton > button p {
    color: #ffffff !important;
}

.stButton > button:hover {
    background-color: #813b21;
    border-color: #813b21;
    color: #ffffff !important;
}

/* Result cards */
.result {
    padding: 20px;
    border-radius: 14px;
    margin-top: 18px;
    margin-bottom: 12px;
    font-size: 22px;
    font-weight: 700;
}

.positive {
    background-color: #e5f4e8;
    color: #237543 !important;
    border: 1px solid #b7dfc1;
}

.negative {
    background-color: #fce5e3;
    color: #b43a36 !important;
    border: 1px solid #efc0bd;
}

.neutral {
    background-color: #fff0cc;
    color: #805600 !important;
    border: 1px solid #f0d58d;
}

/* Expandable information section */
[data-testid="stExpander"] {
    background-color: #ffffff;
    border: 1px solid #ead9c8;
    border-radius: 12px;
}

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p {
    color: #542b1c !important;
}

/* Captions and footer */
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {
    color: #765d4d !important;
}

.footer {
    text-align: center;
    color: #765d4d !important;
    font-size: 13px;
    line-height: 1.8;
    margin-top: 35px;
    padding: 15px;
    border-top: 1px solid #ead9c8;
}
</style>
""", unsafe_allow_html=True)

# Website header
st.markdown("""
<div class="hero">
    <h1>🍽️ ReviewSense AI</h1>
    <p class="tagline">RESTAURANT REVIEW INTELLIGENCE</p>
    <p>
        Every review tells a story. Discover the sentiment behind
        restaurant feedback using Natural Language Processing
        and Machine Learning.
    </p>
</div>
""", unsafe_allow_html=True)

# Review analysis section
st.subheader("📝 Analyze a Restaurant Review")

st.write(
    "Enter a restaurant review below to predict whether "
    "the sentiment is positive, negative, or neutral."
)

# Sample review selection
if "review_text" not in st.session_state:
    st.session_state.review_text = ""

def select_sample(text):
    st.session_state.review_text = text

st.caption("Try an example or enter your own review.")

col1, col2, col3 = st.columns(3)

with col1:
    st.button(
        "😊 Positive example",
        use_container_width=True,
        on_click=select_sample,
        args=("The food was delicious and the service was excellent.",)
    )

with col2:
    st.button(
        "😞 Negative example",
        use_container_width=True,
        on_click=select_sample,
        args=("The food was cold and tasteless, and the service was terrible.",)
    )

with col3:
    st.button(
        "😐 Neutral example",
        use_container_width=True,
        on_click=select_sample,
        args=("The restaurant serves breakfast, lunch, and dinner.",)
    )

# Review input box
review = st.text_area(
    "Your restaurant review",
    key="review_text",
    height=150,
    placeholder="Example: The food was delicious and the staff were friendly..."
)

# Analyze sentiment
if st.button("🔍 Analyze Sentiment", use_container_width=True):
    if review.strip():
        prediction = model.predict([review.strip()])[0]

        if prediction == "Positive":
            st.markdown(
                '<div class="result positive">😊 Positive Review</div>',
                unsafe_allow_html=True
            )
            st.write("The model predicts a positive sentiment.")

        elif prediction == "Negative":
            st.markdown(
                '<div class="result negative">😞 Negative Review</div>',
                unsafe_allow_html=True
            )
            st.write("The model predicts a negative sentiment.")

        else:
            st.markdown(
                '<div class="result neutral">😐 Neutral Review</div>',
                unsafe_allow_html=True
            )
            st.write("The model predicts a neutral sentiment.")

        st.caption(
            "This is a machine-learning prediction and may not "
            "always match the review's actual sentiment."
        )

    else:
        st.warning("Please enter a restaurant review first.")

# About the project
with st.expander("ℹ️ About ReviewSense AI"):
    st.write(
        "ReviewSense AI is an academic project that classifies "
        "restaurant reviews into three sentiment categories."
    )
    st.write("**Dataset:** Yelp restaurant reviews")
    st.write("**Text representation:** TF-IDF")
    st.write("**Classifier:** Linear Support Vector Machine (SVM)")
    st.write(
        "The model was evaluated on a held-out test set. "
        "Neutral sentiment classification is a known limitation."
    )

# Footer
st.markdown("""
<div class="footer">
    Powered by TF-IDF and Support Vector Machine (SVM)<br>
    ReviewSense AI | NLP Academic Project
</div>
""", unsafe_allow_html=True)
