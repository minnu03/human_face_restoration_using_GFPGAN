import streamlit as st
import os
import moviepy.editor as mp
import subprocess
import time
import moviepy
import threading

st.set_page_config(layout="wide")


def run_script(cmd):
    subprocess.call(cmd, shell=True)


def vid_found(op_filename):
    directory_to_monitor = r"C:\Users\cutie\OneDrive\Desktop\VideoRestore-main\video_rebuild\result"
    file_found = any(op_filename in f for f in os.listdir(directory_to_monitor))
    if file_found:
        return True
    else:
        return False


def vid_process(uploaded_file, status=False):
    if uploaded_file:
        st.success("Video uploaded and saved successfully!")
        filename, _ = os.path.splitext(uploaded_file.name)
        op_filename = filename + "_restored" + ".mp3"
        video_directory = 'video_rebuild/src'
        os.chmod(video_directory, 0o775)
        print("ok")
        with open(os.path.join("video_rebuild/src", filename), "wb") as f:
            f.write(uploaded_file.read())
            return True
    elif status:
        st.warning("File Save Failed! Please try again.")
        return False


def progress_bar():
    bar = """

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Continuous Progress Indicator</title>
<style>
    #progress-container {
        width: 650px;
        height: 10px;
        margin: 50px auto;
        border: 1px solid #ccc; /* Adding border */
        overflow: hidden; /* Ensuring the progress bar stays within the container */
    }

    progress {
        width: 100%;
        height: 100px;
        border: none;
        background-color: blue;
        position: relative;
        animation: progressAnimation 2s linear infinite;
        box-sizing: border-box; /* Ensure the width of the progress bar includes padding and border */
    }


    @keyframes progressAnimation {
        0% { left: -100%; }
        100% { left: 100%; }
    }
</style>
</head>
<body>

<div id="progress-container">
    <progress></progress>
</div>

</body>
</html>
    """
    st.markdown(bar, unsafe_allow_html=True)


