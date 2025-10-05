import glob
import os
import ffmpeg

# 入出力先
src_dir = "src_videos/"
dst_dir = "dst_videos/"

# 圧縮パラメータ
prm_crf = 30            # 画質
prm_scale_factor = 1    # 解像度の圧縮率
prm_fps = 30            # fps

def compress_video(input_path, output_path, crf=30, scale_factor=1, fps=30):
    (
        ffmpeg
        .input(input_path)
        .filter('scale', f'iw*{scale_factor}', f'ih*{scale_factor}')
        .output(output_path, r=fps, vcodec='libx264', crf=crf, an=None)
        .run()
    )

def main():
    files = (
        glob.glob(src_dir + "**/*.mp4", recursive=True)
        + glob.glob(src_dir + "**/*.MP4", recursive=True)
    )
    for file in files:
        file_name = os.path.splitext(os.path.basename(file))[0]
        dir_name = dst_dir + "/".join(file.split("/")[1:-1])
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        dst_name = dir_name + file_name + ".mp4"
        print("compress: " + file + "→" + dst_name)
        compress_video(file, dst_name, prm_crf, prm_scale_factor, prm_fps)

if __name__ == "__main__":
    main()
