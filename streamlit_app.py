import streamlit as st

calPerLossWeight = 7700
calPerGainWeight = 7000


def main():
    # login
    st.set_page_config(page_title='Fitness Tracker',
                       page_icon='💪', layout='wide')

    st.header("Hello!")
    st.write("Congratulations on taking your first step towards a healthy lifestyle. This website will be your go-to website for you to set your fitness goals based on your current state and identify small steps to be taken everyday. Remember, the goals suggested by the website are approximate. You can use this as an estimate to achieve your goals! Scroll on! Take your first step towards a new you!")
    st.write("---")

    st.subheader("Current Stage")

    left_column, right_column = st.columns(2)

    with left_column:
        st.write("Weight (KGs)")
        weight = st.slider("", min_value=0,
                           max_value=700, value=60, step=1)
        st.write("##")
        st.write("Height")
        left, right = st.columns(2)

        with left:

            height_f = st.number_input(
                "Feet", min_value=1.0, max_value=8.0, step=1.0)

        with right:
            height_i = st.number_input(
                "Inches", min_value=0.0, max_value=11.9, step=1.0)

        height = (height_f * 0.3048) + (height_i * 0.0254)

    with right_column:
        st.write(f"Weight: {weight} Kilograms")
        st.write(f"Height: {height_f} Feet and {height_i} Inches")
        st.write("#")
        st.write("#")

        bmi = (weight/(height * height))
        st.subheader(f"BMI: {round(bmi, 2)} KG/M\u00b2")

        status = ""
        cla = ""
        if bmi < 16:
            st.error("You are in classification: Severe Thinness", icon="🚨")
            status = "Severe thin"
            cla = "thin"
        elif bmi <= 17 and bmi >= 16:
            st.error("You are in classification: Moderate Thinness", icon="🚨")
            status = "Severe thin"
            cla = "thin"
        elif bmi <= 18.5 and bmi >= 17:
            st.warning("You are in classification: Mild Thinness", icon="⚠️")
            status = "Moderate thin"
            cla = "thin"
        elif bmi <= 25 and bmi >= 18.5:
            st.success("You are in classification: Healthy", icon="✅")
            status = "Perfect"
        elif bmi <= 30 and bmi >= 25:
            st.warning("You are in classification: Overweight", icon="⚠️")
            status = "Moderate obese"
            cla = "obese"
        elif bmi <= 35 and bmi >= 30:
            st.error("You are in classification: Obese Class 1", icon="🚨")
            status = "Severe obese"
            cla = "obese"
        elif bmi <= 40 and bmi >= 35:
            st.error("You are in classification: Obese Class 2", icon="🚨")
            status = "Severe obese"
            cla = "obese"
        elif bmi > 40:
            st.error("You are in classification: Obese Class 3", icon="🚨")
            status = "Severe obese"
            cla = "obese"

    st.write("---")
    st.subheader("Goals")
    if status == "Severe thin":
        st.write("You need to gain weight. But don't worry, let's work together!")
    elif status == "Moderate thin":
        st.write("You need to gain some weight, but you are in good shape!")
    elif status == "Perfect":
        st.write("Great Job! Maintain your fitness!")
    elif status == "Moderate obese":
        st.write("You need to lose some weight, but you are in good shape!")
    elif status == "Severe obese":
        st.write("You need to lose weight. But don't worry, let's work together!")

    min_w = height * height * 18.5
    max_w = height * height * 25

    if weight >= min_w and weight <= max_w:
        st.subheader(
            "You can continue to enjoy the goodness of life! You are on track!")
    else:
        st.write(
            f"To be 'Healthy' you need to be in-between weights: {round(min_w, 2)} KGs and {round(max_w, 2)} KGs")

    st.write("#")
    change = 0
    total_steps = 0
    cal = 0
    time = 0
    if cla == "obese":
        change = weight - max_w
        calories_burn = calPerLossWeight * round(change)
        total_steps = round(calories_burn/0.04)
        st.write(f"You need to lose a minimum {round(change)} KGs")
        time = st.slider("How many months are you looking to loose this weight in?", min_value=1,
                         max_value=60, value=6, step=1)
        steps_per_day = round(total_steps/(time*30))
        st.write(
            f"For that you need to take approximately {steps_per_day} steps per day while maintaining a good diet and a healthy lifestyle.")
        st.write(
            "Continue your journey of 'a new you' with a positive mindset. Bon voyage!")
    elif cla == "thin":
        change = min_w - change
        st.write(f"You need to gain a minimum {round(change)} KGs")
        time = st.slider("How many months are you looking to loose this weight in?", min_value=1,
                         max_value=60, value=6, step=1)
        calories_gain = calPerGainWeight * round(change)
        calories_per_day = round(calories_gain/(time*30))
        st.write(
            f"For that you need to consume approximately {calories_per_day} calories per day while maintaining a good exercise routine and a healthy lifestyle.")
        st.write(
            "Continue your journey of 'a new you' with a positive mindset. Bon voyage!")


if __name__ == '__main__':
    main()
