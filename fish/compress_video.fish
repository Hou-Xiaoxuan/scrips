# @Author: houxiaoxuan
# @Description: 压缩视频，同时保留音质不变，用以存档
# @FilePath: /scrips/fish/compress_video.fish

function compress_video --description "压缩视频，同时保留音质不变，用以存档"
    echo "---Start compress video---\n"
    # 遍历传递的参数
    for filename in $argv
        echo " Compress $filename \n"
        # 提取320k音频
        ffmpeg -i $filename -ab 320k $filename-音频.mp3
        # 2048k 1920*1080提取视频(不包括音频)
        ffmpeg -i $filename -an -s 1920x1080 -b:v 2048k $filename-视频.mp4
        # 合并视频和音频
        ffmpeg -i $filename-视频.mp4 -i $filename-音频.mp3 -vcodec copy -acodec $filename-compressed.mp4

        # 删除临时文件
        rm $filename-视频.mp4
        rm $filename-音频.mp3
        done
    end
    echo "\n---Compress video finished---"
end
