import streamlit as st
import pandas as pd
import numpy as np
import time

def main():
    st.title('CodeSquad LLC :joy: :cry: :angry:')
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
    st.subheader('Learn More About Sentiment Analysis')
    st.write('## Model was built using Logistic Regression :sunglasses:')
    st.write('Model was train in **Portuguese language**')
    st.write('''Reviews should be in that language (Portuguese) \n
    Option to translate to English is Available''')
    st.write('## **Meet the Team!!!**')

    chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data)
    df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

    option = st.selectbox(
    'Which number do you like best?',
     df['second column'])

    'You selected: ', option

    option = st.sidebar.selectbox(
    'Which guy do you like best?',['', 'muhammed', 'abdulhMMED', 'kpk', 'ISREAL'])
    st.write('You selected:', option)

    left_column, right_column = st.beta_columns(2)
    pressed = st.button('Press me?')
    if pressed:
        right_column.write("Woohoo!")
        left_column.write("Woohoo!")

        latest_iteration = st.empty()
        bar = right_column.progress(0)
        bar2 = left_column.progress(0)

        
        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            bar2.progress(i + 1)

            time.sleep(0.1)

        expander = st.beta_expander("FAQ")
        expander.write("Here you could put in some really, really long explanations...")

        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            time.sleep(0.1)

    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)

    st.sidebar.markdown('we are awesome :sunglasses:')



if __name__ == "__main__":
    main()