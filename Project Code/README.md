## Initial Requirements

- Python >= 3.7
- PyTorch >= 1.7
- NVIDIA GPU + CUDA (optional)

## Installation Guide


1. Create Cuda Virtual Environment
   ```bash
   conda create -n video python=3.7
   conda activate video
   ```

2. Install Cuda (only for Nvidia)

   ```bash
   conda install cudatoolkit=10.2
   conda install cudnn
   ```

3. Clone Repository

   ```bash
   git clone https://github.com/minnu03/human_face_restoration_using_GFPGAN.git
   cd project_code
   ```

4. Install Requirements

   ```bash
   pip install -r requirements.txt
   ```

## Download pre-trained weights

- [GFPGANv1.3.pth](https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth)
- [Pretrained StyleGAN2 model: StyleGAN2_512_Cmul1_FFHQ_B12G4_scratch_800k.pth](https://github.com/TencentARC/GFPGAN/releases/download/v0.1.0/StyleGAN2_512_Cmul1_FFHQ_B12G4_scratch_800k.pth)
- [Component locations of FFHQ: FFHQ_eye_mouth_landmarks_512.pth](https://github.com/TencentARC/GFPGAN/releases/download/v0.1.0/FFHQ_eye_mouth_landmarks_512.pth)
- [A simple ArcFace model: arcface_resnet18.pth](https://github.com/TencentARC/GFPGAN/releases/download/v0.1.0/arcface_resnet18.pth)

Place it in `experiments/pretrained_models` folder

## Execution

1. Host an http server

   ```bash
   python -m http.server 8000
   ```
2. Run the webapp

   ```bash
   streamlit run frontend.py
   ```

For debugging:
   ```bash
   python video_rebuild/main.py --video ./video_rebuild/src/demo04.mp4 --save-path ./video_rebuild/result/output.mp4
   ```