def main():
    title = "Video Face Restoration"

    html_content = f"""
    <h1 style="text-align: center; font-family: Tahoma">{title}</h1>
    """
    st.markdown(html_content, unsafe_allow_html=True)

    para = "Have a video with blurry faces? Enhance them using our app!"
    html_content = f"""
    <p style="text-align: center; font-family: Tahoma">{para}</h1>
    """
    st.markdown(html_content, unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    vt1 = "Original:"
    vt2 = "Restored:"
    ext, col1, col2, ext2 = st.columns((4, 9, 9, 4))

    vh1 = f"""
        <video width=650 height controls autoplay loop muted>
    <source src="http://localhost:8000/video_rebuild/src/ipmv.mp4" type="video/mp4" />
    </video>
    """

    vh2 = f"""
        <video width=650 controls autoplay loop muted>
    <source src="http://localhost:8000/video_rebuild/result/opmv.mp4" type="video/mp4" />
    </video>
    """

    with col1:
        st.markdown(f"""<h6 style="font-family: Tahoma">{vt1}</h6>""", unsafe_allow_html=True)
        st.markdown(vh1, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""<h6 style="font-family: Tahoma">{vt2}</h6>""", unsafe_allow_html=True)
        st.markdown(vh2, unsafe_allow_html=True)

    " "

    st.markdown(""" <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Text and Image Layout</title>
  <style>
    body {
      font-family: Tahoma;
      margin: 0;
      padding: 0;
    }
    .container {
      display: flex;
      flex-wrap: wrap;
    }
    .container > div {
      flex: 1 0 50%;
      padding: 10px;
      box-sizing: border-box;
    }
    .text-section {
      text-align: justify;
    }
    .image-section {
      text-align: center;
    }
    img {
      width: 600px;
      height: 250px;
    }
  </style>
</head>
<body>
  <h2 align="center" style="font-family:tahoma">Why Us?</h1>
  <div class="container">
    <div class="text-section">
      <p style="color:#02a349"> <br> <br> <br> Experience the transformative power of our cutting-edge facial restoration algorithm, designed to breathe life into your videos like never before. With our advanced technology, even the most blurred or damaged faces can be seamlessly transformed into stunning portraits of beauty and realism. Say goodbye to limitations and hello to a new era of video enhancement. Trust in our advanced facial restoration algorithm to elevate your content to new heights, one beautiful face at a time</p>
    </div>
    <div class="image-section">
      <img src="http://localhost:8000/comp1.jpeg" alt="Nature Image">
    </div>
    <div class="image-section">
      <video width=500 controls autoplay loop muted>
    <source src="http://localhost:8000/compslide.mp4" type="video/mp4" />
    </video>
    </div>
    <div class="text-section">
      <p style="color:#02a349"> <br> <br> <br> Memories, no matter how distant, deserve to be cherished. Even the faintest glimpses from decades past can hold immense emotional value. Hence we crafted this algorithm that breathes new life into these precious snapshots. Our technology goes beyond simple restoration; it transforms faded faces, imbuing them with a clarity that reflects the spirit you remember. It's like stepping back in time and seeing your loved ones anew, their features brought back to life.</p>
    </div>
  </div>
</body>
</html>
""", unsafe_allow_html=True)

    " "
    " "
    " "

    st.markdown(f"""
    <h3 style="text-align: center; font-family: Tahoma">Try It Yourself!</h1>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose a video file", type=["mp4"])
    print("?????")
    if uploaded_file:
        st.success("Video uploaded and saved successfully!")
        filename, _ = os.path.splitext(uploaded_file.name)
        mod_filename = filename.replace(" ", "_")
        op_filename = mod_filename + "_restored" + ".mp4"
        video_directory = 'video_rebuild/src'
        os.chmod(video_directory, 0o775)
        print("ok")
        with open(os.path.join("video_rebuild/src", mod_filename), "wb") as f:
            f.write(uploaded_file.read())

        cmd = f"python video_rebuild/main.py --video ./video_rebuild/src/{mod_filename} --save-path ./video_rebuild/result/{op_filename}"
        # subprocess_thread = threading.Thread(target=run_script, args=(cmd,))
        # subprocess_thread.start()
        " "
        " "
        while True:
            if vid_found(op_filename):

                vt1 = "Uploaded Video:"
                vt2 = "Restored Video"
                too, ext, col1, col2, ext2 = st.columns((1, 4, 11, 10, 4))

                vh1 = f"""
                       <video width=650 height controls autoplay loop muted>
                   <source src="http://localhost:8000/video_rebuild/src/{mod_filename}" type="video/mp4" />
                   </video>
                   """

                vh2 = f"""
                       <video width=650 controls autoplay loop muted>
                   <source src="http://localhost:8000/video_rebuild/result/{op_filename}" type="video/mp4" />
                   </video>
                   """

                with col1:
                    st.markdown(f"""<h6 style="font-family: Tahoma">{vt1}</h6>""", unsafe_allow_html=True)
                    st.markdown(vh1, unsafe_allow_html=True)

                with col2:
                    st.markdown(f"""<h6 style="font-family: Tahoma">{vt2}</h6>""", unsafe_allow_html=True)
                    st.markdown(vh2, unsafe_allow_html=True)

                video_path = f"video_rebuild/result/{op_filename}"

                with open(video_path, "rb") as video_file:
                    video_data = video_file.read()

                with ext:
                    " "
                    " "
                    " "
                    st.image("http://localhost:8000/download.png", width=150)
                    downloaded = st.download_button(
                        label="Download Video",
                        data=video_data,
                        file_name=op_filename,
                        mime="video/mp4",
                        key="one"
                    )

                if downloaded:
                    st.success("Video downloaded successfully!")
                break

            else:
                with st.spinner('Processing'):
                        time.sleep(5)
                print("wh")
        else:
            pass


if __name__ == "__main__":
    main()