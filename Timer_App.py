## Timer App ##

import streamlit as st
import time
import pyttsx3


def countdown(timer, name, exercise_name):
    timer_text = st.empty() 
    timer_text.text(f"{name} Timer: {timer // 60:02d}:{timer % 60:02d}") 
    
    while timer > 0:
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        timer_text.text(f"{name}'s Timer: {mins:02d}:{secs:02d}") 
        time.sleep(1)
        timer -= 1
    
    st.text(f"{name}'s Timer: {exercise_name} has been completed.")
    engine = pyttsx3.init()
    engine.say(f"{name} has finished their {exercise_name}.")
    engine.runAndWait()


def minutes_to_seconds(minutes):
    return minutes * 60


def main():
    st.title("PT Exercise Timer")
    
    person_name = st.text_input("Enter Name:")
    exercise_name = st.text_input("Enter Exercise Name:")
    interval = st.selectbox("Select Interval (minutes):", list(range(1, 5)))
    timer_seconds = minutes_to_seconds(interval)
    
    if st.button("Start Timer"):
        countdown(timer_seconds, person_name, exercise_name)

if __name__ == "__main__":
    main()

