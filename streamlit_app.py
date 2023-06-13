import streamlit as st

calPerLossWeight = 7700
calPerGainWeight = 7000


def main():
    # login
    st.set_page_config(page_title='Fitness Tracker',
                       page_icon='💪', layout='wide')

    st.header("Hello!")
    st.write("Congratulations on taking your first step towards a healthy lifestyle. This website will be your go-to website for you to set your fitness goals based on your current state and identify small steps to be taken everyday. Remember the goals suggested by the website are approximate and may not be exact. You can use this as an estimate to achieve your goals! Scroll on!")
    st.write("---")

    st.subheader("Current Stage")

    left_column, right_column = st.columns(2)

    with left_column:

        weight = st.slider("Weight (KG)", min_value=0,
                           max_value=700, value=60, step=1)
        height = st.slider("Height (M)", min_value=0.00,
                           max_value=5.00, value=1.00, step=0.01)

    with right_column:
        st.markdown(
            f"""
            * Weight: {weight} Kilograms
            * Height: {height} Meters
        """
        )

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
            "You can leave the website if you want to, you are on track!")
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
        time = st.number_input(
            "How many days are you looking to loose this weight in?", min_value=60)
        steps_per_day = round(total_steps/time)
        st.write(
            f"For that you need to take approximately {steps_per_day} steps per day while maintaing a good diet.")
    elif cla == "thin":
        change = min_w - change
        st.write(f"You need to gain a minimum {round(change)} KGs")
        time = st.number_input(
            "How many days are you looking to gain this weight in?", min_value=60)
        calories_gain = calPerGainWeight * round(change)
        calories_per_day = round(calories_gain/time)
        st.write(
            f"For that you need to consume approximately {calories_per_day} calories per day while maintaing a good exercise routine.")


if __name__ == '__main__':
    main()
