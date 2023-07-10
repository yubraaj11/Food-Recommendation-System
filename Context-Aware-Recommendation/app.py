import streamlit as st
from Recommendation import recommendation

# Dictionary to map weekdays to numerical values
weekday_mapping = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6
}

def main():

    st.title("Food Recommendation")

    st.write("Enter the day and hour to get food recommendations.")

    # Dropdown to select the day of the week
    day = st.selectbox("Day", list(weekday_mapping.keys()))
    hour = st.number_input("Hour", min_value=0, max_value=23, value=0)

    if st.button("Get Recommendations"):
        # Convert the selected day to numerical value using the mapping
        day_value = weekday_mapping[day]
        product_names = recommendation(day=day_value, hour=hour)
        for product_name in product_names:
            st.write(product_name)

if __name__ == "__main__":
    main()
