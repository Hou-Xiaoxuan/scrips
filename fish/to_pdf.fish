# @Author: houxiaoxuan
# @Description: 
# @FilePath: /scrips/fish/to_pdf.fish

# 图片转pdf
function to_pdf --description "当前目录图片转pdf" -a type
    for i in *.$type                                                                                                                                                                        
        # echo $i
        convert $i $i.pdf
    end
end
