import utils.widgets
import streamlit as st

WRAPPER = ['utils.widgets.excel_file_uploader']

def main():
    st.title(":gear: My Toolbox")
    util = utils.widgets.selectbox_without_default("Select wrapper", WRAPPER,
                                                   "Select a wrapper")

    st.header("Demonstration")

    if util == '':
        st.stop()

    if util == 'utils.excel_file_uploader':
        st.subheader("Upload Excel Files")
        data = utils.widgets.excel_file_uploader("Upload the "
                                                 "/input/excel.xlsx file")
        st.write(data)

if __name__ == '__main__':
    main()
